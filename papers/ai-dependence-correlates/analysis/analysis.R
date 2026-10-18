# Psychological correlates of dependence on AI: meta-analysis (protocol v1.0, sections 13 and 15-17; deviations.md D4).
#
# Reads forms/samples.csv and forms/effects.csv (verified extraction, extraction/finalize.py) and writes the results
# to analysis/results/ and the figures to analysis/figures/.
# Effect size: zero-order r as Fisher's z (section 13). Model per correlate: CHE (random effects for samples and for
# effects within samples, assumed within-sample correlation 0.6) with CR2 cluster-robust inference, clustered by study
# (section 15b). Pairs reported both as observed and latent correlations enter once, as the observed one (D4, rule 3).
#
# Run from the repository root:
#   Rscript papers/ai-dependence-correlates/analysis/analysis.R [forms_dir] [out_dir]
# Defaults: papers/ai-dependence-correlates/forms and papers/ai-dependence-correlates/analysis.

suppressPackageStartupMessages({
  library(metafor)
  library(clubSandwich)
  library(weightr)
  library(dplyr)
  library(readr)
  library(tidyr)
  library(ggplot2)
})

args <- commandArgs(trailingOnly = TRUE)
forms_dir <- if (length(args) >= 1) args[1] else "papers/ai-dependence-correlates/forms"
out_root <- if (length(args) >= 2) args[2] else "papers/ai-dependence-correlates/analysis"
res_dir <- file.path(out_root, "results")
fig_dir <- file.path(out_root, "figures")
dir.create(res_dir, showWarnings = FALSE, recursive = TRUE)
dir.create(fig_dir, showWarnings = FALSE, recursive = TRUE)
MIN_K <- 3        # section 15b: a pooled estimate needs at least three independent samples
MIN_K_MOD <- 10   # moderators only when k >= 10 samples
RHO <- 0.6        # assumed within-sample correlation between effects (section 15b)
PRIMARY <- c("depression", "anxiety", "stress", "loneliness", "social_anxiety", "self_esteem", "procrastination")
TYPES <- c("T1", "T2", "T3")   # the contrast of the primary moderator; T4 reported apart

# ---------------------------------------------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------------------------------------------

num <- function(x) {
  x <- gsub("[−–—]", "-", trimws(as.character(x)))
  x <- sub("^(-?)\\s*\\.", "\\10.", gsub(",", "", x))
  suppressWarnings(as.numeric(sub("^(-?[0-9.]+).*$", "\\1", x)))
}
# Coefficients and alphas: a decimal comma (",57", "0,022" in Turkish and Spanish reports) is a decimal point
num_r <- function(x) {
  x <- trimws(as.character(x))
  num(ifelse(grepl("^[-−–]?\\s*[0-9]*,[0-9]+", x) & !grepl(".", x, fixed = TRUE), sub(",", ".", x), x))
}
# n of a sample whose correlation table gives no n: the smallest n the report names ("307 or 361" -> 307;
# "551 at baseline ... 503 complete cases" -> 503); conservative (deviations.md, D5)
n_fallback <- function(x) {
  y <- gsub(",", "", x)
  v <- suppressWarnings(as.numeric(regmatches(y, gregexpr("[0-9]{2,}", y))[[1]]))
  v <- v[!is.na(v) & v >= 10 & v < 1e6]
  if (length(v)) min(v) else NA_real_
}

samples <- read_csv(file.path(forms_dir, "samples.csv"), col_types = cols(.default = "c"), na = character())
effects <- read_csv(file.path(forms_dir, "effects.csv"), col_types = cols(.default = "c"), na = character())

samples <- samples |>
  mutate(n_s = coalesce(num(n_analysed), vapply(n_analysed, n_fallback, numeric(1))),
         n_fallback_used = is.na(num(n_analysed)) & !is.na(n_s), age_mean_n = num(age_mean), pct_female_n = num(pct_female),
         year_n = num(year), journal = pub_status == "journal",
         design2 = ifelse(design == "panel", "first wave of a panel", "cross-sectional or other"),
         region2 = ifelse(region %in% c("", "NR", "multi"), NA_character_, region),
         population2 = ifelse(population %in% c("", "NR"), NA_character_, population),
         ai2 = ifelse(ai_system %in% c("", "NR"), NA_character_, ai_system))
