from setuptools import setup, find_packages

setup(
    name="aicns-univariate-analyzer",
    version="0.0.1",
    description="Univariate time series analyzer library package in AICNS project",
    author="Youngmin An",
    author_email="youngmin.develop@gmail.com",
    license="Apache License 2.0",
    packages=find_packages(),
    install_requires=[
        "pandas==1.1.5",
        "plotly==5.10.0",
        "pyspark==3.2.2",
        "scikit-learn==0.24.2",
    ],
)
