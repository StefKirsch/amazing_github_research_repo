library(readr)
library(dplyr)
library(ggplot2)
library(tidyr)
library(purrr)

# Source the cleaning function (expects to be run from project root)
source("R/src/data_utils.R")

# Load & clean data
df <- readr::read_csv("data/survey_data.csv", show_col_types = FALSE)
df_clean <- clean_data(df)

# Correlations: mental_health vs selected variables
cols <- c("job_satisfaction", "stress_at_job", "salary", "years_experience")
present <- intersect(cols, names(df_clean))

corrs <- tibble(variable = present) |>
  mutate(
    correlation_with_mental_health = map_dbl(
      variable,
      ~ suppressWarnings(
        stats::cor(df_clean$mental_health, df_clean[[.x]],
                   use = "complete.obs", method = "pearson")
      )
    )
  )

dir.create("R/outputs", showWarnings = FALSE, recursive = TRUE)
readr::write_csv(corrs, "R/outputs/mental_health_correlations.csv")

# Plot: mean mental_health by education with side-by-side bars per gender
summary_df <- df_clean |>
  group_by(education, gender) |>
  summarise(mean_mental_health = mean(mental_health, na.rm = TRUE), .groups = "drop")

p <- ggplot(summary_df, aes(x = education, y = mean_mental_health, fill = gender)) +
  geom_col(position = position_dodge(width = 0.8)) +
  labs(x = "Education", y = "Mean mental health",
       title = "Mental health by education and gender") +
  theme_minimal(base_size = 12)

ggsave("R/outputs/mental_health_by_education_gender.png", p, width = 8, height = 5, dpi = 150)

message("Saved: R/outputs/mental_health_correlations.csv")
message("Saved: R/outputs/mental_health_by_education_gender.png")
