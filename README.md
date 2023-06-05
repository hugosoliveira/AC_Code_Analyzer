# AC-Code Analyzer

This code was created to help in the analysis of TFT devices. 

## Authors

Created by Hugo Oliveira (hdesouzaoliveira@unibz.it)
Niloofar Saeedzadeh (nsaeedzadehkhaanghah@unibz.it)

## In Microsoft Windows

### Pre-Requisites

- Before running, make sure you have python installed. If not, go to https://www.python.org/ and download the python installer. 
- Make sure to add python to the PATH variable during the installation (Very Important)
- After installing open the Command Prompt and type `python --version`. If it returns the version of python that is installed, then everything is of.
- Now, you have to install the libraries to make the code run. Type in the command prompt `pip install numpy pandas matplotlib scipy cmath`

### Getting the Code

- If you know to to use GIT, just clone this project to the folder where the TFT measurements are separated in folders (Check Below)
- If you do not use GIt (Make you life easier and learn it), you cna just download this code in a zip file and unzip in the folder you have the the TFT measurements are separated in folders (Check Below)

### Organization of the folder. 

- In the main folder, you must have the folders of each measurement. For example, lets sayt that your main folder is `C:\User\Main_Folder`. 
- Inside this main folder you will have the TFT folders. For example:
 `C:\User\Main_Folder\TFT_1\`
 `C:\User\Main_Folder\TFT_2\`
 `C:\User\Main_Folder\TFT_3\`
`...` 
- Inside the TFT folder, you need to the CSV files, such as 11.CSV, 22.CSV..ect.

### Running the code 
 -  Now that you have everything settled, ente in the main folder with the command promprt, and typy `python Code_analyzer.py`

### What to Expect
- The code will identify the TFT folders
- Get all the CSV data and make all the transformations
- Create a folder named Results inside the manin folder and save there the Data and Chart tables with all the analysis.
- Create a folder named Graphs in the main folder with all the graphs (Gain, Smith Chart, and Parameters)

#### Note: This is an ongoing code, I will add mode features in the future.
