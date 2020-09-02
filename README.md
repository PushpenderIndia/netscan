<p align="center">
  <img src="https://github.com/PushpenderIndia/netscan/blob/master/img/netscan-logo.png" width=543 height=175 alt="NetScan Logo"/>
</p>


<p align="center">
    <a href="https://python.org">
    <img src="https://img.shields.io/badge/Python-3.7-green.svg">
  </a>
  <a href="https://github.com/PushpenderIndia/technowhorse/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/License-BSD%203-lightgrey.svg">
  </a>
  <a href="https://github.com/PushpenderIndia/technowhorse/releases">
    <img src="https://img.shields.io/badge/Release-1.0-blue.svg">
  </a>
    <a href="https://github.com/PushpenderIndia/technowhorse">
    <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-brightgreen.svg">
  </a>
</p>

NetScan is a Network Reconnaissance Tool for Windows/Linux/OSx  etc Written in Python 3.

## Disclaimer
<p align="center">
  :computer: This project was created only for good purposes and personal use.
</p>

THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE THIS SOFTWARE AT YOUR OWN RISK. THE USE IS COMPLETE RESPONSIBILITY OF THE END-USER. THE DEVELOPERS ASSUME NO LIABILITY AND ARE NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE CAUSED BY THIS PROGRAM.

### Why would be need a another Network Scanner when there is netdiscover?

Answer is quite simple, it is because that netdiscover is not OS independent like NetScan and it works on linus only.
This NetScan is purely written in python 3 and hence has no dependencies other that few python modules which can easily installed.

## Main Goal of Developing this tool

There are very few pentesting tools available which are available for windows.
Developing tools in pure python programming enables us to run that script/tool on any system.
Hence I decided to develop a tool completely from scratch which can be used as alternative of netdiscover

## Features
- [x] Works on Windows/Linux/OSx etc
- [x] Simple, Easy to use
- [x] Can Even run smoothly on Raspberry Pi/Arduino with 512mb ram
- [x] Good UI

## Tested On
[![Kali)](https://www.google.com/s2/favicons?domain=https://www.kali.org/)](https://www.kali.org) **Kali Linux - ROLLING EDITION**

[![Windows)](https://www.google.com/s2/favicons?domain=https://www.microsoft.com/en-in/windows/)](https://www.microsoft.com/en-in/windows/) **Windows 8.1 - Pro**

[![Windows)](https://www.google.com/s2/favicons?domain=https://www.microsoft.com/en-in/windows/)](https://www.microsoft.com/en-in/windows/) **Windows 7 - Ultimate**

## Prerequisite
- [x] Python 3.X
- [x] Few External Modules

## How To Use in Linux
```bash
# Install dependencies 
$ Install latest python 3.x

# Clone this repository
$ git clone https://github.com/PushpenderIndia/netscan.git

# Go into the repository
$ cd netscan

# Installing dependencies
$ python -m pip install scapy==2.4.3 pyfiglet

$ chmod +x netscan.py
$ ./netscan.py  --help    or   python netscan.py --help

# Running Script
$ python netscan.py -t 192.168.43.1/24
# OR 
$ python netscan.py --target 192.168.43.1/24

# NetScan takes IP Address or IP range.
```

## How To Use in Windows
```bash
# Install dependencies 
$ Install latest python 3.x

# Clone this repository or Download a ZIP
$ git clone https://github.com/PushpenderIndia/netscan.git

# Go into the repository
$ cd netscan

# Installing dependencies
$ python -m pip install scapy==2.4.3 pyfiglet

$ chmod +x netscan.py
$ ./netscan.py  --help    or   python netscan.py --help

# Running Script
$ python netscan.py -t 192.168.43.1/24
# OR 
$ python netscan.py --target 192.168.43.1/24

# NetScan takes IP Address or IP range.
```

## Note

Procedure is exactly same for all OS

## Screenshots:

#### Getting Help
![](/img/1.getting_help.PNG)

#### Running netscan.py Script
![](/img/2.runing_script.PNG)

## Contribute

* All Contributors are welcome, this repo needs contributors who will improve this tool to make it best.

## TODO

- [ ] Add New features
- [ ] Contribute GUI Version

## Contact

singhpushpender250@gmail.com 

## Buy Me A Coffee

* Support my Open Source projects by making Donation, It really motivates me to work on more projects
* PayPal Email: `shrisatender@gmail.com` [**Please Don't Send Emails to This Address**]
