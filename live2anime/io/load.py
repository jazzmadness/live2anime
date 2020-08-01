# load, split and scale the maps dataset ready for training
import glob
import numpy as np
from keras.preprocessing.image import img_to_array, load_img

# load all images in a directory into memory
def load_images(path, suffix, size=(256,256)):
	pixel_list = list()
	# enumerate filenames in directory, assume all are images
	for filename in glob.glob(path + '*.png'):
		# load and resize the image
		pixels = load_img(filename, target_size=size)
		# convert to numpy array
		pixels = img_to_array(pixels)
		#appending to list
		pixel_list.append(pixels)
	return np.asarray(pixel_list)

# load and prepare training images
def load_real_samples(filename):
	# load compressed arrays
	data = np.load(filename)
	# unpack arrays
	X1, X2 = data['arr_0'], data['arr_1']
	# scale from [0,255] to [-1,1]
	X1 = (X1 - 127.5) / 127.5
	X2 = (X2 - 127.5) / 127.5
	return [X1, X2]
