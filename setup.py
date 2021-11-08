#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2020 Scriptim (https://github.com/Scriptim)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import re

import setuptools

with open('README.md', 'r') as readme:
    long_description = readme.read()
    github_url_prefix = '(https://github.com/Scriptim/Abalone-BoAI/tree/master/'
    github_raw_url_prefix = '(https://raw.githubusercontent.com/Scriptim/Abalone-BoAI/master/'
    long_description = re.sub(
        '\\(\\./img/', github_raw_url_prefix + 'img/', long_description)
    long_description = re.sub('\\(\\./', github_url_prefix, long_description)

setuptools.setup(
    name='alpha-zero-general',
    version='1.0',
    license='MIT',
    packages=['alpha_zero_general'],
    install_requires=['cffi', 'coloredlogs',
                      'cython', 'tqdm', 'pandas', 'numpy'],
    python_requires='>=3.6',
)
