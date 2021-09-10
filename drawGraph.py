from sklearn import metrics
from sklearn.metrics import auc
import matplotlib.pyplot as plt


class DrawGraph:
    def __init__(self):
        plt.figure()
        plt.title('Receiver Operating Characteristic')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.plot([0, 1], [0, 1], 'k--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])

    @staticmethod
    def add(y, score, label, color):
        fpr, tpr, thresholds = metrics.roc_curve(y, score, pos_label=2)
        roc_auc = auc(fpr, tpr)
        plt.plot(fpr, tpr, label=label + ' (area = %0.3f)' % roc_auc, color=color)

    @staticmethod
    def show():
        plt.legend(loc="lower right")
        plt.show()
