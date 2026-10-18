# PRISMA 2020 flow diagram (databases and search engines; citation searching of the included studies, deviations.md D2).
#
# Reads fulltext/prisma_counts.json (fulltext/ft_summary.py) and forms/samples.csv, forms/effects.csv (verified
# extraction); writes analysis/figures/prisma.png, prisma.pdf and prisma.tiff.
# Template: papers/misophonia-prevalence/analysis/prisma.R.
# Run from the repository root: Rscript papers/ai-dependence-correlates/analysis/prisma.R

suppressPackageStartupMessages({
  library(ggplot2)
  library(jsonlite)
})

paper <- "papers/ai-dependence-correlates"
pc <- fromJSON(file.path(paper, "fulltext", "prisma_counts.json"))
fig_dir <- file.path(paper, "analysis", "figures")
dir.create(fig_dir, showWarnings = FALSE, recursive = TRUE)
fmt <- function(x) prettyNum(x, big.mark = ",")

src_names <- c(pubmed = "PubMed", europepmc = "Europe PMC", openalex = "OpenAlex", openalex_non_en = "OpenAlex, other languages",
               s2 = "Semantic Scholar", crossref = "Crossref", citations = "Citations of instrument papers (OpenAlex)",
               datacite = "DataCite", openaire = "OpenAIRE", core = "CORE")
by_src <- pc$records_per_source
src_txt <- paste(sprintf("%s (n = %s)", src_names[names(by_src)], fmt(unlist(by_src))), collapse = "\n")
excl_names <- c(no_eligible_correlate = "No eligible correlate", E5_design = "Design (review, qualitative, other)",
                E1_no_dependence_measure = "No measure of AI dependence", E4_no_zero_order = "No zero-order association",
                E3_out_of_scope = "Out of scope", other = "Other")
excl <- unlist(pc$reports_excluded_full_text)
excl <- excl[order(-excl)]
excl_txt <- paste(sprintf("%s (n = %s)", excl_names[names(excl)], fmt(excl)), collapse = "\n")

s <- read.csv(file.path(paper, "forms", "samples.csv"), colClasses = "character")
e <- read.csv(file.path(paper, "forms", "effects.csv"), colClasses = "character")
in_ma <- unique(e$sample_id)
studies_txt <- sprintf(paste0("Studies included in review (n = %d)\nIndependent samples (n = %d)\n",
                              "Reports of included studies (n = %d)\n\nSamples with at least one\nzero-order correlation (n = %d)"),
                       length(unique(s$study_id)), nrow(s), pc$reports_included, length(in_ma))
nr <- pc$reports_not_retrieved_detail

boxes <- data.frame(
  x = c(1, 3, 1, 3, 1, 3, 1, 3, 1),
  y = c(9, 9, 7, 7, 5, 5, 3, 3, 1),
  w = 1.8,
  h = c(2.0, 1.1, 0.7, 0.7, 0.7, 0.9, 0.7, 1.4, 1.2),
  label = c(
    paste0("Records identified (n = ", fmt(pc$records_identified), "):\n", src_txt),
    paste0("Records removed before screening:\nDuplicate records (n = ", fmt(pc$duplicates_removed),
           ")\nRemoved by automation tools\n(non-study records, n = ", fmt(pc$removed_by_automation), ")"),
    paste0("Records screened\n(n = ", fmt(pc$records_screened_title_abstract), ")"),
    paste0("Records excluded\n(n = ", fmt(pc$records_excluded_title_abstract), ")"),
    paste0("Reports sought for retrieval\n(n = ", fmt(pc$reports_sought_for_retrieval), ")"),
    paste0("Reports not retrieved (n = ", fmt(pc$reports_not_retrieved), "):\nno open-access full text (n = ",
           fmt(nr$no_open_access_copy_or_blocked), ")\nfile did not contain the report (n = ",
           fmt(nr$retrieved_file_did_not_contain_the_report), ")"),
    paste0("Reports assessed for eligibility\n(n = ", fmt(pc$reports_assessed_for_eligibility), ")"),
    paste0("Reports excluded (n = ", fmt(sum(excl)), "):\n", excl_txt),
    studies_txt),
  stringsAsFactors = FALSE)
