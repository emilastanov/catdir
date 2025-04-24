from setuptools import setup, find_packages

setup(
    name="catdir",
    use_scm_version=True,
    setup_requires=[
        "setuptools-scm"
    ],
    description="Concatenate and print the contents of all files in a directory and its subdirectories.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Emil Astanov",
    author_email="emila1998@yandex.ru",
    url="https://github.com/emilastanov/catdir",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "catdir=catdir.main:catdir",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Software Development :: Build Tools",
    ],
    keywords="catdir concatenate files directory cli click",
)
