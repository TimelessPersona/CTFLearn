from PIL import Image
import numpy as np

# Let's read the file and parse the data as grayscale pixel values
file_path = 'output.txt'

with open(file_path, 'r') as file:
    data = file.read()

# Split the data into individual values and convert to integers
values = [int(x) for x in data.split() if x.strip()]

# Check if the data length matches 600*600
if len(values) != 256 * 256:
    raise ValueError("Data length does not match 256*256")

# Reshape the data to a 600x600 numpy array
image_data = np.array(values, dtype=np.uint8).reshape((256, 256))

# Create a grayscale image from the numpy array
image = Image.fromarray(image_data, 'L')

# Save the image
image.save('output_image.png')

# Display the image
image.show()
