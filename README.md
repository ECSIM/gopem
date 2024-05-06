<div align="center">
	<img src="https://github.com/ECSIM/gopem/raw/master/rsrc/logo.png" width=320px>
	<br>
	<a href="https://www.python.org/"><img src="https://img.shields.io/badge/built%20with-Python3-green.svg" alt="built with Python3"></a>
	<a href="https://badge.fury.io/py/gopem"><img src="https://badge.fury.io/py/gopem.svg" alt="PyPI version" height="18"></a>
	<a href="https://discord.gg/mgpwvEuBxZ"><img src="https://img.shields.io/discord/1006472275920425012.svg" alt="Discord Channel"></a>
</div>

--------

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
		<td align="center"><img src="https://github.com/ECSIM/gopem/actions/workflows/test.yml/badge.svg?branch=master"></td>
		<td align="center"><img src="https://github.com/ECSIM/gopem/actions/workflows/test.yml/badge.svg?branch=develop"></td>
	</tr>
</table>

<table>
	<tr> 
		<td align="center">Code Quality</td>
		<td align="center"><a href="https://www.codefactor.io/repository/github/ecsim/gopem"><img src="https://www.codefactor.io/repository/github/ecsim/gopem/badge" alt="CodeFactor" /></a></td>
		<td align="center"><a href="https://app.codacy.com/gh/ECSIM/gopem/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade"><img src="https://app.codacy.com/project/badge/Grade/1ab9a56a65414c2f9b0b7d9ec127ea9f"/></a></td>
	</tr>
</table>

## Installation	

### Source Code
- Download and install [Python3.x](https://www.python.org/downloads/) (>=3.6)
	- [x] Select `Add to PATH` option
	- [x] Select `Install pip` option
- Download [Version 0.8](https://github.com/ecsim/gopem/archive/v0.8.zip) or [Latest Source ](https://github.com/ecsim/gopem/archive/develop.zip)
- Run `pip install .`

### PyPI
- Check [Python Packaging User Guide](https://packaging.python.org/installing/)     
- Run `pip install gopem==0.8`


### Exe Version (Only Windows)
- Download [Installer-Version 0.8](https://github.com/ECSIM/gopem/releases/download/v0.8/GOPEM-0.8.exe) or [Portable-Version 0.8](https://github.com/ECSIM/gopem/releases/download/v0.8/GOPEM-Portable-0.8.exe)
- Run and install

⚠️ The portable build is slower to start


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
- Run `gopem` or `python -m gopem` (or run `GOPEM.exe`)
- Wait about 4-15 seconds (depends on your system specification)
- Enter PEM cell parameters (or run standard test vectors)	
- For more information about parameters visit [OPEM (Open Source PEM Fuel Cell Simulation Tool)](https://github.com/ECSIM/opem "OPEM")
## Issues & Bug Reports			

Just fill an issue and describe it. We'll check it ASAP!							
or send an email to [opem@ecsim.site](mailto:opem@ecsim.site "opem@ecsim.site"). 

You can also join our discord server			

<a href="https://discord.gg/mgpwvEuBxZ">
  <img src="https://img.shields.io/discord/1006472275920425012.svg?style=for-the-badge" alt="Discord Channel">
</a>


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

Download [OPEM.bib](http://www.ecsim.site/opem/OPEM.bib)(BibTeX Format)									

<table>
	<tr> 
		<td align="center">JOSS</td>
		<td align="center"><a style="border-width:0" href="https://doi.org/10.21105/joss.00676"><img src="http://joss.theoj.org/papers/10.21105/joss.00676/status.svg" alt="DOI badge" ></a></td>	
	</tr>
	<tr>
		<td align="center">Zenodo</td>
		<td align="center"><a href="https://doi.org/10.5281/zenodo.1133110"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.1133110.svg" alt="DOI"></a></td>
	</tr>
</table>


## Show Your Support			

<h3>Star This Repo</h3>					

Give a ⭐️ if this project helped you! 


<h3>Donate to Our Project</h3>  
								
If you do like our project and we hope that you do, can you please support us? Our project is not and is never going to be working for profit. We need the money just so we can continue doing what we do ;-) .

<a href="https://www.ecsim.site/opem/donate.html" target="_blank"><img src="http://www.ecsim.site/images/Donate-Button.png" height="90px" width="270px" alt="OPEM Donation"></a>
