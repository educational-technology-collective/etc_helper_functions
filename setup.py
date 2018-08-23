import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="etc",
    version="0.0.1",
    author="Anant Mittal",
    author_email="anmittal@umich.edu",
    description="A python package to help etc research group",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/educational-technology-collective/etc_helper_functions",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)