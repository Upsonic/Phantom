#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import setup

with open('requirements.txt') as fp:
    install_requires = fp.read()
setup(
    name="upsonic_phantom",
    version="0.0.0",
    description="""The cloud python encryption for your applications !""",
    long_description="".join(open("README.md", encoding="utf-8").readlines()),
    long_description_content_type="text/markdown",
    url="https://github.com/Upsonic/Phantom",
    author="Onur Atakan ULUSOY",
    author_email="onur.atakan.ulusoy@upsonic.co",
    license="MIT",
    packages=["upsonic_phantom",],
    install_requires=install_requires,
    python_requires=">= 3",
    zip_safe=False,
)

