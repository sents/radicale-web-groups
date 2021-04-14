#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name="radicale-web-groups",
    version="0.2",
    description="""
    Web Interface to use Radicale with groups and owners""",
    long_description="""
    A slight modification to the default Radicale web interface, allowing to
    specify a group for which to create a calendar and acls.""",
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
        "Programming Language :: Python :: 3.9"
        "Programming Language :: Python :: 3.10"
    ],
    license="GNU AGPLv3",
    install_requires=["radicale>=3"],
    author="Finn Krein",
    author_email="finn@krein.moe",
    url='https://github.com/sents/radicale-web-groups',
    packages=["radicale_web_groups"],
    package_data={"radicale_web_groups": ['internal_data/*']},
)
