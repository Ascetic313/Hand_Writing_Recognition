import codecademylib3_seaborn
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans

digits = datasets.load_digits()
print(digits.DESCR)
print(digits.data)
print(digits.target)
plt.gray() 
 
plt.matshow(digits.images[100])
 
plt.show()
print(digits.target[100])

model = KMeans(n_clusters=10, random_state=42)
model.fit(digits.data)
fig = plt.figure(figsize=(8,3))
fig.suptitle('Cluser Center Images', fontsize=14, fontweight='bold')


for i in range(10):
 
  # Initialize subplots in a grid of 2X5, at i+1th position
  ax = fig.add_subplot(2, 5, 1 + i)
 
  # Display images
  ax.imshow(model.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
plt.show()