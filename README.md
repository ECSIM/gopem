<div align="center">
<img src="https://github.com/ECSIM/opem/raw/master/otherfile/logo.png" width=250px height=250px>
</br>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>
<a href="https://badge.fury.io/py/gopem"><img src="https://badge.fury.io/py/gopem.svg" alt="PyPI version" height="18"></a>
<a href = "https://hub.docker.com/r/ecsim/gopem"><img alt="Docker Cloud Build Status" src="https://img.shields.io/docker/cloud/build/ecsim/gopem"></a>
</div>

--------

## Table of contents				
   * [Overview](https://github.com/ECSIM/gopem#overview)
   * [Installation](https://github.com/ECSIM/gopem#installation)
   * [Usage](https://github.com/ECSIM/gopem#usage)
   * [Issues & Bug Reports](https://github.com/ECSIM/gopem#issues--bug-reports)
   * [Contribution](https://github.com/ECSIM/gopem/blob/master/.github/CONTRIBUTING.md)
   * [Dependencies](https://github.com/ECSIM/gopem#dependencies)
   * [Thanks](https://github.com/ECSIM/gopem#thanks)
   * [Cite](https://github.com/ECSIM/gopem#cite)
   * [Authors](https://github.com/ECSIM/gopem/blob/master/AUTHORS.md)
   * [License](https://github.com/ECSIM/gopem#license)
   * [Donate](https://github.com/ECSIM/gopem#donate-to-our-project)
   * [Changelog](https://github.com/ECSIM/gopem/blob/master/CHANGELOG.md)
   * [Code of Conduct](https://github.com/ECSIM/gopem/blob/master/.github/CODE_OF_CONDUCT.md)

## Overview		

GOPEM is a graphical user interface of [OPEM (Open Source PEM Fuel Cell Simulation Tool)](https://github.com/ECSIM/opem "OPEM").

<table>
	<tr> 
		<td align="center">Branch</td>
		<td align="center">master</td>	
		<td align="center">develop</td>	
	</tr>
	<tr>
		<td align="center">Travis</td>
		<td align="center"><a href="https://travis-ci.org/ECSIM/gopem"><img src="https://travis-ci.org/ECSIM/gopem.svg?branch=master"></a></td>
		<td align="center"><a href="https://travis-ci.org/ECSIM/gopem"><img src="https://travis-ci.org/ECSIM/gopem.svg?branch=develop"></a></td>
	</tr>
	<tr>
		<td align="center">AppVeyor</td>
		<td align="center"><a href="https://ci.appveyor.com/project/sepandhaghighi/gopem"><img src="https://ci.appveyor.com/api/projects/status/2765bl1ne9cy1j4o/branch/master?svg=true"></a></td>
		<td align="center"><a href="https://ci.appveyor.com/project/sepandhaghighi/gopem"><img src="https://ci.appveyor.com/api/projects/status/2765bl1ne9cy1j4o/branch/develop?svg=true"></a></td>
	</tr>
</table>

<table>
	<tr> 
		<td align="center">Code Quality</td>
		<td align="center"><a href="https://www.codefactor.io/repository/github/ecsim/gopem"><img src="https://www.codefactor.io/repository/github/ecsim/gopem/badge" alt="CodeFactor" /></a></td>
		<td align="center"><a href="https://www.codacy.com/app/sepand-haghighi/gopem?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ECSIM/gopem&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/f715670f91fb4765a98f93f1908d4943"/></a></td>
	</tr>
</table>

## Installation	

### Source Code
- Download and install [Python3.x](https://www.python.org/downloads/) (>=3.6)
	- [x] Select `Add to PATH` option
	- [x] Select `Install pip` option
- Download [Version 0.5](https://github.com/ecsim/gopem/archive/v0.5.zip) or [Latest Source ](https://github.com/ecsim/gopem/archive/develop.zip)
- Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` (Need root access)
- Run `python3 setup.py install` or `python setup.py install` (Need root access)				

### PyPI


- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- Run `pip install gopem` or `pip3 install gopem` (Need root access)

### Easy Install

- Run `easy_install --upgrade gopem` (Need root access)


### Docker	

- Run `docker pull ecsim/gopem` (Need root access)
- Configuration :
	- Ubuntu 16.04
	- Python 3.6


### Exe Version (Only Windows)
- Download [Installer-Version 0.5](https://github.com/ECSIM/gopem/releases/download/v0.5/GOPEM-0.5.exe) or [Portable-Version 0.5](https://github.com/ECSIM/gopem/releases/download/v0.5/GOPEM-Portable-0.5.exe)
- Run and install

⚠️ The portable build is slower to start

### DMG Version (MacOS)
- Download [DMG-Version 0.5](https://github.com/ECSIM/gopem/releases/download/v0.5/GOPEM-0.5.dmg)
- Open DMG file
- Copy `GOPEM` into your system
- Run `GOPEM`


### Exe Version Note
For GOPEM targeting Windows < 10, the user needs to take special care to include the Visual C++ run-time .dlls: Python >=3.5 uses Visual Studio 2015 run-time, which has been renamed into “Universal CRT“ and has become part of Windows 10. For Windows Vista through Windows 8.1 there are Windows update packages, which may or may not be installed in the target-system. So you have the following options:

1. Use [OPEM](https://github.com/ECSIM/opem) (Without GUI)
2. Use [Source Code](https://github.com/ECSIM/gopem#source-code)
3. Download and install [Visual C++ Redistributable for Visual Studio 2015](https://www.microsoft.com/en-us/download/details.aspx?id=48145)

### System Requirements
GOPEM will likely run on a modern dual core PC. Typical configuration is:

- Dual Core CPU (2.0 Ghz+)
- 2GB of RAM

⚠️ Note that it may run on lower end equipment though good performance is not guaranteed.

## Usage

<div align="center">

<img src="https://github.com/ECSIM/gopem/blob/master/rsrc/GOPEM.gif">
<p>GIF</p>

<img src="https://github.com/ECSIM/gopem/blob/master/rsrc/SS1.png">
<p>Screenshot 1</p>

<img src="https://github.com/ECSIM/gopem/blob/master/rsrc/SS2.png">
<p>Screenshot 2</p>

</div>	

- Open `CMD` (Windows) or `Terminal` (UNIX)
- Run `python -m gopem` or `python3 -m gopem` (or run `GOPEM.exe`)
- Wait about 4-15 seconds (depends on your system specification)
- Enter PEM cell parameters (or run standard test vectors)	
- For more information about parameters visit [OPEM (Open Source PEM Fuel Cell Simulation Tool)](https://github.com/ECSIM/opem "OPEM")
## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!							
or send an email to [opem@ecsim.ir](mailto:opem@ecsim.ir "opem@ecsim.ir"). 

Gitter is another option :				

[![Gitter](https://badges.gitter.im/ECSIM/opem.svg)](https://gitter.im/ECSIM/opem?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)


## Dependencies		


<table>
	<tr> 
		<td align="center">master</td>	
		<td align="center">develop</td>	
	</tr>
	<tr>
		<td align="center"><a href="https://requires.io/github/ECSIM/gopem/requirements/?branch=master"><img src="https://requires.io/github/ECSIM/gopem/requirements.svg?branch=master" alt="Requirements Status" /></a></td>
		<td align="center"><a href="https://requires.io/github/ECSIM/gopem/requirements/?branch=develop"><img src="https://requires.io/github/ECSIM/gopem/requirements.svg?branch=develop" alt="Requirements Status" /></a></td>
	</tr>
</table>

## Thanks

* [PyInstaller](https://github.com/pyinstaller/pyinstaller)



## Cite

If you use OPEM in your research , please cite this paper :

<pre>

@article{Haghighi2018,
  doi = {10.21105/joss.00676},
  url = {https://doi.org/10.21105/joss.00676},
  year  = {2018},
  month = {jul},
  publisher = {The Open Journal},
  volume = {3},
  number = {27},
  pages = {676},
  author = {Sepand Haghighi and Kasra Askari and Sarmin Hamidi and Mohammad Mahdi Rahimi},
  title = {{OPEM} : Open Source {PEM} Cell Simulation Tool},
  journal = {Journal of Open Source Software}
}


</pre>

Download [OPEM.bib](http://www.ecsim.ir/opem/OPEM.bib)(BibTeX Format)									

<table>
	<tr> 
		<td align="center">JOSS</td>
		<td align="center"><a style="border-width:0" href="https://doi.org/10.21105/joss.00676"><img src="http://joss.theoj.org/papers/10.21105/joss.00676/status.svg" alt="DOI badge" ></a></td>	
	</tr>
	<tr>
		<td align="center">Zenodo</td>
		<td align="center"><a href="https://doi.org/10.5281/zenodo.1133110"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.1133110.svg" alt="DOI"></a></td>
	</tr>
	<tr>
		<td align="center">Researchgate</td>
		<td align="center"><a href="https://www.researchgate.net/project/Open-Source-Electrochemistry-Simulation-Toolbox"><img src="https://img.shields.io/badge/Researchgate-OPEM-yellow.svg"></a></td>
	</tr>
</table>

## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FECSIM%2Fgopem.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FECSIM%2Fgopem?ref=badge_large)		


## Donate to our project
								
<h3>Bitcoin :</h3>					

```12Xm1qL4MXYWiY9sRMoa3VpfTfw6su3vNq```			



<h3>Payping (For Iranian citizens) :</h3>

<a href="http://www.payping.net/sepandhaghighi" target="__blank"><img src="http://www.qpage.ir/images/payping.png" height=100px width=100px></a>	


<h3>Say Thanks! </h3>


<a href="https://saythanks.io/to/ecsim"><img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg"></a>
