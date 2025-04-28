from setuptools import setup, find_packages

setup(
    name="unico",
    version="0.1.0",
    description="Python Client for the UNICO Api",
    author="UNICO",
    author_email="info@theunico.it",
    license="MIT",
    python_requires=">=3.11",
    install_requires=["requests"],
    packages=find_packages(include=["unico", "unico.*"]),
)
