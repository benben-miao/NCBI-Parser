#!/usr/bin/python
# _*_ coding:utf-8 _*_

from setuptools import setup, find_packages

### 1. Read the README.md contents
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
readme = 'ncbiparser/README.md'

### 2. Setup the package configure
setup(
    # 2.1 Package information
    name="ncbiparser",
    version="1.1.0",
    url="https://github.com/benben-miao/NCBI-Parser",
    keywords=["CLI", "Biology", "NCBI", "Parser"],
    description="Search and fetch the Species Latin names, Accessory Number, Sequence Length, Division, Collection Country, Collection Date, Collected Worker, Identified Worker, and Reference information, etc. of the search records as tabular files.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    download_url="https://pypi.org/project/ncbi-parser",

    # 2.2 Developer information
    author="benben-miao",
    author_email="benben.miao@outlook.com",
    maintainer="benben-miao",
    maintainer_email="benben.miao@outlook.com",
    license="MIT License",

    # 2.3 Package configure
    # include_package_data=True,
    platforms="any",
    install_requires=['biopython', 'click'],
    # packages=find_packages(),
    packages=['ncbiparser'],
    entry_points={
        'console_scripts': ['ncbiparser=ncbiparser.ncbiparser:run']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    data_files=[readme],
    # package_data={
    #     '':['examples/*.xlsx']
    # },
    include_package_data=True
    # exclude_package_data={
    # }
)

### 3. Package build, test and publish
# 3.1 Install setuptools with wheel and twine
# pip install --upgrade setuptools wheel twine

# 3.2 Check the setup.py content
# python setup.py check

# 3.2 Build source code tarball
# python setup.py sdist

# 3.3 Build wheel package and test
# python setup.py bdist_wheel
# pip install dist\*.whl

# 3.4 Test package and uninstall test version
# ncbiparser --help
# pip uninstall ncbiparser

# 3.5 Publish the package to PyPI
# twine upload dist\*