write_csv(samples |> filter(n_fallback_used) |> select(sample_id, n_analysed, n_used = n_s),
          file.path(res_dir, "n_fallback.csv"))

# r from a reported OR or d (Borenstein et al., 2009): d = ln(OR) * sqrt(3) / pi; r = d / sqrt(d^2 + a)
r_from_conv <- function(stat_type, value, ci_or_se, n) {
  if (stat_type == "converted_or") {
    d <- log(num_r(value)) * sqrt(3) / pi
  } else {
    parts <- strsplit(value, ";")[[1]]
    if (length(parts) == 2) {
      g <- lapply(parts, function(p) num(strsplit(p, ",")[[1]]))
      sp <- sqrt(((g[[1]][3] - 1) * g[[1]][2]^2 + (g[[2]][3] - 1) * g[[2]][2]^2) / (g[[1]][3] + g[[2]][3] - 2))
      d <- (g[[1]][1] - g[[2]][1]) / sp
      n1 <- g[[1]][3]; n2 <- g[[2]][3]
      return(d / sqrt(d^2 + (n1 + n2)^2 / (n1 * n2)))
    }
    d <- num_r(value)
  }
  gs <- num(strsplit(gsub("[^0-9.,]", " ", ci_or_se), "[ ,]+")[[1]])
  a <- if (length(gs) >= 2 && all(!is.na(gs[1:2])) && all(gs[1:2] > 1)) (gs[1] + gs[2])^2 / (gs[1] * gs[2]) else 4
  d / sqrt(d^2 + a)
}

effects <- effects |>
  left_join(samples |> select(sample_id, study_id, n_s), by = "sample_id") |>
  mutate(n_e = coalesce(num(n), n_s),
         r_raw = mapply(function(t, v, c, n) if (t %in% c("converted_or", "converted_d")) r_from_conv(t, v, c, n) else num_r(v),
                        stat_type, value, ci_or_se, n_e),
         r = ifelse(reversed == "yes", -r_raw, r_raw),   # higher = more of the named construct (codebook)
         later_wave = !(trimws(wave) %in% c("1", "")) & lagged != "yes",
         latent = stat_type == "latent", converted = stat_type %in% c("converted_or", "converted_d"),
         usable = !is.na(r) & abs(r) < 1 & !is.na(n_e) & n_e > 3)

bad <- effects |> filter(!usable)
write_csv(bad |> select(effect_id, sample_id, correlate_construct, stat_type, value, n), file.path(res_dir, "effects_not_usable.csv"))

main <- effects |>
  filter(usable, !later_wave, !(latent & observed_pair_exists == "yes")) |>
  mutate(yi = atanh(r), vi = 1 / (n_e - 3)) |>
  left_join(samples |> select(sample_id, journal, design2, region2, population2, ai2, age_mean_n, pct_female_n,
                              year_n, rob_1, rob_3, rob_6), by = "sample_id") |>
  mutate(adhoc = startsWith(exposure_family, "ADHOC_"))
# Effects with a later wave only (narrative synthesis)
write_csv(effects |> filter(later_wave) |> select(effect_id, sample_id, wave, correlate_construct, value),
          file.path(res_dir, "later_waves.csv"))

# ---------------------------------------------------------------------------------------------------------------
# CHE model with CR2 inference
# ---------------------------------------------------------------------------------------------------------------

na_row <- function(label, d, note) {
  tibble(analysis = label, k_studies = n_distinct(d$study_id), k_samples = n_distinct(d$sample_id), k_effects = nrow(d),
         n_total = sum(d |> distinct(sample_id, .keep_all = TRUE) |> pull(n_e)), r = NA_real_, ci.lb = NA_real_,
         ci.ub = NA_real_, pi.lb = NA_real_, pi.ub = NA_real_, df = NA_real_, p = NA_real_, tau2_sample = NA_real_,
         tau2_effect = NA_real_, I2_sample = NA_real_, I2_effect = NA_real_, note = note)
}

