from setuptools import setup, find_packages

setup(
    name="hashutils",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "hashutils=hashutils.cli:main",
        ],
    },
    install_requires=[],
    python_requires=">=3.8",
    description="Calcula el hash de textos y archivos desde la terminal",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="victor17v",
    license="MIT",
    url="https://github.com/victor17v/hashutils",
)
