from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in education/__init__.py
from asxoraEducation import __version__ as version

setup(
	name="asxoraEducation",
	version=version,
	description="asxoraEducation",
	author="Asxora Technology LLP",
	author_email="abid@asxora.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
)
