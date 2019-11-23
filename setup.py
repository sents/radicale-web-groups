#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from distutils.core import setup

WEB_FILES = ["web/css/icon.png", "web/css/main.css", "web/fn.js",
             "web/index.html"]

setup(
    name="radicale-web-groups",
    version="0.1",
    description="""
    Web Interface to use Radicale with groups""",
    long_description="""
    A slight modification to the default Radicale web interface, allowing to
    specify a group for which to create a calendar.""",
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    license="GNU GPLv3",
    install_requires=["radicale"],
    author="Finn Krein",
    author_email="finn@krein.moe",
    url='https://github.com/sents/radicale-web-groups',
    packages=["radicale_web_groups"],
    package_data={"radicale_web_groups": WEB_FILES},
)
