# This program display a simple bar chart
import matplotlib.pyplot as plt

def main():
    # create a list with the x coordinates of each bars left edge
    left_edges=[0,10,20,30,40]

    #create a list withh the heights of each bar 
    heights=[100,200,300,400,500]

    # create bar width
    bar_width=5
    
    #give color
    plt.bar(left_edges, heights, bar_width,color=('r','g','b','w','k'))

    #build the bar chart
    plt.bar(left_edges,heights,bar_width)

    plt.show()

main()