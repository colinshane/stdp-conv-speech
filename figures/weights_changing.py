#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as image
import json
import pickle


with open('../params.json') as f:
    params = json.load(f)

m = 3  # features
n = 12 # time points
fig, axes = plt.subplots(m, n, figsize=(4.5, 4.5))

for i in range(n):
    with open('../output/weights_layer_1_{}.pickle'.format(i * 2000), 'rb') as f:
        w = pickle.load(f)
    w = w.reshape((params['layers'][1]['sec_num'], params['layers'][1]['map_num'], params['layers'][1]['win'][0], params['layers'][1]['win'][1]))
    axes[0, i].axis('off')
    axes[0, i].imshow(w[5][2].transpose(), interpolation="nearest", vmin=0, vmax=1)
    axes[1, i].axis('off')
    axes[1, i].imshow(w[5][6].transpose(), interpolation="nearest", vmin=0, vmax=1)
    axes[2, i].axis('off')
    axes[2, i].imshow(w[5][34].transpose(), interpolation="nearest", vmin=0, vmax=1)
    # axes[2, i].text(0, 43, i * 2000)

fig.tight_layout(pad=0)
fig.savefig('weights_changing.png')
img = image.imread('weights_changing.png')

fig, axes = plt.subplots()
axes.imshow(img)
axes.set_xlim([0, 1400])
axes.set_ylim([1350, -50])
axes.set_xticks([x for x in range(85, 1400, 112)])
axes.set_xticklabels([x*2000 for x in range(12)], rotation=30)
axes.set_yticks([])
# axes.set_yticks([200, 650, 1100])
# axes.set_yticklabels([2, 6, 34])
axes.set_xlabel('Number of training samples')
axes.set_ylabel('Three selected feature maps')

fig.savefig('weights_changing.png')
plt.show()
