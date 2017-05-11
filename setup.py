# coding: utf-8
"""
Flask-Postmark
--------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-Postmark',
    version='0.1',
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
        'Flask', 'postmarker >= 0.11.1'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Email',
    ]
)
