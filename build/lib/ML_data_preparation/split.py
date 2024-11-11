import pandas as pd
from sklearn.model_selection import train_test_split

def split_dataset(df, target, test_size=0.2, stratify=True):
    """
    Split the dataset into train and test sets.

    Args:
        df (pd.DataFrame): Input dataframe.
        target (str): Target column name.
        test_size (float): Fraction of the dataset to include in the test split.
        stratify (bool): Whether to stratify by the target.

    Returns:
        tuple: X_train, X_test, y_train, y_test
    """
    X = df.drop(columns=[target])
    y = df[target]
    stratify = y if stratify else None
    return train_test_split(X, y, test_size=test_size, stratify=stratify, random_state=42)
