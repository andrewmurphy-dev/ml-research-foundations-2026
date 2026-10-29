# ML Coding Plan — CODING ONLY

Where you are now:
- Week 1: NumPy ✅
- Week 2: pandas ✅
- Week 3: dot product, weights, gradients ✅
- Week 4: probability, stats, bootstrap ✅
- Week 5: scikit-learn (X/y, train/test, linear + logistic regression, KNN) ← you are here

Rules for every day:
1. Write code by hand. No copy-paste.
2. Each day = 1 folder, `plan.txt` + `topic_N.py` files (same as now).
3. Every file must RUN and PRINT something.
4. If something is confusing → write it in `confusion.txt` the same day.
5. End of day: commit + push.

---

## WEEK 5 (finish it) — scikit-learn basics

| Day | Code you write |
|-----|----------------|
| Day 4 | `train_test_split` on a small NumPy dataset. Print shapes of X_train, X_test, y_train, y_test. Change `test_size` and `random_state`, see what changes. |
| Day 5 | `StandardScaler`: `fit` on train ONLY, `transform` train and test. Run KNN with and without scaling, print accuracy both times. |
| Day 6 | Metrics: `accuracy_score`, `mean_squared_error`, `confusion_matrix`. Compute MSE by hand with NumPy first, then check with sklearn. |
| Day 7 | Revision: one file, 20 questions mixing Day 1–6. No notes. |

---

## WEEK 6 — Full ML pipeline on a real dataset

Use `sklearn.datasets.load_iris` and `load_diabetes` (no downloading needed).

| Day | Code you write |
|-----|----------------|
| Day 1 | Load dataset → put into pandas DataFrame → `.head()`, `.shape`, `.describe()`, `.isna().sum()` |
| Day 2 | Split X / y from the DataFrame. `train_test_split`. Baseline (mean for regression, most common class for classification). |
| Day 3 | Train LinearRegression on diabetes. Print coefficients, MSE on test. Beat the baseline? |
| Day 4 | Train LogisticRegression + KNN on iris. Compare accuracy. |
| Day 5 | `Pipeline([("scaler", StandardScaler()), ("model", KNeighborsClassifier())])` |
| Day 6 | Plot with matplotlib: predicted vs actual (regression), accuracy vs `n_neighbors` (KNN 1–20). |
| Day 7 | Revision: do the whole pipeline from an empty file in under 30 minutes. |

---

## WEEK 7 — Build it yourself from scratch (NumPy only)

This is where weeks 3 + 5 connect. No sklearn for the model.

| Day | Code you write |
|-----|----------------|
| Day 1 | `predict(X, w, b)` for linear regression using `X @ w + b` |
| Day 2 | `mse_loss(y_pred, y)` and `gradients(X, y, w, b)` |
| Day 3 | Gradient descent loop: 100 steps, print loss every 10 steps |
| Day 4 | Compare your w, b with sklearn's `LinearRegression` on the same data |
| Day 5 | Logistic regression from scratch: `sigmoid`, predict probabilities |
| Day 6 | KNN from scratch: distance with NumPy, `argsort`, majority vote |
| Day 7 | Revision: rewrite linear regression from scratch, no notes |

---

## WEEK 8 — Model evaluation & overfitting

| Day | Code you write |
|-----|----------------|
| Day 1 | `cross_val_score` with 5 folds, print mean and std |
| Day 2 | Overfitting demo: `DecisionTreeClassifier` with `max_depth` 1–20, train vs test accuracy |
| Day 3 | `GridSearchCV` to pick best `n_neighbors` / `max_depth` |
| Day 4 | Bootstrap confidence interval for test accuracy (reuse week 4 bootstrap code!) |
| Day 5 | `precision_score`, `recall_score`, `f1_score` on an imbalanced dataset |
| Day 6 | Mini project: one dataset, 3 models, compare with CV, plot results |
| Day 7 | Revision + write `README.md` for the mini project |

---

## After week 8 (preview)
- Week 9: PyTorch tensors (it's NumPy with gradients)
- Week 10: tiny neural network in PyTorch on iris / MNIST