fit_che <- function(d, rho = RHO, mods = ~ 1) {
  d <- d |> arrange(sample_id) |> mutate(es_id = row_number())
  V <- vcalc(vi, cluster = sample_id, obs = es_id, rho = rho, data = d)
  m <- rma.mv(yi, V, mods = mods, random = ~ 1 | sample_id / es_id, data = d, method = "REML", sparse = TRUE,
              control = list(optimizer = "nlminb"))
  list(m = m, d = d)
}

pool_che <- function(d, label, rho = RHO) {
  if (n_distinct(d$sample_id) < MIN_K) return(na_row(label, d, sprintf("k < %d samples: not pooled", MIN_K)))
  f <- tryCatch(fit_che(d, rho), error = function(e) e)
  if (inherits(f, "error")) return(na_row(label, d, paste("model failed:", conditionMessage(f))))
  m <- f$m
  ct <- coef_test(m, vcov = "CR2", cluster = f$d$study_id)
  ci <- conf_int(m, vcov = "CR2", cluster = f$d$study_id)
  # prediction interval: CR2 standard error, both variance components, t with Satterthwaite df
  tot <- sum(m$sigma2)
  se <- ct$SE[1]
  q <- qt(0.975, df = max(ct$df_Satt[1], 1))
  W <- solve(m$V)   # typical sampling variance for the multilevel I2 (Cheung, 2014)
  X <- model.matrix(m)
  P <- W - W %*% X %*% solve(t(X) %*% W %*% X) %*% t(X) %*% W
  v_typ <- (m$k - m$p) / sum(diag(P))
  tibble(analysis = label, k_studies = n_distinct(f$d$study_id), k_samples = n_distinct(f$d$sample_id), k_effects = m$k,
         n_total = sum(f$d |> distinct(sample_id, .keep_all = TRUE) |> pull(n_e)),
         r = tanh(ct$beta[1]), ci.lb = tanh(ci$CI_L[1]), ci.ub = tanh(ci$CI_U[1]),
         pi.lb = tanh(ct$beta[1] - q * sqrt(se^2 + tot)), pi.ub = tanh(ct$beta[1] + q * sqrt(se^2 + tot)),
         df = ct$df_Satt[1], p = ct$p_Satt[1], tau2_sample = m$sigma2[1], tau2_effect = m$sigma2[2],
         I2_sample = 100 * m$sigma2[1] / (tot + v_typ), I2_effect = 100 * m$sigma2[2] / (tot + v_typ), note = "")
}

# One effect per sample: z averaged within sample with the same assumed correlation (metafor::aggregate)
one_per_sample <- function(d, rho = RHO) {
  es <- escalc(measure = "ZCOR", yi = d$yi, vi = d$vi, data = d)
  ag <- aggregate(es, cluster = sample_id, rho = rho, struct = "CS")
  ag
}

pool_re <- function(d, label) {
  if (n_distinct(d$sample_id) < MIN_K) return(na_row(label, d, sprintf("k < %d samples: not pooled", MIN_K)))
  ag <- one_per_sample(d)
  m <- rma(yi, vi, data = ag, method = "REML", test = "knha")
  pr <- predict(m, transf = tanh)   # not 'p': mutate() would read the column p of na_row()
  na_row(label, d, "one effect per sample (z averaged), REML + Hartung-Knapp") |>
    mutate(r = pr$pred, ci.lb = pr$ci.lb, ci.ub = pr$ci.ub, pi.lb = pr$pi.lb, pi.ub = pr$pi.ub, df = m$k - 1,
           p = m$pval, tau2_sample = m$tau2, I2_sample = m$I2)
}

# ---------------------------------------------------------------------------------------------------------------
# 1. Pooled correlations, every correlate with k >= 3 samples (primary always tabulated)
# ---------------------------------------------------------------------------------------------------------------

