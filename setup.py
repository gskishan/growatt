from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in growatt/__init__.py
from growatt import __version__ as version

setup(
	name="growatt",
	version=version,
	description="Common Use",
	author="Simran",
	author_email="shreyasnaik01",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
