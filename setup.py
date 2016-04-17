from setuptools import setup, find_packages

install_requires = [
]

tests_require = install_requires + [
    "mock",
    "nose2",
]

dependency_links = [
]

setup(
    name="furtivio.example",
    version="0.1",
    namespace_packages=["furtivio"],
    description="",
    long_description="",

    author="Furtivio LLC",
    author_email="janitha@furtivio.com",
    license="Apache 2.0",
    classifiers=(
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Topic :: Utilities"),
    packages=find_packages(),
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite="nose.collector",
    extras_require={
        "test": tests_require,
    },
    dependency_links=dependency_links,

    entry_points=("""
    [console_scripts]
    furtivio_example=furtivio.example.main:main
    """),
)
