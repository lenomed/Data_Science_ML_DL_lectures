import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
tips = sns.load_dataset("tips")
print(tips.head())

sns.displot(tips['total_bill'], kde=True, bins=50)
plt.show()
#joinplot() helps you to join two distplots together

sns.jointplot(x='total_bill', y='tip', kind='scatter', data=tips)# you cnn input hex,kde,reg in kind= '
plt.tight_layout
plt.show()
# pairplot creates a grid of plots showing how every variable relates to every other variable.

sns.pairplot(tips, hue='sex',  palette='coolwarm')
plt.show()

# using the rugplot to explain what the kde that we saw earlier is
#kde stands for kernel density estimation plots
sns.rugplot(tips['total_bill'])
plt.show()
# Create dataset
dataset = np.random.randn(25)

# Create another rugplot
sns.rugplot(dataset);

# Set up the x-axis for the plot
x_min = dataset.min() - 2
x_max = dataset.max() + 2

# 100 equally spaced points from x_min to x_max
x_axis = np.linspace(x_min, x_max, 100)

# Set up the bandwidth, for info on this:
url = 'http://en.wikipedia.org/wiki/Kernel_density_estimation#Practical_estimation_of_the_bandwidth'

bandwidth = ((4 * dataset.std() ** 5) / (3 * len(dataset))) ** .2

# Create an empty kernel list
kernel_list = []

# Plot each basis function
for data_point in dataset:
    # Create a kernel for each point and append to list
    kernel = stats.norm(data_point, bandwidth).pdf(x_axis)
    kernel_list.append(kernel)

    # Scale for plotting
    kernel = kernel / kernel.max()
    kernel = kernel * .4
    plt.plot(x_axis, kernel, color='grey', alpha=0.5)

plt.ylim(0, 1)
plt.show()

# To get the kde plot we can sum these basis functions.

# Plot the sum of the basis function
sum_of_kde = np.sum(kernel_list,axis=0)

# Plot figure
fig = plt.plot(x_axis,sum_of_kde,color='indianred')

# Add the initial rugplot
sns.rugplot(dataset,c = 'indianred')

# Get rid of y-tick marks
plt.yticks([])

# Set title
plt.suptitle("Sum of the Basis Functions")
plt.show()

# you can use the kdeplot instead of the distribution of the plots

sns.kdeplot(tips['total_bill'])
plt.show()