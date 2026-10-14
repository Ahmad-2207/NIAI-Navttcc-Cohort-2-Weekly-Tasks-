# Task 52: Perform Logistic Regression
# Part 1: binary classification (breast cancer data)
# Part 2: multiclass classification of handwritten digits (MNIST style, 8x8 pixels)
# Both data sets ship with scikit-learn, so no download is needed.

from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer, load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

out = Path(__file__).parent

# ---------- Part 1: binary ----------
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.2, random_state=42, stratify=cancer.target)

binary_model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
binary_model.fit(X_train, y_train)
pred = binary_model.predict(X_test)

print("PART 1: binary classification (malignant vs benign)")
print("  accuracy:", round(accuracy_score(y_test, pred), 3))
print("  confusion matrix [[TN FP] [FN TP]]:\n", confusion_matrix(y_test, pred))
print(classification_report(y_test, pred, target_names=cancer.target_names))

# Probabilities for the first 3 test patients
proba = binary_model.predict_proba(X_test[:3])
for p, label in zip(proba, pred[:3]):
    print(f"  P(malignant)={p[0]:.3f}  P(benign)={p[1]:.3f}  -> {cancer.target_names[label]}")

# ---------- Part 2: multiclass ----------
digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.25, random_state=0, stratify=digits.target)

multi_model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
multi_model.fit(X_train, y_train)
pred = multi_model.predict(X_test)

print("\nPART 2: multiclass classification (digits 0 to 9)")
print("  train accuracy:", round(multi_model.score(X_train, y_train), 3))
print("  test accuracy :", round(accuracy_score(y_test, pred), 3))
print(classification_report(y_test, pred))

ConfusionMatrixDisplay.from_predictions(y_test, pred, cmap="Blues")
plt.title("Digits: confusion matrix")
plt.savefig(out / "task_52_digits_confusion_matrix.png", dpi=120)
plt.close()

# Show a few predictions as images
fig, axes = plt.subplots(2, 5, figsize=(9, 4))
for ax, image, true, guess in zip(axes.ravel(), X_test[:10], y_test[:10], pred[:10]):
    ax.imshow(image.reshape(8, 8), cmap="gray_r")
    ax.set_title(f"true {true} / pred {guess}", fontsize=9)
    ax.axis("off")
plt.tight_layout()
plt.savefig(out / "task_52_digit_predictions.png", dpi=120)
plt.close()
print("Saved two plots next to this script.")
