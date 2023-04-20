import os
import matplotlib.pyplot as plt

# Define a directory containing the images
image_dir = './images/'

# Get a list of the image files in the directory
image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]

# Create a figure with a grid of plots
fig, axs = plt.subplots(nrows=1, ncols=len(image_files), figsize=(10, 5))

# Load and display each image in a plot
for i, file in enumerate(image_files):
    img = plt.imread(os.path.join(image_dir, file))
    axs[i].imshow(img)
    axs[i].set_title(file)

# Remove the axis labels
for ax in axs:
    ax.axis('off')

# Show the plots
plt.show()
p