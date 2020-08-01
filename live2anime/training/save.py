import numpy as np
from matplotlib import pyplot
from live2anime.io.load import load_images

# dataset path
path = 'data/png_files/'
# load dataset
images_live_action, images_anime = load_images(path)
print('Loaded: ', images_live_action.shape, images_anime.shape)

# save as compressed numpy array
filename = 'data/npz_files/pictures.npz'
np.savez_compressed(filename, images_live_action, images_anime)
print('Saved dataset: ', filename)
