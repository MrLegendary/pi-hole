from setuptools import setup, find_packages

setup(
    name="Pi-hole",
    version="3.0.0",
    packages=find_packages(),
    scripts=["bin/pihole"],
    url="https://pi-hole.net",
    license="AGPL"
)
