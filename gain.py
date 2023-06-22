import matplotlib.pyplot as plt

def plots(all_data_df, name, main_folder):

    # Create a figure with subplots arranged in a 2x2 grid
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
    fig.suptitle('Folder: ' + name, fontsize=16)

    # Define the columns to plot (adjust as per your column names)
    columns = ['Smoothed_MAG21', 'Smoothed_Im_1/H21', 'Smoothed_MSG', 'Smoothed_GTU']
    curves_names = ['Current Gain h21 (dB)', 'Imaginary 1/h21', 'Maximum Stable Gain (dB)', 'Unilateral Gain (dB)']

    # Iterate over the subplots and plot the curves
    for i, ax in enumerate(axes.flatten()):
        # Get the column name for the curve in the current subplot
        column = columns[i]
        curve_n = curves_names[i]
        
        # Plot the curve in the current subplot
        ax.plot(all_data_df['Freq']/1E6, all_data_df[column], color='red')
        ax.set_ylabel(curve_n)
        
        # Set x-axis scale to logarithmic for the first graph of the first row and the two graphs of the second row
        if (i == 0) or (i >= 2):
            ax.set_xscale('log')
        
        ax.set_xlabel('Frequency (MHz)')
        
        # Add a black line at y=0
        ax.axhline(0, color='black', linestyle='-')
        
        # Tick inside the Graph
        ax.tick_params(axis='both', direction='in')

    # Adjust spacing between subplots
    plt.tight_layout()
    
    # Save the plot
    plt.savefig(main_folder + '\\' + 'Graphs' + '\\' + 'Gain_'+ name +'.pdf', dpi=300, bbox_inches='tight')
    plt.savefig(main_folder + '\\' + 'Graphs' + '\\' + 'Gain_'+ name +'.svg', dpi=300, bbox_inches='tight')

    # Show the figure
    # plt.show()

    plt.close()    