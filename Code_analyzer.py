""""
     _    ____    ____          _          
    / \  / ___|  / ___|___   __| | ___     
   / _ \| |     | |   / _ \ / _` |/ _ \    
  / ___ \ |___  | |__| (_) | (_| |  __/    
 /_/   \_\____|  \____\___/ \__,_|\___|    
     _                _                    
    / \   _ __   __ _| |_   _ _______ _ __ 
   / _ \ | '_ \ / _` | | | | |_  / _ \ '__|
  / ___ \| | | | (_| | | |_| |/ /  __/ |   
 /_/   \_\_| |_|\__,_|_|\__, /___\___|_|   
                        |___/                                                                           
AC Code Analyzer
Created by Hugo Oliveira and Niloofar Saeedzadeh
hdesouzaoliveira@unibz.it
nsaeedzadehkhaanghah@unibz.it
May 2023                     
"""
import logo as lg
import pandas as pd
import cmath
import os
import transformations as tr
import charts as ct
import parameter as prt
import gain as gn
import smith as smt

art = lg.logo()
print(art)

file_path = os.path.abspath(__file__)
main_folder = os.path.dirname(file_path)
os.chdir(main_folder)

if not os.path.exists('Results'):
    # Create the folder RESULTS if it does not exist
    os.mkdir('Results')

if not os.path.exists('Graphs'):
    # Create the folder RESULTS if it does not exist
    os.mkdir('Graphs')

# Get the folder names to a list
folder_names = [folder for folder in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, folder))]
folder_names = [n for n in folder_names if n != '__pycache__' and n != 'Results' and n != 'Graphs' and n != '.git']

for folder_n in folder_names:
    
    folder_file = main_folder + '\\' + folder_n
    
    print('FOLDER: ', folder_n)

    os.chdir(folder_file)

    # Get the file names to a list
    name_data_acquired = [file for file in os.listdir(folder_file) if file.endswith(".CSV")]
    all_data_df = pd.DataFrame()

    for file_name in name_data_acquired:

        df = pd.read_csv(file_name, delimiter=', ', skiprows=2, engine='python')
        # os.system('cls')

        # print('Folder Name: ', folder_n)
        # print('File: ', file_name)

        file_name = file_name[-6:] # To avoid problems with naming

        df.columns = [''] * len(df.columns)
        df.columns =['Freq', 'x_number', 'y_number']

        complex_numbers = []

        for index, row in df.iterrows():
            # Access the elements in the second and third columns
            element1 = float(row['x_number'])
            element2 = float(row['y_number'])

            # Create a complex number and append it to the list
            complex_num = complex(element1, element2)
            complex_numbers.append(complex_num)

        # Add the column of frequency
        if 'Freq' in all_data_df.columns:
            pass
        else:
            all_data_df.insert(0,'Freq',df['Freq'].values)

        title_column = file_name[:-4] #I am just rmeoving the 4 last characters of the file_name
        all_data_df['S' + title_column + '_complex_number'] = complex_numbers
        all_data_df['S' + title_column + '_modulus'] = list(map(lambda x: abs(x), complex_numbers))
        all_data_df['S' + title_column + '_phase'] = list(map(lambda x: cmath.phase(x), complex_numbers))

    # Calculating MSG, GTU, H21, MagH21, IM(1/H21)
    all_data_df = tr.transformations(all_data_df)

    # Recording the Data to a csv file inside the folder Results
    all_data_df.to_csv( main_folder + '\\' + 'Results' + '\\' + 'Data_'+ folder_n +'.csv', index=False, header=True)

    # Preparing for the charts
    chart_df = ct.charts(all_data_df)

    # Add the column of frequency
    if 'Freq' in chart_df.columns:
        pass
    else:
        chart_df.insert(0,'Freq',all_data_df['Freq'].values)

    # Recording the Chart data to a csv file inside the folder Results
    chart_df.to_csv( main_folder + '\\' + 'Results' + '\\' + 'Chart_'+ folder_n +'.csv', index=False, header=True)


    # ---- MAKING THE PLOTS

    # Making the Plots - Parameters
    prt.plots(chart_df, folder_n, main_folder)

    # Making the Plots - Gain
    gn.plots(all_data_df, folder_n, main_folder)

    # Making the Plots - Smith Chart
    smt.plots(all_data_df, folder_n, main_folder)
