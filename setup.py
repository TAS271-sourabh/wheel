from setuptools import setup, find_packages

setup(
    name="ML_data_preparation",  # Name of your package
    version="0.1.0",  # Version of your package
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for automated machine learning data preparation.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="http://example.com/mypackage",  # Optional: URL for your package
    packages=find_packages(),  # Automatically finds submodules
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
    python_requires=">=3.6",  # Specify compatible Python versions
)
