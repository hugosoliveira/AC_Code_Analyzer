import pandas as pd
import numpy as np
from scipy.signal import savgol_filter

def charts(all_data_df):

    chart_df = pd.DataFrame()
    chart_df['Freq'] = all_data_df['Freq']

    chart_df['Mag_S11_db'] = 20 * np.log10(all_data_df['S11_modulus'])
    chart_df['Phase_S11_deg'] = (360/(2*np.pi))*all_data_df['S11_phase']
    chart_df['Mag_S12_db'] = 20 * np.log10(all_data_df['S12_modulus'])
    chart_df['Phase_S12_deg'] = (360/(2*np.pi))*all_data_df['S12_phase']
    chart_df['Mag_S21_db'] = 20 * np.log10(all_data_df['S21_modulus'])
    chart_df['Phase_S21_deg'] = (360/(2*np.pi))*all_data_df['S21_phase']
    chart_df['Mag_S22_db'] = 20 * np.log10(all_data_df['S22_modulus'])
    chart_df['Phase_S22_deg'] = (360/(2*np.pi))*all_data_df['S22_phase']

    window_size = 50
    polynomial_order = 3

    chart_df['Mag_S11_db_smooth'] = savgol_filter(chart_df['Mag_S11_db'], window_size, polynomial_order)
    chart_df['Phase_S11_deg_smooth'] = savgol_filter(chart_df['Phase_S11_deg'], window_size, polynomial_order)
    chart_df['Mag_S12_db_smooth'] = savgol_filter(chart_df['Mag_S12_db'], window_size, polynomial_order)
    chart_df['Phase_S12_deg_smooth'] = savgol_filter(chart_df['Phase_S12_deg'], window_size, polynomial_order)
    chart_df['Mag_S21_db_smooth'] = savgol_filter(chart_df['Mag_S21_db'], window_size, polynomial_order)
    chart_df['Phase_S21_deg_smooth'] = savgol_filter(chart_df['Phase_S21_deg'], window_size, polynomial_order)
    chart_df['Mag_S22_db_smooth'] = savgol_filter(chart_df['Mag_S22_db'], window_size, polynomial_order)
    chart_df['Phase_S22_deg_smooth'] = savgol_filter(chart_df['Phase_S22_deg'], window_size, polynomial_order)

    return chart_df