constructs <- sort(unique(main$correlate_construct))
pooled <- bind_rows(lapply(constructs, function(cn) {
  pool_che(main |> filter(correlate_construct == cn), cn) |>
    mutate(role = ifelse(cn %in% PRIMARY, "primary", "secondary"))
}))
for (cn in setdiff(PRIMARY, constructs)) pooled <- bind_rows(pooled, na_row(cn, main[0, ], "no effects") |> mutate(role = "primary"))
pooled <- pooled |> arrange(desc(role == "primary"), match(analysis, PRIMARY), desc(k_samples))
write_csv(pooled, file.path(res_dir, "pooled.csv"))

# ---------------------------------------------------------------------------------------------------------------
# 2. Primary moderator: type of dependence measure (T1-T3 contrast, HTZ Wald test); T4 apart
# ---------------------------------------------------------------------------------------------------------------

by_type <- list(); type_tests <- list()
for (cn in PRIMARY) {
  d <- main |> filter(correlate_construct == cn)
  for (t in c(TYPES, "T4")) {
    by_type[[paste(cn, t)]] <- pool_che(d |> filter(exposure_type == t), cn) |> mutate(type = t)
  }
  dt <- d |> filter(exposure_type %in% TYPES)
  present <- dt |> distinct(sample_id, exposure_type) |> count(exposure_type) |> filter(n >= MIN_K)
  if (n_distinct(d$sample_id) >= MIN_K_MOD && nrow(present) >= 2) {
    dt <- dt |> filter(exposure_type %in% present$exposure_type) |> mutate(type = factor(exposure_type))
    f <- tryCatch(fit_che(dt, mods = ~ 0 + type), error = function(e) NULL)
    if (!is.null(f)) {
      ff <- f$d
      wt <- Wald_test(f$m, constraints = constrain_equal(1:nlevels(ff$type)), vcov = "CR2", cluster = ff$study_id,
                      test = "HTZ")
      type_tests[[cn]] <- tibble(correlate = cn, types = paste(levels(ff$type), collapse = ", "),
                                 k_samples = n_distinct(ff$sample_id), F = wt$Fstat, df_num = wt$df_num,
                                 df_denom = wt$df_denom, p = wt$p_val)
    }
  } else {
    type_tests[[cn]] <- tibble(correlate = cn, types = paste(present$exposure_type, collapse = ", "),
                               k_samples = n_distinct(d$sample_id), F = NA, df_num = NA, df_denom = NA, p = NA)
  }
}
write_csv(bind_rows(by_type) |> relocate(type, .after = analysis), file.path(res_dir, "by_type.csv"))
write_csv(bind_rows(type_tests), file.path(res_dir, "type_tests.csv"))

# Post hoc (deviations.md, D6): the registered T1-T3 contrast has fewer than two types with k >= 3 for every primary
# correlate, because T2 and T3 scales are rarely paired with them. Here T4 enters the contrast, for every correlate
# with k >= 10 samples (primary and secondary), each type with k >= 3.
posthoc <- list()
for (cn in pooled$analysis[!is.na(pooled$k_samples) & pooled$k_samples >= MIN_K_MOD]) {
  d <- main |> filter(correlate_construct == cn, exposure_type %in% c(TYPES, "T4"))
  present <- d |> distinct(sample_id, exposure_type) |> count(exposure_type) |> filter(n >= MIN_K)
  if (nrow(present) < 2) next
  dt <- d |> filter(exposure_type %in% present$exposure_type) |> mutate(type = factor(exposure_type))
  f <- tryCatch(fit_che(dt, mods = ~ 0 + type), error = function(e) NULL)
  if (is.null(f)) next
  wt <- Wald_test(f$m, constraints = constrain_equal(1:nlevels(f$d$type)), vcov = "CR2", cluster = f$d$study_id,
                  test = "HTZ")
  ct <- coef_test(f$m, vcov = "CR2", cluster = f$d$study_id)
  posthoc[[cn]] <- tibble(correlate = cn, role = ifelse(cn %in% PRIMARY, "primary", "secondary"),
                          types = paste(levels(f$d$type), collapse = ", "),
                          k_by_type = paste(present$exposure_type, present$n, sep = "=", collapse = ", "),
                          r_by_type = paste(sprintf("%s %.2f", levels(f$d$type), tanh(ct$beta)), collapse = "; "),
                          F = wt$Fstat, df_num = wt$df_num, df_denom = wt$df_denom, p = wt$p_val)
}
write_csv(bind_rows(posthoc), file.path(res_dir, "posthoc_type_tests.csv"))

