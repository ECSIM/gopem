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
    version='0.2',
    description='GOPEM is a graphical user interface of OPEM',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    author='Mohammad Mahdi Rahimi,Sepand Haghighi,Kasra Askari,Sarmin Hamidi',
    author_email='opem@ecsim.ir',
    url='https://github.com/ecsim/gopem',
    download_url='https://github.com/ecsim/gopem/tarball/v0.2',
    keywords="OPEM PEM FC CELL Fuel-Cell Chemistry GUI PyQt GOPEM",
    project_urls={
        'Webpage': 'http://opem.ecsim.ir',
        'Say Thanks!': 'https://saythanks.io/to/ecsim',
        'Source': 'https://github.com/ecsim/gopem',
    },
    platforms=["any"],
    install_requires=get_requirements(),
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    license='MIT',
)
