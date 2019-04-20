import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="isolearn",
    version="0.1",
    author="Johannes Linder",
    author_email="johannes.linder@hotmail.com.com",
    description="Keras Genomics Data Generators",
    long_description=long_description,
    url="https://github.com/johli/isolearn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