# ---------------------------------------------------------------------------------------------------------------
# 3. Other moderators (one at a time, k >= 10 samples), primary correlates
# ---------------------------------------------------------------------------------------------------------------

MODS <- list(population = "population2", region = "region2", ai_type = "ai2", age = "age_mean_n",
             pct_female = "pct_female_n", design = "design2", peer_reviewed = "journal", year = "year_n",
             rob_1 = "rob_1", rob_3 = "rob_3", rob_6 = "rob_6", latent = "latent", converted = "converted",
             lagged = "lagged")
mod_rows <- list(); mod_levels <- list()
for (cn in PRIMARY) {
  d0 <- main |> filter(correlate_construct == cn)
  for (nm in names(MODS)) {
    v <- MODS[[nm]]
    d <- d0[!is.na(d0[[v]]) & d0[[v]] != "" & d0[[v]] != "NR", ]
    k <- n_distinct(d$sample_id)
    if (k < MIN_K_MOD) {
      mod_rows[[paste(cn, nm)]] <- tibble(correlate = cn, moderator = nm, k_samples = k, F = NA, df_num = NA,
                                          df_denom = NA, p = NA, note = "k < 10")
      next
    }
    d$x <- d[[v]]
    if (!is.numeric(d$x)) {
      lv <- d |> distinct(sample_id, x) |> count(x) |> filter(n >= 2)
      d <- d |> filter(x %in% lv$x)
      if (n_distinct(d$x) < 2) {
        mod_rows[[paste(cn, nm)]] <- tibble(correlate = cn, moderator = nm, k_samples = k, F = NA, df_num = NA,
                                            df_denom = NA, p = NA, note = "fewer than two levels with 2+ samples")
        next
      }
      d$x <- factor(d$x)
    }
    f <- tryCatch(fit_che(d, mods = ~ x), error = function(e) NULL)
    if (is.null(f)) next
    idx <- 2:f$m$p
    wt <- Wald_test(f$m, constraints = constrain_zero(idx), vcov = "CR2", cluster = f$d$study_id, test = "HTZ")
    mod_rows[[paste(cn, nm)]] <- tibble(correlate = cn, moderator = nm, k_samples = n_distinct(f$d$sample_id),
                                        F = wt$Fstat, df_num = wt$df_num, df_denom = wt$df_denom, p = wt$p_val,
                                        note = if (is.numeric(d[[v]])) sprintf("slope (z per unit) %.4f", f$m$beta[2]) else
                                          paste(levels(d$x), collapse = " / "))
    if (!is.numeric(d[[v]])) {   # pooled r in each level of a categorical moderator, for the text
      for (lvl in levels(d$x)) {
        mod_levels[[paste(cn, nm, lvl)]] <- pool_che(d |> filter(x == lvl), lvl) |>
          mutate(correlate = cn, moderator = nm, .before = 1)
      }
    }
  }
}
write_csv(bind_rows(mod_rows), file.path(res_dir, "moderators.csv"))
write_csv(bind_rows(mod_levels), file.path(res_dir, "moderator_levels.csv"))

# ---------------------------------------------------------------------------------------------------------------
# 4. Sensitivity analyses (section 15c; 9 added in D4)
# ---------------------------------------------------------------------------------------------------------------

alpha_n <- function(x) { a <- num_r(x); ifelse(!is.na(a) & a > 1, a / 100, a) }
main <- main |> mutate(ax = alpha_n(exposure_alpha), ay = alpha_n(correlate_alpha)) |>
  group_by(exposure_family, exposure_part) |> mutate(ax = coalesce(ax, mean(ax, na.rm = TRUE))) |> ungroup() |>
  group_by(ci = tolower(correlate_instrument)) |> mutate(ay = coalesce(ay, mean(ay, na.rm = TRUE))) |> ungroup() |>
  select(-ci)

