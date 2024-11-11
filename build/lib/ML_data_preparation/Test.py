from autoPreprocess import auto_preprocess

import pandas as pd

# Example DataFrame
data = pd.DataFrame({
    "age": [25, 30, None, 35],
    "income": [50000, 60000, 55000, None],
    "gender": ["M", "F", "M", "F"],
    "bought": [0, 1, 0, 1]
})

# Automatically preprocess the data
X, y = auto_preprocess(data, target="bought", scaling=True, encode=True)
print(X)
print(y)
