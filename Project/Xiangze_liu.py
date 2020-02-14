
from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


x_data = "ProductType"
y_data = "Total Amount"

def lineplot(x_data, y_data, x_label="Product Type", y_label="Total Amount", title="Sales"):
    __, ax = plt.subplots()

    ax.plot(x_data, y_data, lw=3, color ='#539caf', alpha =1)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

lineplot(x_data, y_data)
line, = ax.plot([1, 2, 3], label='Inline label')
ax.legend()
