import os
from setuptools import setup, find_packages

version = "1.0dev"


def read(*rnames):
    return open(
        os.path.join('.', *rnames)
    ).read()

long_description = "\n\n".join(
    [read('README.rst'),
     read('docs', 'INSTALL.rst'),
     read('docs', 'HISTORY.rst')]
)

classifiers = [
    "Programming Language :: Python",
    "Topic :: Software Development"]
EPS = {
    'console_scripts': [
        'mc_github_staff = makina.githubscripts.githubscripts:main',
    ]
 }
name = 'makina.githubscripts'
setup(
    name=name,
    namespace_packages=[
         'makina'
    ],
    version=version,
    description='github scripts',
    long_description=long_description,
    classifiers=classifiers,
    keywords='',
    author='kiorky',
    author_email='kiorky@cryptelium.net',
    url='http://www.generic.com',
    license='GPL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    extras_require={
        #'test': ['plone.testing']
        'test': []
    },
    install_requires=[
        'setuptools',
        'pygithub',
        # -*- Extra requirements: -*-
    ],
    # define there your console scripts
    entry_points=EPS,
)
# vim:set ft=python:
