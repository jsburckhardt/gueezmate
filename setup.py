import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# What packages are required for this module to be executed?
with open("requirements.in") as f:
    INSTALL_REQUIRES = f.read().splitlines()

setuptools.setup(
    name="gueezmate",
    version="{VERSION}",
    author="jsburckhardt",
    author_email="",
    description="expense tracker api",
    install_requires=INSTALL_REQUIRES,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jsburckhardt/gueezmate",
    packages=setuptools.find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
