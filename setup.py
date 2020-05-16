import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setuptools.setup(
    name="ds-util",
    version="0.1.5",
    author="noko",
    author_email="",
    description="You can receive the message 'Hello!!!'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.nasa.future.co.jp/data-analysis/mlops/ds-util",
    packages=setuptools.find_packages(),
    install_requires=_requires_from_file('requirements.txt'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['ds-util = ds_util.sample_command:main']
    },
    python_requires='>=3.7',
)
