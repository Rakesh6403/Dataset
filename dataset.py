from simple_image_download import simple_image_download as simp

# Instantiate the simple_image_download object
my_downloader = simp.simple_image_download()

# Set the desired file extension for downloaded images (if needed)
# Example: my_downloader.extensions = ['.jpg', '.png']

# Define the keyword(s) for the dataset
keyword = 'cat'

# Specify the number of images to download (limit)
limit = 150

# Download the images
my_downloader.download(keyword, limit)
