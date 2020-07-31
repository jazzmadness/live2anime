import numpy as np
from matplotlib import pyplot
from dataprep.loading import load_images
# dataset path
path = '../data/png_files/'
# load dataset
images = load_images(path)
print('Loaded: ', images.shape)

# save as compressed numpy array
filename = '../data/npz_files/pictures.npz'
np.savez_compressed(filename, images)
print('Saved dataset: ', filename)

# load the prepared dataset
# load the dataset
data = np.load('../data/npz_files/pictures.npz')
images = data['arr_0']
print('Loaded: ', images.shape)
# plot images
n_samples = 3
for i in range(n_samples):
	pyplot.subplot(1, n_samples, 1 + i) #1 row, 3 columns, index from 1 to 3
	pyplot.axis('off')
	pyplot.imshow(images[i].astype('uint8'))
