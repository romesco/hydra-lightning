from setuptools import find_namespace_packages, setup

setup(
    name="hydra-configs-torch",
    version="1.0.1",
    packages=find_namespace_packages(include=["hydra_configs*"]),
    author=["Rosario Scalise"],
    author_email=["rosario@cs.uw.edu"],
    url="http://github.com/romesco/hydra-lightning",
    include_package_data=True,
)
