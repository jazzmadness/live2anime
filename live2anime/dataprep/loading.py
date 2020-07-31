#for real, all this is from https://machinelearningmastery.com/how-to-develop-a-pix2pix-gan-for-image-to-image-translation/

# load, split and scale the maps dataset ready for training
from os import listdir
from numpy import asarray
from numpy import vstack
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img

# load all images in a directory into memory
def load_images(path, size=(256,512)):
	pixel_list = list()
	# enumerate filenames in directory, assume all are images
	for filename in listdir(path):
		# load and resize the image
		pixels = load_img(path + filename, target_size=size)
		# convert to numpy array
		pixels = img_to_array(pixels)
		#appending to list
		pixel_list.append(pixels)
	return asarray(pixels_list)
