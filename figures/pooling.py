#!/usr/bin/env python

import pickle
import numpy as np
import matplotlib.pyplot as plt


with open('../output/output_test_set.pickle', 'rb') as f:
    test_set = pickle.load(f)

fig, axes = plt.subplots(5, 2, figsize=(4.5, 4))

for i in range(10):
    idxes = np.where(test_set[1] == i)[0]
    idx = idxes[0]
    ax = axes.ravel()[i]
    ax.imshow(test_set[0][idx].reshape((50, 9)).transpose())
    ax.axis('off')
    ax.set_title('Digit ' + str(i))

axes[4, 0].arrow(-0.5, 12, 50, 0, head_width=2, head_length=3, fc='k', ec='k', length_includes_head=True, overhang=0.3, clip_on=False)
axes[4, 0].arrow(-4, 8.5, 0, -9, head_width=2, head_length=3, fc='k', ec='k', length_includes_head=True, overhang=0.3, clip_on=False)
axes[4, 0].text(25, 13.5, 'Feature maps', verticalalignment='top', horizontalalignment='center', size='medium')
axes[4, 0].text(-5.5, 4, 'Sections', verticalalignment='center', horizontalalignment='right', size='medium', rotation=90)

fig.tight_layout()
fig.subplots_adjust(bottom=0.08, left=0.08)
fig.savefig('pooling.png')
plt.show()
