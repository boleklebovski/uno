from setuptools import setup, find_packages

setup(
    name="uno",
    version="0.2.0",
    packages=find_packages(),
    install_requires=["web3>=6.15.0", "requests>=2.31.0"],
    entry_points={"console_scripts": ["uno=uno.cli:main"]},
    python_requires=">=3.10",
)
