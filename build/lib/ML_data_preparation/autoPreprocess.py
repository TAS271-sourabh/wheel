from encoding import encode_categorical
from missingValue import handle_missing_values
from scale import scale_data
from split import split_dataset


def auto_preprocess(df, target, scaling=True, encode=True, missing_strategy="mean"):
    """
    Automatically preprocess the dataset.

    Args:
        df (pd.DataFrame): Input dataframe.
        target (str): Target column name.
        scaling (bool): Whether to scale numerical features.
        encode (bool): Whether to encode categorical features.
        missing_strategy (str): Strategy to handle missing values.

    Returns:
        tuple: Processed features (X) and target (y).
    """
    # Handle missing values
    df = handle_missing_values(df, strategy=missing_strategy)
    
    # Separate target
    y = df[target]
    X = df.drop(columns=[target])
    
    # Encode categorical features
    if encode:
        cat_cols = X.select_dtypes(include=['object', 'category']).columns
        X = encode_categorical(X, cat_cols, method="onehot")
    
    # Scale numerical features
    if scaling:
        num_cols = X.select_dtypes(include=['float64', 'int64']).columns
        X = scale_data(X, num_cols, method="standard")
    
    return X, y