arrows <- data.frame(
  x = c(1, 1.9, 1, 1.9, 1, 1.9, 1, 1.9), y = c(9 - 1.0, 9, 7 - 0.35, 7, 5 - 0.35, 5, 3 - 0.35, 3),
  xend = c(1, 2.1, 1, 2.1, 1, 2.1, 1, 2.1), yend = c(7 + 0.35, 9, 5 + 0.35, 7, 3 + 0.35, 5, 1 + 0.6, 3))

ch <- pc$other_methods_citation_searching
cex <- unlist(ch$reports_excluded)
cex <- cex[order(-cex)]
other <- data.frame(
  x = c(5, 7, 5, 7, 5, 7), y = c(9, 7, 5, 5, 3, 3), w = 1.8, h = c(1.1, 1.1, 0.7, 0.7, 0.7, 1.1),
  label = c(
    paste0("Records identified from citation\nsearching of included studies and\nreviews (not in the database set;\nn = ",
           fmt(ch$new_works_not_in_main_set), ")"),
    paste0("Records not sought: no AI term\nnear a dependence term in title\nor abstract (n = ",
           fmt(ch$without_exposure_concept_in_title_abstract), ")"),
    paste0("Reports sought for retrieval\n(n = ", fmt(ch$reports_sought), ")"),
    paste0("Reports not retrieved\n(no open-access full text; n = ", fmt(ch$reports_not_retrieved), ")"),
    paste0("Reports assessed for eligibility\n(n = ", fmt(ch$reports_assessed), ")"),
    paste0("Reports excluded (n = ", fmt(sum(cex)), "):\n",
           paste(sprintf("%s (n = %s)", excl_names[names(cex)], fmt(cex)), collapse = "\n"),
           "\nReports included (n = ", ch$reports_included, ")")),
  stringsAsFactors = FALSE)
boxes <- rbind(boxes, other)
arrows <- rbind(arrows, data.frame(
  x = c(5, 5, 5, 5.9, 5, 5.9), y = c(9 - 0.55, 7, 5 - 0.35, 5, 3, 3),
  xend = c(5, 6.1, 5, 6.1, 5, 6.1), yend = c(5 + 0.35, 7, 3 + 0.35, 5, 3, 3)))
arrows <- arrows[!(arrows$x == 5 & arrows$y == 3 & arrows$xend == 5), ]

p <- ggplot() +
  geom_rect(data = boxes, aes(xmin = x - w / 2, xmax = x + w / 2, ymin = y - h / 2, ymax = y + h / 2),
            fill = "white", colour = "black", linewidth = 0.3) +
  geom_text(data = boxes, aes(x = x, y = y, label = label), size = 2.2, lineheight = 0.95) +
  geom_segment(data = arrows, aes(x = x, y = y, xend = xend, yend = yend),
               arrow = arrow(length = unit(0.12, "cm"), type = "closed"), linewidth = 0.3) +
  annotate("text", x = -0.25, y = c(9, 6, 1), label = c("Identification", "Screening", "Included"),
           angle = 90, size = 2.8, fontface = "bold") +
  annotate("text", x = c(2, 6), y = 10.4,
           label = c("Databases, search engines and instrument citations", "Citation searching"),
           size = 2.8, fontface = "bold") +
  coord_cartesian(xlim = c(-0.4, 8), ylim = c(0.2, 10.6)) +
  theme_void()
ggsave(file.path(fig_dir, "prisma.png"), p, width = 12, height = 8.3, dpi = 300, bg = "white")
ggsave(file.path(fig_dir, "prisma.pdf"), p, width = 12, height = 8.3)
ggsave(file.path(fig_dir, "prisma.tiff"), p, width = 12, height = 8.3, dpi = 1000, bg = "white", compression = "lzw")   # line art (Elsevier: 1000 dpi)
cat("PRISMA flow diagram ->", fig_dir, "\n")
