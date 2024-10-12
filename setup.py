# -*- coding: utf-8 -*-
"""Setup module."""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_requirements():
    """Read requirements.txt."""
    requirements = open("requirements.txt", "r").read()
    return list(filter(lambda x: x != "", requirements.split()))


def read_description():
    """Read README.md and CHANGELOG.md."""
    try:
        with open("README.md") as r:
            description = "\n"
            description += r.read()
        with open("CHANGELOG.md") as c:
            description += "\n"
            description += c.read()
        return description
    except Exception:
        return "GOPEM is a graphical user interface of OPEM (Open Source PEM Fuel Cell Simulation Tool)"


setup(
    name='gopem',
    packages=['gopem'],
    version='0.8',
    description='GOPEM is a graphical user interface of OPEM',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='ECSIM Development Team',
    author_email='opem@ecsim.site',
    url='https://github.com/ecsim/gopem',
    download_url='https://github.com/ecsim/gopem/tarball/v0.8',
    keywords="OPEM PEM FC CELL Fuel-Cell Chemistry GUI PyQt GOPEM",
    project_urls={
        'Webpage': 'http://opem.ecsim.site',
        'Source': 'https://github.com/ecsim/gopem',
    },
    platforms=["any"],
    install_requires=get_requirements(),
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    license='MIT',
    entry_points={
        'console_scripts': [
            'gopem = gopem.__main__:main',
        ]
    }
)
