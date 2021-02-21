from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="torch-gnn",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "joblib",
        "lxml",
        "networkx",
        "numpy",
        "pandas",
        "requests",
        "scikit-learn",
        "scipy",
        "tqdm",
    ],
    url="https://github.com/quocdat32461997/torch-gnn",
    license="Apache-2.0 License",
    author="quocdat32461997",
    author_email="quocdat32461997@yahoo.com",
    description="Graph Neural Networks in PyTorch",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
