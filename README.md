# wheel
**ML Data Preparation Package Documentation**
Overview
The ML_data_preparation package is a Python library designed to simplify and standardize the preprocessing of data for machine learning tasks. It is built as a reusable Python package, distributed as a .whl file, and can be installed via pip.

In this document there is entire description of project covering code structure, wheel setup, wheel build and use case of the module. 

**Package Features**

**Automated Handling of Missing Values:** Includes strategies to handle both numeric and categorical missing data.

**Encoding Categorical Variables:** Converts categorical data into numerical format using Label Encoding or One-Hot Encoding.

**Scaling Numerical Data:** Standardizes or normalizes numerical features for better model performance.

**Data Splitting:** Provides an easy way to split datasets into training and testing sets.

**End-to-End Preprocessing Pipeline:** Combines all functionalities in a single function for ease of use.

**Installation**
The package is distributed as a .whl file. To install it:

**Build the Package **(if not already built): Run the following command in the root directory of your project where setup.py is located:

// python3 setup.py bdist_wheel

This will create a .whl file in the dist/ directory.

Install the Wheel File: To install the package locally:

// pip install dist/ML_data_preparation-0.1.0-py3-none-any.whl

**Package Structure**
The ML_data_preparation package is organized into the following modules:

ML_data_preparation/
│
├── __init__.py           # Package-level imports
├── handle_missing.py     # Functions for handling missing values
├── encode.py             # Functions for encoding categorical variables
├── scale.py              # Functions for scaling numerical features
├── split.py              # Functions for splitting datasets
├── autopreprocess.py     # Combines all functionalities into a single pipeline

Each module provides independent functionality and can be used on its own or as part of the auto_preprocess pipeline.

**Using the Package**
Import the Package: Once installed, import the desired modules or functions:

// from ML_data_preparation.autopreprocess import auto_preprocess
// from ML_data_preparation.handle_missing import handle_missing_values

**Example Usage:**

import pandas as pd
from ML_data_preparation.autopreprocess import auto_preprocess

# Example dataset
data = pd.DataFrame({
    "age": [25, None, 35],
    "income": [50000, 60000, None],
    "gender": ["M", None, "F"],
    "bought": [0, 1, 1]
})

# Preprocess the data
X, y = auto_preprocess(data, target="bought", scaling=True, encode=True)
print("Features (X):", X)
print("Target (y):", y)

**Creating and Uploading the Package**
1. Writing setup.py
The setup.py file is crucial for building and distributing the package. Here's what it looks like:

//
from setuptools import setup, find_packages

setup(
    name="ML_data_preparation",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for automated machine learning data preparation.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="http://example.com/mypackage",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
        "scikit-learn>=0.24.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
//

**2. Building the Wheel**
Run the following command to build the .whl file:

bash
Copy code
python3 setup.py bdist_wheel
The built wheel file will be in the dist/ directory.

**3. Uploading to PyPI (Optional)** : To upload your package on 'PyPI' repository, you have to create a token and using that, package can be uploaded to 'PyPI' repository. 
To share your package publicly:

// pip install twine
// twine upload dist/*

**Dependencies**
The package relies on the following Python libraries:

pandas: For handling and manipulating data.
numpy: For numerical operations.
scikit-learn: For preprocessing functions like scaling, encoding, and splitting.
These dependencies are automatically installed when the package is installed.

**How wheel works:**

it uses a setuptools library which read setup.py file . it collects our python files and dependecies listed in setup.py. 

it creates a .whl file in the dist/ directory. 

.whl : it is a file which is zip archieve. if you unzip it, you can see all files and directories organized as: 

**mypackage-0.1.0.dist-info/**   // it is meta data folder : 
it has : 
**MetaData:**: 
it has package details like version, author, dependencies etc. 
**Record:**: 
it has all the files in the package in form of hashes. 
**Wheel:**: 
contains the actual python modules of your package. 

mypackage // your package's python files 












































