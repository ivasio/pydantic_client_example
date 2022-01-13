from setuptools import setup, find_packages  # noqa: H301

NAME = "common-models"
VERSION = "1.0.9"


REQUIRES = ["pydantic"]

setup(
    name=NAME,
    version=VERSION,
    description="Swagger Petstore Models",
    author_email="apiteam@swagger.io",
    url="",
    keywords=["Swagger", "Swagger Petstore"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is DTO models lib for a sample server Petstore server
    """
)
