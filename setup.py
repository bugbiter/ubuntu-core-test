#!/usr/bin/env python3
# coding=utf-8

from setuptools import setup

package_name = 'iot-labs-uc-test'
filename = package_name + '.py'

def get_version():
    import ast

    with open(filename) as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                return ast.parse(line).body[0].value.s

def get_long_description():
    try:
        with open('README.md', 'r') as f:
            return f.read()
    except IOError:
        return ''

setup(
    name=package_name,
    version=get_version(),
    author='bugbiter',
    author_email='bugbiter@live.no',
    description='Test Ubuntu Core on RPi',
    url='https://github.com/bugbiter/ubuntu-core-test',
    long_description=get_long_description(),
    py_modules=[package_name],
    entry_points={
        'console_scripts': [
            'iot-labs-uc-test = iot-labs-uc-test:main'
        ]
    },
    license='License :: OSI Approved :: MIT License'
)