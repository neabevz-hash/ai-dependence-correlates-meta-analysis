# Manuscript figures from the analysis results (analysis.R must run first).
#
# Figure 2 - pooled correlations of AI dependence with every correlate pooled (k >= 3 samples): r, 95% CI and 95%
#            prediction interval (CHE, CR2), primary correlates first.
# Figure 3 - evidence map: number of independent samples per correlate and type of dependence scale (T1-T4, R1's
#            types, extraction/instruments.csv); a sample counts once per cell.
# Writes analysis/figures/fig2_pooled.{png,pdf,tiff} and fig3_evidence_map.{png,pdf,tiff}.
# Run from the repository root: Rscript papers/ai-dependence-correlates/analysis/figures.R

suppressPackageStartupMessages({
  library(ggplot2)
  library(dplyr)
  library(readr)
})

paper <- "papers/ai-dependence-correlates"
res <- file.path(paper, "analysis", "results")
fig_dir <- file.path(paper, "analysis", "figures")
PRIMARY <- c("depression", "anxiety", "stress", "loneliness", "social_anxiety", "self_esteem", "procrastination")
LABEL <- c(depression = "Depression", anxiety = "Anxiety", stress = "Stress", loneliness = "Loneliness",
           social_anxiety = "Social anxiety", self_esteem = "Self-esteem", procrastination = "Procrastination",
           self_efficacy = "Self-efficacy", academic_stress = "Academic stress", ai_anxiety = "AI anxiety",
           self_control = "Self-control", extraversion = "Extraversion", conscientiousness = "Conscientiousness",
           neuroticism = "Neuroticism", openness = "Openness", agreeableness = "Agreeableness",
           social_support = "Social support", distress = "Psychological distress", escapism_motive = "Escapism motive",
           wellbeing = "Well-being", problematic_internet_use = "Problematic internet use",
           sleep_quality = "Sleep quality", attachment_anxiety = "Attachment anxiety", fomo = "Fear of missing out",
           impulsivity = "Impulsivity", problematic_social_media_use = "Problematic social media use",
           problematic_smartphone_use = "Problematic smartphone use", attachment_avoidance = "Attachment avoidance",
           boredom = "Boredom proneness", mindfulness = "Mindfulness")
lab <- function(x) ifelse(x %in% names(LABEL), LABEL[x], x)
save3 <- function(p, name, w, h) {
  ggsave(file.path(fig_dir, paste0(name, ".png")), p, width = w, height = h, dpi = 300, bg = "white")
  ggsave(file.path(fig_dir, paste0(name, ".pdf")), p, width = w, height = h)
  ggsave(file.path(fig_dir, paste0(name, ".tiff")), p, width = w, height = h, dpi = 1000, bg = "white",
         compression = "lzw")
}

# Figure 2 ---------------------------------------------------------------------------------------------------------
pooled <- read_csv(file.path(res, "pooled.csv"), show_col_types = FALSE) |>
  filter(!is.na(r)) |>
  mutate(group = ifelse(analysis %in% PRIMARY, "Primary correlates", "Secondary correlates"),
         group = factor(group, levels = c("Primary correlates", "Secondary correlates")),
         name = sprintf("%s (k = %d)", lab(analysis), k_samples),
         ord = ifelse(analysis %in% PRIMARY, match(analysis, PRIMARY), 100 - r))
pooled$name <- factor(pooled$name, levels = rev(pooled$name[order(pooled$group, pooled$ord)]))
p2 <- ggplot(pooled, aes(y = name)) +
  geom_vline(xintercept = 0, linewidth = 0.3, colour = "grey50") +
  geom_errorbarh(aes(xmin = pi.lb, xmax = pi.ub), height = 0, linewidth = 0.3, colour = "grey60") +
  geom_errorbarh(aes(xmin = ci.lb, xmax = ci.ub), height = 0.25, linewidth = 0.5) +
  geom_point(aes(x = r), shape = 15, size = 1.8) +
  geom_text(aes(x = 1.02, label = sprintf("%.2f [%.2f, %.2f]", r, ci.lb, ci.ub)), hjust = 0, size = 2.4) +
  facet_grid(group ~ ., scales = "free_y", space = "free_y") +
  scale_x_continuous(limits = c(-1, 1.45), breaks = seq(-1, 1, 0.5)) +
  labs(x = "Correlation with AI dependence, r (95% CI; grey: 95% prediction interval)", y = NULL) +
  theme_bw(base_size = 8) +
  theme(panel.grid.minor = element_blank(), panel.grid.major.y = element_blank(),
        strip.background = element_rect(fill = "grey95"))
save3(p2, "fig2_pooled", 6.5, 6)

# Figure 3 ---------------------------------------------------------------------------------------------------------
eff <- read_csv(file.path(paper, "forms", "effects.csv"), col_types = cols(.default = "c"))
map <- eff |> distinct(sample_id, exposure_type, correlate_construct) |>
  count(correlate_construct, exposure_type, name = "samples")
tot <- eff |> distinct(sample_id, correlate_construct) |> count(correlate_construct, name = "all")
keep <- tot |> filter(all >= 3 | correlate_construct %in% PRIMARY)
map <- tidyr::complete(map |> filter(correlate_construct %in% keep$correlate_construct),
                       correlate_construct, exposure_type = c("T1", "T2", "T3", "T4"), fill = list(samples = 0L))
ord <- c(PRIMARY, setdiff(keep$correlate_construct[order(-keep$all)], PRIMARY))
map <- map |> mutate(row = factor(sprintf("%s (%d)", lab(correlate_construct), tot$all[match(correlate_construct, tot$correlate_construct)]),
                                  levels = rev(sprintf("%s (%d)", lab(ord), tot$all[match(ord, tot$correlate_construct)]))),
                     col = factor(exposure_type, levels = c("T1", "T2", "T3", "T4"),
                                  labels = c("T1\naddiction-type", "T2\nfunctional", "T3\nemotional", "T4\nmixed or unclear")),
                     primary = correlate_construct %in% PRIMARY)
p3 <- ggplot(map, aes(x = col, y = row, fill = samples)) +
  geom_tile(colour = "white", linewidth = 0.6) +
  geom_text(aes(label = samples, colour = samples > 10), size = 2.6) +
  scale_fill_gradient(low = "grey97", high = "grey20", name = "Samples") +
  scale_colour_manual(values = c(`FALSE` = "black", `TRUE` = "white"), guide = "none") +
  geom_hline(yintercept = length(ord) - length(PRIMARY) + 0.5, linewidth = 0.4) +
  labs(x = "Type of AI-dependence scale", y = "Correlate (samples with any scale)") +
  theme_minimal(base_size = 8) + theme(panel.grid = element_blank())
save3(p3, "fig3_evidence_map", 5.2, 6)
cat("figures ->", fig_dir, "\n")
