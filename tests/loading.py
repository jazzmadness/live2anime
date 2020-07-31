from numpy import load, savez_compressed
from matplotlib import pyplot
from dataprep.loading import load_images
# dataset path
path = '../live2anime/data/png_files/'
# load dataset
images = load_images(path)
print('Loaded: ', images.shape)

# save as compressed numpy array
filename = '../live2anime/data/npz_files/pictures.npz'
savez_compressed(filename, src_images, tar_images)
print('Saved dataset: ', filename)

# load the prepared dataset
# load the dataset
data = load('../live2anime/data/npz_files/pictures.npz')
src_images, tar_images = data['arr_0'], data['arr_1']
print('Loaded: ', src_images.shape, tar_images.shape)
# plot source images
n_samples = 3
for i in range(n_samples):
	pyplot.subplot(2, n_samples, 1 + i)
	pyplot.axis('off')
	pyplot.imshow(src_images[i].astype('uint8'))
# plot target image
for i in range(n_samples):
	pyplot.subplot(2, n_samples, 1 + n_samples + i)
	pyplot.axis('off')
	pyplot.imshow(tar_images[i].astype('uint8'))
pyplot.show()
