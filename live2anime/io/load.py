# load, split and scale the maps dataset ready for training
import glob
import numpy as np
from keras.preprocessing.image import img_to_array, load_img

# load all images in a directory into memory
def load_images(path, size=(256, 256)):
	pixel_list_an = list()
	pixel_list_lv_a = list()

	# getting list of anime pictures, and its respective live action ones
	filename_anime = glob.glob(path + '*_anime*.png')
	filename_anime = filename_anime + glob.glob(path + '*_manga*.png')
	filename_anime = sorted(filename_anime)

	# initializing live action list
	filename_live_action = list()

	for f in filename_anime:
	    # only keeps name and number id (if it has)
	    raw_name = (f
	             .split('/')[2]
	             .split('.')[0]
	             .replace('_anime', '')
	             .replace('_manga', '')
	             )
	    # checking if it has number id, because it has to be used to match the
	    # respective id from the live action pictures
	    is_comp = 0
	    for idx, val in enumerate(raw_name):
	        if val.isdigit():
	            # if it has a digit on the last character, maybe it is a
	            # numbered picture
	            if (len(raw_name) - 1) - idx == 0:
                	is_comp = 1
	    # if the name is 009, it is a unnumbered picture, so it'll not be
	    # treated here
	    if is_comp and raw_name != '009':
	        # create complete path with wildcards
	        # path + name w/o number + changing anime/manga by live_action +
	        # number id + wildcard with png
	        filename_live_action.append(path +
	                         raw_name.rsplit('_', 1)[0] +
	                         '_live_action_' +
	                         raw_name.rsplit('_', 1)[1] +
	                         '.png')
	    else:
	        # dont need to create logic for number idea
	        filename_live_action.append(path +
	                         raw_name +
	                         '_live_action.png')

	# enumerate filenames in directory
	for an, lv_a in zip(filename_anime, filename_live_action):
		# load and resize the image
		pixels_an = load_img(an, target_size=size)
		# load and resize the image
		pixels_lv_a = load_img(lv_a, target_size=size)
		# convert to numpy array
		pixels_an = img_to_array(pixels_an)
		# convert to numpy array
		pixels_lv_a = img_to_array(pixels_lv_a)
		#appending to list
		pixel_list_an.append(pixels_an)
		#appending to list
		pixel_list_lv_a.append(pixels_lv_a)

	return np.asarray(pixel_list_lv_a), np.asarray(pixel_list_an)

# load single image
def load_image(filename, size=(256,256)):
	# load image with the preferred size
	pixels = load_img(filename, target_size=size)
	# convert to numpy array
	pixels = img_to_array(pixels)
	# scale from [0,255] to [-1,1]
	pixels = (pixels - 127.5) / 127.5
	# reshape to 1 sample
	pixels = np.expand_dims(pixels, 0)
	return pixels

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
