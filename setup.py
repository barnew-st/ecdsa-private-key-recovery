#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
try:
    from ecdsa_key_recovery import utils
except:
    pass
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


version = "0.1.2"

setup(
    name="ecdsa-private-key-recovery",
    version=version,
    packages=find_packages(),
    author="Security Research Team",
    author_email="research@crypto-sec.io",
    description=(
        "A simple library to recover the private key of ECDSA and DSA signatures sharing the same nonce k and therefore having identical signature parameter r"),
    license="GPLv2",
    keywords=["ecdsa", "dsa", "recovery", "nonce", "blockchain"],
    url="https://github.com/crypto-research/ecdsa-key-recovery",
    download_url="https://github.com/crypto-research/ecdsa-key-recovery/tarball/v%s" % version,
    # python setup.py register -r https://testpypi.python.org/pypi
    long_description=read("README.md") if os.path.isfile("README.md") else "",
    long_description_type='text/markdown',
    install_requires=["pycryptodomex",
                      "pycrypto",
                      "ecdsa"],
)
