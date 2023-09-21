from setuptools import setup, find_packages

setup(
    name="jsonapi",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    description="Extended JSON library.",
    long_description=open("README.md").read(),
)
