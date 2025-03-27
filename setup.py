from setuptools import setup, find_packages

setup(
    name="networksecurity-mlops",
    version="0.1.0",
    author="RajeshR",
    description="A package for MLOps in network security",
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here, e.g., 'numpy', 'pandas', 'scikit-learn'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)