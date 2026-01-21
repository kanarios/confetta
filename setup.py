from setuptools import find_packages, setup


def find_required():
    with open("requirements.txt") as f:
        return f.read().splitlines()


setup(
    name="confetta",
    version="0.1.1",
    description="Configuration helpers for Docker-based development environments",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="kanarios",
    author_email="",
    python_requires=">=3.7",
    url="https://github.com/kanarios/confetta",
    license="Apache-2.0",
    packages=find_packages(exclude=("tests",)),
    package_data={"confetta": ["py.typed"]},
    install_requires=find_required(),
)