sens <- list()
for (cn in PRIMARY) {
  d <- main |> filter(correlate_construct == cn)
  rob3 <- d |> filter(rob_3 != "no", !adhoc)
  sens[[cn]] <- bind_rows(
    pool_che(d, "main") ,
    pool_che(rob3, "1 without single-item and ad hoc measures"),
    pool_che(d |> filter(!converted), "2 without converted statistics"),
    pool_che(d |> filter(!latent), "3 without latent correlations"),
    pool_che(d |> filter(journal), "4 peer-reviewed reports only"),
    pool_che(d, "5a within-sample correlation 0.3", rho = 0.3),
    pool_che(d, "5b within-sample correlation 0.8", rho = 0.8),
    pool_re(d, "6 one effect per sample, random effects"),
    {
      dc <- d |> filter(!is.na(ax), !is.na(ay), ax > 0, ay > 0) |>
        mutate(rc = pmax(pmin(r / sqrt(ax * ay), 0.999), -0.999), yi = atanh(rc), vi = vi / (ax * ay))
      pool_che(dc, "7 corrected for unreliability (Hunter-Schmidt)")
    },
    pool_che(d |> filter(lagged != "yes"), "9 without time-lagged correlations (D4)")
  ) |> mutate(correlate = cn, .before = 1)
}
write_csv(bind_rows(sens), file.path(res_dir, "sensitivity.csv"))

# 8. Leave one study out
loo <- list()
for (cn in PRIMARY) {
  d <- main |> filter(correlate_construct == cn)
  if (n_distinct(d$sample_id) < MIN_K + 1) next
  for (st in unique(d$study_id)) {
    loo[[paste(cn, st)]] <- pool_che(d |> filter(study_id != st), paste("without", st)) |> mutate(correlate = cn, .before = 1)
  }
}
write_csv(bind_rows(loo), file.path(res_dir, "leave_one_study_out.csv"))

# ---------------------------------------------------------------------------------------------------------------
# 5. Meta-biases (section 16)
# ---------------------------------------------------------------------------------------------------------------

bias <- list()
for (cn in PRIMARY) {
  d <- main |> filter(correlate_construct == cn)
  if (n_distinct(d$sample_id) < MIN_K_MOD) {
    bias[[cn]] <- tibble(correlate = cn, k_samples = n_distinct(d$sample_id), note = "k < 10: tests not run")
    next
  }
  d <- d |> mutate(sei = sqrt(vi))
  f <- fit_che(d, mods = ~ sei)
  eg <- coef_test(f$m, vcov = "CR2", cluster = f$d$study_id)
  ag <- one_per_sample(d)
  ag$sei <- sqrt(ag$vi)
  pet <- rma(yi, vi, mods = ~ sei, data = ag, method = "REML", test = "knha")
  peese <- rma(yi, vi, mods = ~ vi, data = ag, method = "REML", test = "knha")
  use_peese <- pet$pval[1] < 0.05   # Stanley & Doucouliagos (2014): PEESE when the PET intercept differs from 0
  sel <- tryCatch(weightfunct(effect = ag$yi, v = ag$vi, steps = c(0.025, 1)), error = function(e) NULL)
  sel_r <- sel_p <- NA_real_
  if (!is.null(sel)) {
    adj <- sel[[2]]
    sel_r <- tanh(adj$par[2])
    lr <- 2 * abs(sel[[2]]$value - sel[[1]]$value)
    sel_p <- pchisq(lr, df = 1, lower.tail = FALSE)
  }
  bias[[cn]] <- tibble(correlate = cn, k_samples = n_distinct(d$sample_id), egger_slope = eg$beta[2], egger_p = eg$p_Satt[2],
                       pet_r = tanh(pet$beta[1]), pet_p = pet$pval[1], peese_r = tanh(peese$beta[1]),
                       pet_peese_r = tanh(if (use_peese) peese$beta[1] else pet$beta[1]),
                       selection_r = sel_r, selection_lrt_p = sel_p, note = "")
  png(file.path(fig_dir, sprintf("funnel_%s.png", cn)), width = 1600, height = 1400, res = 250)
  metafor::funnel(rma(yi, vi, data = ag, method = "REML"), xlab = "Fisher z", main = cn)   # weightr masks funnel()
  dev.off()
}
write_csv(bind_rows(bias), file.path(res_dir, "publication_bias.csv"))

