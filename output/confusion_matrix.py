import itertools
import numpy as np
import pickle
import matplotlib.pyplot as plt


with open('confusion_matrix.pickle', 'rb') as f:
    cm = pickle.load(f)
classes = list(range(10))

plt.figure()
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
plt.title('Confusion matrix')
plt.colorbar()
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes)
plt.yticks(tick_marks, classes)
plt.ylabel('True class')
plt.xlabel('Predicted class')

# thresh = cm.max() / 2.
# for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
#     plt.text(j, i, cm[i, j],
#              horizontalalignment='center',
#              verticalalignment='center',
#              color='white' if cm[i, j] > thresh else 'black')

plt.show()
