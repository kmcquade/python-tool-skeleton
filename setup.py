"""Setup script"""
import setuptools
import os
import re

HERE = os.path.abspath(os.path.dirname(__file__))
VERSION_RE = re.compile(r"""__version__ = ['"]([0-9.]+)['"]""")
TESTS_REQUIRE = ["coverage", "nose", "pytest"]
DESCRIPTION = ""
REQUIRED_PACKAGES = [
    "click",
    "click_option_group",
]


def get_version():
    init = open(os.path.join(HERE, "yolo", "bin", "version.py")).read()
    return VERSION_RE.search(init).group(1)


def get_description():
    return open(
        os.path.join(os.path.abspath(HERE), "README.md"), encoding="utf-8"
    ).read()


setuptools.setup(
    name="yolo",
    include_package_data=True,
    version=get_version(),
    author="null",
    author_email="null@example.com",
    description=DESCRIPTION,
    long_description=get_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/yolo/yolo",
    packages=setuptools.find_packages(exclude=["test*"]),
    tests_require=TESTS_REQUIRE,
    install_requires=REQUIRED_PACKAGES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": "yolo=yolo.bin.cli:main"},
    zip_safe=True,
    keywords="security",
    python_requires=">=3.7",
)
