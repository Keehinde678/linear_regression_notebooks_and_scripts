#!/usr/bin/env Rscript
# Sample regression data
regression_data <- data.frame(
  YearsExperience = c(1.1, 2.0, 3.2, 4.5, 5.0, 6.1, 7.4, 8.0, 9.5, 10.3),
  Salary = c(39343, 46205, 54445, 61111, 66029, 81363, 93940, 101302, 112635, 122391)
)

# Save to CSV in current directory
write.csv(regression_data, "regression_data.csv", row.names = FALSE)

cat("CSV file 'regression_data.csv' created!\n")
# Load the dataset
data <- read.csv("regression_data.csv", stringsAsFactors = FALSE)

# View the first few rows
head(data)
plot(data$YearsExperience, data$Salary,
     main = "Salary vs Years of Experience",
     xlab = "Years of Experience",
     ylab = "Salary",
     col = "blue", pch = 19)
# Fit a linear regression model
model <- lm(Salary ~ YearsExperience, data = data)

# Print model summary
summary(model)
# Scatter plot
plot(data$YearsExperience, data$Salary,
     main = "Salary vs Years of Experience",
     xlab = "Years of Experience",
     ylab = "Salary",
     col = "blue", pch = 19)

# Add regression line
abline(model, col = "red", lwd = 2)
# Save the scatterplot with regression line as PNG
png("salary_vs_experience_plot.png", width = 800, height = 600)

# Create scatterplot
plot(data$YearsExperience, data$Salary,
     main = "Salary vs Years of Experience",
     xlab = "Years of Experience",
     ylab = "Salary",
     col = "blue", pch = 19)

# Add regression line
abline(model, col = "red", lwd = 2)

# Finish writing to file
dev.off()

cat("Plot saved as 'salary_vs_experience_plot.png'\n")
