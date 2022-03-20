import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="casefy",
    version="0.1.2",
    author="Diego Miguel Lozano",
    author_email="hello@diegomiguel.me",
    description="Utilities for string case conversion.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dmlls/python-casefy",
    project_urls={
        "Bug Tracker": "https://github.com/dmlls/python-casefy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "casefy"},
    packages=setuptools.find_packages(where="casefy"),
    python_requires=">=3.6",
    package_data={
        "": ["py.typed"],
    }
)
