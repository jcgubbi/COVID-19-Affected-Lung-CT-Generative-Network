from numpy import asarray
from numpy import vstack
from numpy.random import randn
from numpy.random import randint
from numpy import linspace
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt

''' Code adapted from: https://machinelearningmastery.com/how-to-interpolate-and-perform-vector-arithmetic-with-faces-using-a-generative-adversarial-network/'''

# uniform interpolation between two points
# linear interpolation
def interpolate_points(p1, p2, n_steps=10):
	# interpolate ratios between the points
	ratios = linspace(0, 1, num=n_steps)
	# linear interpolate vectors
	vectors = list()
	for ratio in ratios:
		v = (1.0 - ratio) * p1 + ratio * p2
		vectors.append(v)
	return asarray(vectors)
 
 # create a plot of generated images
def plot_generated(examples, n):
	# plot images with larger figure size
	plt.figure(figsize=(16.8,18.4))
	for i in range(n):
		plt.subplot(n, n, 1 + i)
		plt.axis('off')
		plt.title(str(i))
		plt.imshow(examples[i, :, :,0], cmap='gray')
	plt.show()

'''Model the progression from a starting CT scan to an ending CT scan'''
def model_progression(generator, start, end, steps=10, display=10): 
	'''
	generator: provide a generator function from GAN
	start: starting image
	end: ending image
	steps: how many steps of the progression to calculate
	display: how many steps of the progression to display
	
	**This uses linear interpolation**
	
	'''
	# use two images - start and end
	n=2
	pts = np.concatenate((start, end))
	# interpolate pairs
	results = None
	for i in range(0, n, 2):
		interpolated = interpolate_points(pts[i], pts[i+1], steps)
		# generate images based on interpolated noise
		X = generator.predict(interpolated)
		# scale from [-1,1] to [0,1]
		X = (X + 1) / 2.0
		if results is None:
			results = X
		else:
			results = vstack((results, X))
	
	plot_generated(results,display)

