from setuptools import find_namespace_packages
from setuptools import setup

setup(
    name="hydra-configs-pytorch-lightning",
    version="0.1.0",
    packages=find_namespace_packages(include=["hydra_configs*"]),
    author=["Rosario Scalise"],
    author_email=["rosario@cs.uw.edu"],
    url="http://github.com/romesco/hydra-lightning",
    install_requires=[
        "omegaconf",
    ],
)
