# AC-Code Analyzer

This code was created to help in the analysis of TFT devices. 

## Authors

Created by 
- Hugo Oliveira (hdesouzaoliveira@unibz.it)
- Niloofar Saeedzadeh Khaanghah (nsaeedzadehkhaanghah@unibz.it)

## How to use 

#### In Microsoft Windows

#### Pre-Requisites

- Before running, make sure you have python installed. If not, go to https://www.python.org/ and download the python installer. 
- Make sure to add python to the PATH variable during the installation (Very Important)
- After installing open the Command Prompt and type `python --version`. If it returns the version of python that is installed, then everything is ok.
- Now, you have to install the libraries to make the code run. Type in the command prompt `pip install numpy pandas matplotlib scipy cmath`

__Note: I know... I know... there are many ways of installing python and the Conda distribution might be a good shot. However, I dont like how Conda integrates with the PATH variable in linux and windows. So I prefer to install in the traditional way, as I described before. If you have enough knowledge, just do the way you want.__

#### Getting the Code

- If you know how to use GIT, just clone this project to the folder where the TFT measurements are separated in folders (Check Below).
- If you do not use Git (Make you life easier and check out how to use it), you can just download this code in a zip file and unzip in the folder you have the the TFT measurements are separated in folders (Check Below).

#### Organization of the folder. 

- In the main folder, you must have the folders of each measurement. For example, lets sayt that your main folder is `C:\User\Main_Folder`. 
- Inside this main folder you will have the TFT folders. For example:
 `C:\User\Main_Folder\TFT_1\`
 `C:\User\Main_Folder\TFT_2\`
 `C:\User\Main_Folder\TFT_3\`
`...` 
- Inside the TFT folder, you need to the CSV files, such as 11.CSV, 22.CSV..ect.
### In GNU Linux

If you run linux, most probabily you already know what to do. If not, install python using the package manager of your Linux Distribution.
For example:
- For Debian-based Distros:
`sudo apt install python3`
- For Arch-based Distros:
- `sudo pacman -S python`
- For Fedora:
- `sudo dnf install python`

Depending on the distribuition the pip package manager might not be installed. Check the documentation of your distro on how to install it. Then, just type `pip install numpy pandas matplotlib scipy cmath`

## Running the code 
 -  Now that you have everything settled, enter in the main folder with the command promprt, and typy `python Code_analyzer.py`

## What to Expect
The code will: 
- Identify the TFT folders.
- Get all the CSV data and make all the transformations.
- Create a folder named Results inside the main folder 
- Save the Data and Chart tables with all the analysis in the Results folder.
- Create a folder named Graphs in the main folder 
- Save all the graphs (Gain, Smith Chart, and Parameters) inside the Graphs folder.

#### Note: This is an ongoing code, I will add mode features in the future.
