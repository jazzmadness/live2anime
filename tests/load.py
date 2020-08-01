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

# load the prepared dataset
# load the dataset
data = np.load('data/npz_files/pictures.npz')
images_live_action, images_anime = data['arr_0'], data['arr_1']
print('Loaded: ', images_live_action.shape, images_anime.shape)
# plot source images
n_samples = 3
for i in range(n_samples):
	pyplot.subplot(2, n_samples, 1 + i)
	pyplot.axis('off')
	pyplot.imshow(images_live_action[i].astype('uint8'))
# plot target image
for i in range(n_samples):
	pyplot.subplot(2, n_samples, 1 + n_samples + i)
	pyplot.axis('off')
	pyplot.imshow(images_anime[i].astype('uint8'))
pyplot.show()
