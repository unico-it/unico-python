from setuptools import setup, find_packages

setup(
    name="UNICO Python",
    version="0.1.0",
    description="Python Client for the UNICO Api",
    author="UNICO",
    packages=find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)
