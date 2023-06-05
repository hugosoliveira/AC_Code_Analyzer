import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def plots(chart_df, name, main_folder):

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
    fig.suptitle(name, fontsize=16)

    curves = [('Mag_S11_db_smooth', 'Phase_S11_deg_smooth'), ('Mag_S12_db_smooth', 'Phase_S12_deg_smooth'), ('Mag_S21_db_smooth', 'Phase_S21_deg_smooth'), ('Mag_S22_db', 'Phase_S22_deg_smooth')]
    curves_names = [('Magnitude S11 (dB)', 'Phase S11 (°)'), ('Magnitude S12 (dB)', 'Phase S12 (°)'), ('Magnitude S21 (dB)', 'Phase S21 (°)'), ('Magnitude S22 (dB)', 'Phase S22 (°)')]

    # Define the desired x and y ranges
    # x_range = [(0, 400E6), (0, 400E6),(0, 400E6),(0, 400E6)]   # Specify the desired x-axis range
    # y_range = [(-1.75, 0.5), (-75, 5), (-48, 0), (-1.25, 0.75)]  # Specify the desired y-axis range
    # y2_range = [(-16, 1), (-20, 110), (-10, 190), (-18, 2)]  # Specify the desired y-axis range

    

    # Iterate over the subplots and plot the curves
    for i, ax in enumerate(axes.flatten()):
        # Get the column names for the curves in the current subplot
        curve1, curve2 = curves[i]
        curve_n1, curve_n2 = curves_names[i] 
        
        # The first part of the graph (red part)
        ax.plot(chart_df['Freq'], chart_df[curve1], color='red', label=curve1)
        ax.set_ylabel(curve_n1, color='red')
        ax.tick_params(axis='y', labelcolor='red')
        ax.set_xscale('log')    
        # ax.set_xlim(x_range[i])
        # ax.set_ylim(y_range[i])
        # ax.ticklabel_format(style='plain', axis='x')

        # Add a red line at y=0
        ax.axhline(0, color='red', linestyle='--')
        
        # Tick inside the Graph
        ax.tick_params(axis='both', direction='in')
        
        
        # The second part of the graph (blue part)
        ax2 = ax.twinx()
        ax2.plot(chart_df['Freq'], chart_df[curve2], color='blue', label=curve2)
        ax2.set_ylabel(curve_n2, color='blue')
        ax2.tick_params(axis='y', labelcolor='blue')
        ax2.set_xscale('log')
        # ax2.set_ylim(y2_range[i])
        
        # Tick inside the Graph
        ax2.tick_params(axis='both', direction='in')
            
        # Add a red line at y=0
        ax2.axhline(0, color='blue', linestyle='-')
        
        # Set labels and legend for both y-axes
        ax.set_xlabel('Frequency (MHz)')
        lines = ax.get_lines() + ax2.get_lines()

    # Adjust spacing between subplots
    plt.tight_layout()

    # Save the plot
    plt.savefig(main_folder + '\\' + 'Graphs' + '\\' + 'Param_'+ name +'.pdf', dpi=300, bbox_inches='tight')

    # # Show the figure
    plt.show()
