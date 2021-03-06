#!/usr/bin/env python

import matplotlib.pyplot as plt
import json
import pickle


with open('../params.json') as f:
    params = json.load(f)


rows = 2
cols = params['layers'][1]['map_num'] // rows

with open('../output/weights_layer_1.pickle', 'rb') as f:
    w = pickle.load(f)
w = w.reshape((params['layers'][1]['sec_num'], params['layers'][1]['map_num'], params['layers'][1]['win'][0], params['layers'][1]['win'][1]))

plt.figure(figsize=(7.5, 3.5))
for j in range(params['layers'][1]['map_num']):
    plt.subplot(rows, cols, j + 1)
    plt.axis('off')
    plt.imshow(w[5][j].transpose(), interpolation="nearest", vmin=0, vmax=1)

plt.savefig('weights.png')
plt.show()
