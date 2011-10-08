"""Installer for py-serverdensity
"""

import os
cwd = os.path.dirname(__file__)
__version__ = open(os.path.join(cwd, 'serverdensity', 'version.txt'), 'r').read().strip()

try:
        from setuptools import setup, find_packages
except ImportError:
        from ez_setup import use_setuptools
        use_setuptools()
        from setuptools import setup, find_packages
setup(
    name='py-serverdensity',
    description='Python ServerDensity.com API wrapper',
    long_description=open('README.rst').read(),
    version=__version__,
    author='Wes Mason',
    author_email='wes@boxedice.com',
    url='https://github.com/1stvamp/py-serverdensity',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=open('requirements.txt').readlines(),
    package_data={'serverdensity': ['version.txt']},
    include_package_data=True,
    license='BSD'
)
