#!/usr/bin/env python

from setuptools import find_packages, setup

PROJECT = "jt"

# Change docs/sphinx/conf.py too!
VERSION = "0.1"

try:
    long_description = open("README.rst", "rt").read()
except IOError:
    long_description = ""

setup(
    name=PROJECT,
    version=VERSION,
    description="Demo app for cliff",
    long_description=long_description,
    author="Doug Hellmann",
    author_email="doug.hellmann@gmail.com",
    url="https://github.com/openstack/cliff",
    download_url="https://github.com/openstack/cliff/tarball/master",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "Environment :: Console",
    ],
    platforms=["Any"],
    scripts=[],
    provides=[],
    install_requires=["cliff"],
    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": ["jt = jt.main:main"],
        "cliff.demo": [
            "simple = jt.simple:Simple",
            "two_part = jt.simple:Simple",
            "error = jt.simple:Error",
            "list files = jt.list:Files",
            "files = jt.list:Files",
            "file = jt.show:File",
            "show file = jt.show:File",
            "unicode = jt.encoding:Encoding",
            "hooked = jt.hook:Hooked",
        ],
        "cliff.demo.hooked": [
            "sample-hook = jt.hook:Hook",
        ],
    },
    zip_safe=False,
)
