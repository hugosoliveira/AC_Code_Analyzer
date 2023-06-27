import matplotlib.pyplot as plt
import skrf as rf

def plots(all_data_df, name, main_folder):

    # Define the column names for the complex numbers (excluding the 'Frequency' column)
    complex_columns = ['S11_complex_number', 'S12_complex_number', 'S21_complex_number', 'S22_complex_number']
    labels = ['S11','S12','S21','S22', ]
    # Create a figure with subplots arranged in a 2x2 grid
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))
    fig.suptitle('Folder: ' + name, fontsize=16)

    # Iterate over the subplots and plot the Smith charts
    for i, ax in enumerate(axes.flatten()):
        # Get the column name for the complex numbers in the current subplot
        column = complex_columns[i]

        # Transforming the Dataframe into numpy complex array for plotting...Using lambda function
        complex_plot = (all_data_df[column].apply(lambda x: complex(x)) - 1) / (all_data_df[column].apply(lambda x: complex(x)) + 1)

        # Create a Smith chart object for the current subplot
        rf.plotting.plot_smith(complex_plot, ax=ax, draw_labels=True, color='red')
        label_used = labels[i]
        # Set title for the subplot
        ax.set_title(label_used)

    # Adjust spacing between subplots
    plt.tight_layout()

    # Save the plot
    plt.savefig(main_folder + '\\' + 'Graphs' + '\\' + 'Smith_'+ name +'.pdf', dpi=300, bbox_inches='tight')
    plt.savefig(main_folder + '\\' + 'Graphs' + '\\' + 'Smith_'+ name +'.svg', dpi=300, bbox_inches='tight')


    # Show the figure
    # plt.show()
    plt.close()    
