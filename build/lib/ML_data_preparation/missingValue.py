import pandas as pd
from sklearn.impute import SimpleImputer

def handle_missing_values(df, strategy="mean", columns=None):
    """
    Handle missing values in the dataset.

    Args:
        df (pd.DataFrame): Input dataframe.
        strategy (str): Strategy for imputation ("mean", "median", "most_frequent", "constant").
        columns (list): List of columns to impute. If None, all columns are processed.

    Returns:
        pd.DataFrame: Dataframe with missing values handled.
    """
    # Default to all columns if none are provided
    columns = columns or df.columns

    # Separate numeric and non-numeric columns
    numeric_cols = df[columns].select_dtypes(include=["number"]).columns
    non_numeric_cols = df[columns].select_dtypes(exclude=["number"]).columns

    # Handle numeric columns
    if not numeric_cols.empty:
        num_imputer = SimpleImputer(strategy=strategy)
        df[numeric_cols] = num_imputer.fit_transform(df[numeric_cols])

    # Handle non-numeric columns (most_frequent or constant strategy)
    if not non_numeric_cols.empty:
        cat_strategy = "most_frequent" if strategy in ["mean", "median"] else strategy
        cat_imputer = SimpleImputer(strategy=cat_strategy)
        df[non_numeric_cols] = cat_imputer.fit_transform(df[non_numeric_cols])

    return df
