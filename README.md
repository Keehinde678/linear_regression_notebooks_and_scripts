# linear_regression_notebooks_and_scripts

## Dataset

- **`regression_data.csv`** contains the dataset used for analysis.  
- It should include numerical columns suitable for regression, such as a predictor (`x`) and an outcome (`y`).  
- Example columns: `YearsExperience` (predictor), `Salary` (outcome).

## Part I: Jupyter Notebooks

### Objectives

- Load data from CSV.
- Visualize relationships with scatter plots.
- Fit simple linear regression models.
- Overlay regression lines on plots.
- Evaluate model fit using statistical metrics.
- Export notebooks as `.ipynb` and `.html` for sharing.

### Details

Both notebooks (Python and R) are structured to:

1. **Load the dataset** — Users can specify which CSV file and columns to use.
2. **Plot the data** — Scatter plots show raw data points.
3. **Fit a linear regression model** — Using `scikit-learn` in Python, and `lm()` in R.
4. **Display regression line** — Overlayed on scatter plot for visual clarity.
5. **Model evaluation** — Calculate and display R² and Root Mean Squared Error (RMSE).
6. **Export output** — Save plots inline and export notebook to `.html` format.

### How to Run

- Install Jupyter Notebook or JupyterLab.
- Open the notebooks under `/notebooks/`.
- Update the file path and column names as needed.
- Run all cells to generate outputs and analyses.

## Part II: Standalone Command-Line Scripts

### Purpose

Scripts allow automation and easy repetition of regression analysis without opening notebooks. They accept user inputs via command-line arguments and save output plots.

### Features

- Accepts arguments: `<filename> <x_column> <y_column>`.
- Loads the specified dataset.
- Creates scatter plot with regression line.
- Saves plot image to `/outputs/`.
- Prints evaluation metrics (R², RMSE) to console.

## NB:
Python and R Notebooks are in /notebooks/

Outputs (PNG plots) are in /outputs/

### Example Usage

```bash
# Python script
python scripts/linear_regression_python.py data/regression_data.csv YearsExperience Salary

# R script
Rscript scripts/linear_regression_r.R data/regression_data.csv YearsExperience Salary
