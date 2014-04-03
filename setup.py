import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README.rst")).read()

install_requires = [
    "pyramid>=1.4",
    "SQLAlchemy"
]

test_requires = [
    "zope.sqlalchemy"
]

setup(
    name="megalith.sqlalchemy",
    version="0.0.1",
    description="SQLAlchemy helper for Pyramid",
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
    ],
    url="http://www.megalithproject.org",
    license="MIT",
    packages=find_packages(),
    namespace_packages=["megalith"],
    test_suite="megalith.sqlalchemy.tests",
    install_requires=install_requires,
    tests_require=install_requires + test_requires
)
