import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="comgen",
    version="0.0.1",
    author="iBug",
    author_email="iBug@users.noreply.github.com",
    description="Git commit generator, good for creating loads of (empty) commits",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iBug/comgen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