# ---------------------------------------------------------------------------------------------------------------
# 6. GRADE inputs (section 17) and the evidence map
# ---------------------------------------------------------------------------------------------------------------

grade <- list()
for (cn in PRIMARY) {
  d <- main |> filter(correlate_construct == cn)
  p <- pooled |> filter(analysis == cn)
  if (is.na(p$r)) { grade[[cn]] <- tibble(correlate = cn, note = "not pooled"); next }
  w <- d |> group_by(sample_id) |> summarise(w = sum(1 / vi), rob = any(c(first(rob_1), first(rob_3), first(rob_6)) == "no"),
                                             student = first(population2) == "university_students",
                                             region = first(region2), .groups = "drop")
  grade[[cn]] <- tibble(correlate = cn, k_samples = p$k_samples, r = p$r, ci.lb = p$ci.lb, ci.ub = p$ci.ub,
                        pi.lb = p$pi.lb, pi.ub = p$pi.ub,
                        weight_share_rob_no = sum(w$w[w$rob %in% TRUE]) / sum(w$w),
                        pi_crosses_zero = p$pi.lb < 0 & p$pi.ub > 0,
                        ci_spans_small_and_moderate = p$ci.lb < 0.10 & p$ci.ub > 0.30,
                        share_students = mean(w$student, na.rm = TRUE), n_regions = n_distinct(na.omit(w$region)),
                        note = "")
}
write_csv(bind_rows(grade), file.path(res_dir, "grade_inputs.csv"))

evidence_map <- effects |> filter(usable) |> distinct(sample_id, exposure_family, exposure_type, correlate_construct) |>
  count(exposure_type, exposure_family, correlate_construct, name = "samples") |> arrange(exposure_type, desc(samples))
write_csv(evidence_map, file.path(res_dir, "evidence_map.csv"))

# Forest plots of the primary correlates: one row per sample (z averaged within sample), CHE pooled value below
for (cn in PRIMARY) {
  d <- main |> filter(correlate_construct == cn)
  if (n_distinct(d$sample_id) < MIN_K) next
  ag <- one_per_sample(d)
  lab <- samples |> select(sample_id, first_author, year) |> mutate(lab = paste(first_author, year, sample_id))
  ag$lab <- lab$lab[match(ag$sample_id, lab$sample_id)]
  ag$type <- d |> group_by(sample_id) |> summarise(t = paste(sort(unique(exposure_type)), collapse = "/")) |>
    (\(x) x$t[match(ag$sample_id, x$sample_id)])()
  ag <- ag[order(ag$type, ag$yi), ]
  p <- pooled |> filter(analysis == cn)
  h <- 0.18 * nrow(ag) + 2
  png(file.path(fig_dir, sprintf("forest_%s.png", cn)), width = 2000, height = max(1000, h * 250), res = 250)
  forest(ag$yi, ag$vi, slab = paste(ag$lab, ag$type), transf = tanh, xlab = "r", header = c(cn, "r [95% CI]"),
         ylim = c(-2, nrow(ag) + 3), cex = 0.6)
  addpoly(x = atanh(p$r), ci.lb = atanh(p$ci.lb), ci.ub = atanh(p$ci.ub), row = -1, transf = tanh,
          mlab = "CHE, CR2", cex = 0.6)
  dev.off()
}

writeLines(capture.output(sessionInfo()), file.path(out_root, "sessionInfo.txt"))
cat(sprintf("effects %d (usable %d, main %d), samples %d -> %s\n", nrow(effects), sum(effects$usable), nrow(main),
            n_distinct(main$sample_id), res_dir))
print(pooled |> select(analysis, k_samples, k_effects, r, ci.lb, ci.ub, pi.lb, pi.ub, note), n = 40, width = 200)
