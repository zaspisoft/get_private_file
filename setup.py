from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in get_private_file/__init__.py
from get_private_file import __version__ as version

setup(
	name="get_private_file",
	version=version,
	description="Get Private File if you have Access to File DocType",
	author="Zaspi Softwares",
	author_email="zaspisoft@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
