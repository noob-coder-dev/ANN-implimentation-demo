from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Manojit Roy",
    author_email="roy.monojit982810@gmail.com",
    description="A package for ANN Implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/noob-coder-dev/ANN-implimentation-demo",
    packages=["src"],
    python_requires=">=3.8",
    install_requires=[
        "tensorflow",
        "matplotlib",
        "seaborn",
        "numpy",
        "pandas"

    ]
)