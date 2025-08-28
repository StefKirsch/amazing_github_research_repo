#' Clean the dataset
#' 1) remove rows with any missing values
#' 2) keep participants with 18 <= age <= 70
clean_data <- function(df) {
  df |>
    tidyr::drop_na() |>
    dplyr::filter(age >= 18, age <= 70)
}