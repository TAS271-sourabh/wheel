import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def scale_data(df, columns, method="standard"):
    """
    Scale numerical features in the dataset.

    Args:
        df (pd.DataFrame): Input dataframe.
        columns (list): List of columns to scale.
        method (str): Scaling method ("standard" or "minmax").

    Returns:
        pd.DataFrame: Dataframe with scaled features.
    """
    if method == "standard":
        scaler = StandardScaler()
    elif method == "minmax":
        scaler = MinMaxScaler()

    df[columns] = scaler.fit_transform(df[columns])
    return df
