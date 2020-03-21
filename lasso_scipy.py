from sklearn.linear_model import Lasso
import numpy as np

x = np.random.randn(100, 5)
true_weights = [2, 3, 0, 0, -1]

y = x.dot(true_weights) + np.random.randn(np.shape(x)[0]) * 0.1

lasso = Lasso(alpha=0.2)
lasso.fit(x, y)
print(lasso.coef_)
