# -*- coding: utf-8 -*-
"""Setup module."""
from setuptools import setup


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
    keywords='OPEM PEM FC CELL Fuel-Cell Chemistry GUI PyQt GOPEM',
    project_urls={
        'Webpage': 'http://opem.ecsim.site',
        'Source': 'https://github.com/ecsim/gopem',
    },
    platforms=['any'],
    install_requires=[
        'art>0.7',
        'requests>=2.20.0',
        'matplotlib>=2.2.2',
        'PyQt5>=5.10',
        'PyQt5-sip>=4.19.12',
        'opem>=0.9'
    ],
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
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
