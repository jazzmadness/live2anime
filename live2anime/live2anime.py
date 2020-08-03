"""Main module."""
import tensorflow as tf
from keras.models import load_model
from matplotlib import pyplot
from live2anime.io.load import load_image

#config for using gpu on tensorflow...https://github.com/tensorflow/tensorflow/issues/24496
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
	try:
		for gpu in gpus:
			tf.config.experimental.set_memory_growth(gpu, True)
	except RuntimeError as e:
		print(e)

def live2anime(img, model_version):
    # load source image
    src_image = load_image(img)
    print('Loaded', src_image.shape)
    # load model
    model = load_model('data/models/model_' + model_version + '.h5')
    # generate image from source
    gen_image = model.predict(src_image)
    # scale from [-1,1] to [0,1]
    gen_image = (gen_image + 1) / 2.0
    # plot the image
    pyplot.imshow(gen_image[0])
    pyplot.axis('off')
    pyplot.show()

#example, running test.png on model version 007900
#live2anime('data/png_files/test.png', '007900')
