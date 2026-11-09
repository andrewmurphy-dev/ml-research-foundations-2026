import numpy as np
from sklearn.metrics import mean_squared_error

y_true = np.array([3, 5, 2, 7])
y_guess = np.array([2, 5, 4, 8])

# by hand
errors = y_true - y_guess
squared = errors ** 2
mse_by_hand = squared.mean()
print("MSE by hand:", mse_by_hand)

# check with sklearn
mse_sklearn = mean_squared_error(y_true, y_guess)
print("MSE sklearn:", mse_sklearn)
