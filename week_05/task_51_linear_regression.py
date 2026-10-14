# Task 51: Implement Linear Regression with scikit-learn
# Uses datasets bundled with scikit-learn, so no download is needed.

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

out = Path(__file__).parent

# ---------- Part 1: simple (one feature) linear regression ----------
rng = np.random.default_rng(0)
hours = rng.uniform(1, 10, 80).reshape(-1, 1)                 # hours studied
score = 35 + 6 * hours.ravel() + rng.normal(0, 4, 80)         # exam score with noise

X_train, X_test, y_train, y_test = train_test_split(hours, score, test_size=0.2, random_state=42)
model = LinearRegression().fit(X_train, y_train)
pred = model.predict(X_test)

print("PART 1: score vs hours studied")
print("  intercept:", round(model.intercept_, 2), "(true value 35)")
print("  slope    :", round(model.coef_[0], 2), "(true value 6)")
print("  R2       :", round(r2_score(y_test, pred), 3))
print("  predicted score for 7.5 hours:", round(model.predict([[7.5]])[0], 1))

plt.scatter(X_test, y_test, label="actual")
line_x = np.linspace(1, 10, 50).reshape(-1, 1)
plt.plot(line_x, model.predict(line_x), color="red", label="fitted line")
plt.xlabel("Hours studied"); plt.ylabel("Exam score"); plt.legend()
plt.title("Simple linear regression")
plt.savefig(out / "task_51_simple_regression.png", dpi=120)
plt.close()

# ---------- Part 2: multiple linear regression on a real data set ----------
data = load_diabetes(as_frame=True)
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression().fit(X_train, y_train)
pred = model.predict(X_test)

print("\nPART 2: diabetes progression data (442 patients, 10 features)")
print("  MAE :", round(mean_absolute_error(y_test, pred), 2))
print("  MSE :", round(mean_squared_error(y_test, pred), 2))
print("  RMSE:", round(mean_squared_error(y_test, pred) ** 0.5, 2))
print("  R2  :", round(r2_score(y_test, pred), 3))

coefs = pd.Series(model.coef_, index=X.columns).sort_values()
print("\n  Coefficients:")
print(coefs.round(1).to_string())

# Compare a few predictions to the real values
comparison = pd.DataFrame({"actual": y_test.values[:8], "predicted": pred[:8].round(1)})
print("\n", comparison)

plt.scatter(y_test, pred)
lims = [y.min(), y.max()]
plt.plot(lims, lims, "r--")
plt.xlabel("Actual"); plt.ylabel("Predicted"); plt.title("Actual vs predicted")
plt.savefig(out / "task_51_actual_vs_predicted.png", dpi=120)
plt.close()
print("\nSaved two plots next to this script.")
