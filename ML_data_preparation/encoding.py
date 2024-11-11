import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def encode_categorical(df, columns, method="onehot"):
    """
    Encode categorical features in the dataset.

    Args:
        df (pd.DataFrame): Input dataframe.
        columns (list): List of columns to encode.
        method (str): Encoding method ("onehot" or "label").

    Returns:
        pd.DataFrame: Dataframe with encoded features.
    """
    if method == "onehot":
        encoder = OneHotEncoder(sparse=False)
        encoded = encoder.fit_transform(df[columns])
        encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(columns))
        df = df.drop(columns, axis=1).join(encoded_df)
    elif method == "label":
        encoder = LabelEncoder()
        for col in columns:
            df[col] = encoder.fit_transform(df[col])
    return df
