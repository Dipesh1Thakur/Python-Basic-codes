# This program displays a simple line graph
import matplotlib.pyplot as plt

def main():
# create lists with the X and Y coordinates of each data point
    x_coords=[0,1,2,3,4]
    y_coords=[0,3,1,5,2]

# Build the line graph 
    plt.plot(x_coords,y_coords)

    # Add a title .
    plt.title("Sample Data")

    # Add labels to the axes
    plt.xlabel("This is the X axix")
    plt.ylabel("This is the Y axix")

    # Set the axix limits 
    plt.xlim(xmin=-1,xmax=10)
    plt.ylim(ymin=-1,ymax=6)

    # add a grid 
    plt.grid(True)

    # display the line graph
    plt.show()

# call  the main function

main()