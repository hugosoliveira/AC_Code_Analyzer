import pandas as pd
import numpy as np
from scipy.signal import savgol_filter

def transformations(all_data_df):

    # Calculate the MSG(db)

    division_results = all_data_df['S21_modulus'].values / all_data_df['S12_modulus'].values
    log_results = 10 * np.log10(division_results)
    msg = pd.DataFrame(log_results, columns=['MSG'])
    all_data_df = pd.concat([all_data_df, msg], axis=1)

    # Calculate the GTU(db)

    multiplication_1 = all_data_df['S21_modulus'].values * all_data_df['S21_modulus'].values
    multiplication_2 = (1-all_data_df['S11_modulus'].values * all_data_df['S11_modulus'].values)*(1-all_data_df['S22_modulus'].values * all_data_df['S22_modulus'].values)
    division = multiplication_1 / multiplication_2
    #Make a note here anout the problem with the positive numbers
    positive_numbers = list(map(abs, division)) # this is not done in the origin file. 
    final_calc = 10 * np.log10(positive_numbers)
    gtu = pd.DataFrame(final_calc, columns=['GTU'])
    all_data_df = pd.concat([all_data_df, gtu], axis=1)

    # Calculate the H21

    multiplication_1 = (1-all_data_df['S11_complex_number'].values)*(1+all_data_df['S22_complex_number'].values)
    multiplication_2 = (all_data_df['S12_complex_number'].values)*(all_data_df['S21_complex_number'].values)
    numerator = -2 * all_data_df['S21_complex_number'].values
    division = numerator / (multiplication_1 + multiplication_2)
    h21 = pd.DataFrame(division, columns=['H21'])
    all_data_df = pd.concat([all_data_df, h21], axis=1)
    
    # Calculate Mag H21

    mag_h21 = pd.DataFrame({'MAG21': 20*np.log10(h21['H21'].apply(abs))})
    all_data_df = pd.concat([all_data_df, mag_h21], axis=1)

    # Canculate the Im (1/H21)

    div_imaginary = pd.DataFrame({'Im_1/H21': np.imag(1 / h21['H21'])})
    all_data_df = pd.concat([all_data_df, div_imaginary], axis=1)

# ---------------------------- SMOOTHING DATA-------------------------

    # Smoothing MSG Data using Adjacent-Avaraging
    window_size = 25
    polynomial_order = 1
    all_data_df['Smoothed_MSG'] = savgol_filter(all_data_df['MSG'], window_size, polynomial_order)

    # Smoothing GTU Data using Savgov Filter
    window_size = 25
    polynomial_order = 1
    all_data_df['Smoothed_GTU'] = savgol_filter(all_data_df['GTU'], window_size, polynomial_order)

    # Smoothing MAG21 Data using Savgov Filter
    window_size = 25
    polynomial_order = 1
    all_data_df['Smoothed_MAG21'] = savgol_filter(all_data_df['MAG21'], window_size, polynomial_order)

    # Smoothing Im_1/H21 Data using Savgov Filter
    window_size = 25
    polynomial_order = 2
    all_data_df['Smoothed_Im_1/H21'] = savgol_filter(all_data_df['Im_1/H21'], window_size, polynomial_order)

    return all_data_df