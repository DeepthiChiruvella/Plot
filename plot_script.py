# Filename: plot_script.py

# Import the required library for plotting
import matplotlib.pyplot as plt

# Import the sys module to access command line arguments
import sys

# Function to plot a basic line graph and save it as an image file
def plot_basic_line(x, y, output_file):
    # Plot the data points
    plt.plot(x, y)
    
    # Label for the X-axis
    plt.xlabel('X-axis label')

    # Label for the Y-axis
    plt.ylabel('Y-axis label')

    # Title for the plot
    plt.title('Basic Line Plot')

    # Save the plot as an image file with the specified name
    plt.savefig(output_file)

    # Display the plot
    plt.show()

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Example data for X and Y axes
    x_data = [1, 2, 3, 4, 5]
    y_data = [2, 4, 6, 8, 10]

    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        # Print usage instructions and exit with an error code
        print("Usage: python plot_script.py <output_file.png>")
        sys.exit(1)

    # Get the output file name from the command line argument
    output_file_name = sys.argv[1]

    # Call the function to plot the data and save the plot as an image file
    plot_basic_line(x_data, y_data, output_file_name)
