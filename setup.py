import multiprocessing, logging # Fix atexit bug
from setuptools import setup, find_packages

import pytool

def readme():
    try:
        return open('README.md').read()
    except:
        pass
    return ''

setup(
        name='pytool',
        version=pytool.__version__,
        author="Jacob Alheid",
        author_email="jake@about.me",
        description="A Collection of Python Tools",
        long_description=readme(),
        url='http://github.com/shakefu/pytool',
        packages=find_packages(exclude=['test']),
        test_suite='nose.collector',
        tests_require=[
            'nose',
            'mock',
            ],
        )
