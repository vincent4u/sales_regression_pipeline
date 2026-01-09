import numpy as np
from sklearn.linear_model import LinearRegression


def test_linear_regression_trains_successfully():
    """Model should fit without errors and produce coefficients."""
    X = np.array([[1], [2], [3], [4]])
    y = np.array([100, 200, 300, 400])

    model = LinearRegression()
    model.fit(X, y)

    assert model.coef_ is not None
    assert model.intercept_ is not None