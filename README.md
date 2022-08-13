<div align="center">
<img src="https://github.com/ECSIM/gopem/raw/master/rsrc/logo.png" width=350px>
</br>
<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3" /></a>
<a href="https://badge.fury.io/py/gopem"><img src="https://badge.fury.io/py/gopem.svg" alt="PyPI version" height="18"></a>
</div>
<a href="https://discord.gg/mgpwvEuBxZ">
  <img src="https://img.shields.io/discord/1006472275920425012.svg" alt="Discord Channel">
</a>

--------

## Table of Contents				
   * [Overview](https://github.com/ECSIM/gopem#overview)
   * [Installation](https://github.com/ECSIM/gopem#installation)
   * [Usage](https://github.com/ECSIM/gopem#usage)
   * [Issues & Bug Reports](https://github.com/ECSIM/gopem#issues--bug-reports)
   * [Contribution](https://github.com/ECSIM/gopem/blob/master/.github/CONTRIBUTING.md)
   * [Dependencies](https://github.com/ECSIM/gopem#dependencies)
   * [Thanks](https://github.com/ECSIM/gopem#thanks)
   * [Cite](https://github.com/ECSIM/gopem#cite)
   * [Authors](https://github.com/ECSIM/gopem/blob/master/AUTHORS.md)
   * [License](https://github.com/ECSIM/gopem/blob/master/LICENSE)
   * [Show Your Support](https://github.com/ECSIM/gopem#show-your-support)
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
		<td align="center">CI</td>
		<td align="center"><img src="https://github.com/ECSIM/gopem/workflows/CI/badge.svg?branch=master"></td>
		<td align="center"><img src="https://github.com/ECSIM/gopem/workflows/CI/badge.svg?branch=develop"></td>
	</tr>
</table>

<table>
	<tr> 
		<td align="center">Code Quality</td>
		<td align="center"><a href="https://www.codefactor.io/repository/github/ecsim/gopem"><img src="https://www.codefactor.io/repository/github/ecsim/gopem/badge" alt="CodeFactor" /></a></td>
		<td align="center"><a href="https://www.codacy.com/gh/ECSIM/gopem/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ECSIM/gopem&amp;utm_campaign=Badge_Grade"><img src="https://app.codacy.com/project/badge/Grade/1ab9a56a65414c2f9b0b7d9ec127ea9f"/></a></td>
	</tr>
</table>

## Installation	

### Source Code
- Download and install [Python3.x](https://www.python.org/downloads/) (>=3.6)
	- [x] Select `Add to PATH` option
	- [x] Select `Install pip` option
- Download [Version 0.7](https://github.com/ecsim/gopem/archive/v0.7.zip) or [Latest Source ](https://github.com/ecsim/gopem/archive/develop.zip)
- Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt` (Need root access)
- Run `python3 setup.py install` or `python setup.py install` (Need root access)				

### PyPI


- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- Run `pip install gopem` or `pip3 install gopem` (Need root access)

### Easy Install

- Run `easy_install --upgrade gopem` (Need root access)


### Exe Version (Only Windows)
- Download [Installer-Version 0.7](https://github.com/ECSIM/gopem/releases/download/v0.7/GOPEM-0.7.exe) or [Portable-Version 0.7](https://github.com/ECSIM/gopem/releases/download/v0.7/GOPEM-Portable-0.7.exe)
- Run and install

⚠️ The portable build is slower to start

### DMG Version (MacOS)
- Download [DMG-Version 0.7](https://github.com/ECSIM/gopem/releases/download/v0.7/GOPEM-0.7.dmg)
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

<img src="https://github.com/ECSIM/gopem/raw/master/rsrc/GOPEM.gif">
<p>GIF</p>

<img src="https://github.com/ECSIM/gopem/raw/master/rsrc/SS1.png">
<p>Screenshot 1</p>

<img src="https://github.com/ECSIM/gopem/raw/master/rsrc/SS2.png">
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

You can also join our discord server			

<a href="https://discord.gg/mgpwvEuBxZ">
  <img src="https://img.shields.io/discord/1006472275920425012.svg?style=for-the-badge" alt="Discord Channel">
</a>


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
* [Zahra Mobasher](https://www.instagram.com/littleblackoyster/?hl=en) (Logo design)



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


## Show Your Support			

<h3>Star This Repo</h3>					

Give a ⭐️ if this project helped you! 


<h3>Donate to Our Project</h3>  
								
If you do like our project and we hope that you do, can you please support us? Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do ;-) .

<a href="https://www.ecsim.ir/opem/donate.html" target="_blank"><img src="http://www.ecsim.ir/images/Donate-Button.png" height="90px" width="270px" alt="OPEM Donation"></a>
