# coding: utf-8

import os

from setuptools import setup

current_dir = os.path.abspath(os.path.dirname(__file__))
readme = open(os.path.join(current_dir, 'README.md')).read()

setup(
    name='pythononrio-templatetags',
    version='1.0',
    packages=['notificacoes'],
    description='Templates Tags desenvolvidos no Python On Rio',
    long_description=readme,
    author='Élysson MR',
    author_email='elyssonmr@gmail.com',
    url='https://github.com/elyssonmr/django_pkg/',
    license='MIT',
    install_requires=[
        'Django>=1.8',
    ]
)
