# coding: utf-8
"""
Flask-Postmark
--------------

This is a simple integration with Postmark for Flask applications.
"""
import os
import re

from setuptools import setup


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))


def get_version():
    with open(os.path.join(ROOT_DIR, 'flask_postmark', '__init__.py')) as fd:
        content = fd.read()
        return re.findall(r"__version__ = '(.+)'", content)[0]


setup(
    name='Flask-Postmark',
    version=get_version(),
    url='https://github.com/Stranger6667/Flask-Postmark',
    license='MIT',
    author='Dmitry Dygalo',
    author_email='dadygalo@gmail.com',
    description='Postmark Flask extension',
    keywords=['flask', 'postmark', 'email'],
    long_description=__doc__,
    packages=['flask_postmark'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask', 'postmarker >= 0.11.2'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Email',
    ]
)
