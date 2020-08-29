import os
import re

from setuptools import find_packages, setup


ROOT_DIR = os.path.abspath(os.path.dirname(__file__))


def get_version():
    with open(os.path.join(ROOT_DIR, "src", "flask_postmark", "__init__.py")) as f:
        content = f.read()
        return re.findall(r"__version__ = \"(.+)\"", content)[0]


with open(os.path.join(ROOT_DIR, "README.rst")) as fd:
    long_description = fd.read()

setup(
    name="Flask-Postmark",
    version=get_version(),
    url="https://github.com/Stranger6667/Flask-Postmark",
    license="MIT",
    author="Dmitry Dygalo",
    author_email="dadygalo@gmail.com",
    description="Postmark Flask extension",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    keywords=["flask", "postmark", "email"],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=["Flask", "postmarker >= 0.11.2"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Email",
    ],
)
