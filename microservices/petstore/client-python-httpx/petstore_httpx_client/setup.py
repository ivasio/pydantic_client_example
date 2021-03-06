# coding: utf-8

"""
    Swagger Petstore

    This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key `special-key` to test the authorization filters.  # noqa: E501

    The version of the OpenAPI document: 1.0.6
    Contact: apiteam@swagger.io
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "petstore-httpx-client"
VERSION = "1.0.6"
MODELS_PACKAGE = "common-models"
MODELS_PACKAGE_VERSION = "1.0.9"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["pydantic", "httpx", "fastapi", "typing_extensions", f"{MODELS_PACKAGE}=={MODELS_PACKAGE_VERSION}"]

setup(
    name=NAME,
    version=VERSION,
    description="Swagger Petstore",
    author_email="apiteam@swagger.io",
    url="",
    keywords=["Swagger", "Swagger Petstore"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "petstore_httpx_client": ["py.typed"],
    },
    long_description="""\
    This is a sample server Petstore server.  You can find out more about Swagger at [http://swagger.io](http://swagger.io) or on [irc.freenode.net, #swagger](http://swagger.io/irc/).  For this sample, you can use the api key &#x60;special-key&#x60; to test the authorization filters.  # noqa: E501
    """
)
