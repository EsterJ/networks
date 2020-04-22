import argparse
from networks import Network, get_params_from_file
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from PIL import Image

parser = argparse.ArgumentParser(description='Uses mnist nework to classify a png image')
parser.add_argument('--imagePath', default=(str(Path.home())) + '/Downloads/pixil-frame-0.png')
parser.add_argument('--networkPath', default='outputs/network.pkl')

args = parser.parse_args()
imagePath = args.imagePath
networkPath = args.networkPath

# load network
parameters = get_params_from_file(networkPath)
my_network = Network(*parameters, 'classification')

# load image
img = Image.open(imagePath)
img.thumbnail((28, 28), Image.ANTIALIAS)
img = np.asarray(img)
img_array = img/255  # rescale to between 0 and 1
img_array = 1 - img_array
img_array = img_array[:, :, 0]  # image should be greyscale, pick only one channel

network_input = img_array.reshape([-1, 1])  # reshapes image to 1d numpy array to feed into network
network_output = my_network.activate(network_input)
network_output = np.ravel(network_output)
x = np.arange(10)  # x labels

plt.subplot(121)
imgplot = plt.imshow(img_array)#, interpolation='bicubic')

plt.subplot(122)
plt.bar(x, network_output)
plt.xticks(x)
plt.ylim(top=1)

plt.show()
