import ast
import json
import os
from PIL import Image
import numpy as np


class GetData:
    def __init__(self, path):
        self.path = path
        self.y = []
        self.scores = []

    def list(self):
        folder = os.listdir(self.path)
        for name in folder:
            y, scores = self.load(self.path + '/' + name)
            self.y += y
            self.scores += scores

        return np.array(self.y), np.array(self.scores)

    @staticmethod
    def load(path):
        print('\n[LOAD]', path)

        # Append list
        list_lbl = []
        for paths, dirs, files in os.walk(path + '/MAP'):
            for name in sorted(files):
                if name.endswith('_fill.png') and len(name) == 13:
                    list_lbl.append(name)
                if name.endswith('_fill.png') and len(name) == 17:
                    list_lbl.append(name)

        # Create list
        list_y = []
        list_scores = []

        # Read JSON file
        with open(os.path.dirname(path) + 'json/' + os.path.basename(path) + '.out') as f:
            data = json.load(f)
        data = ast.literal_eval(json.dumps(data))

        i = 0
        dict_abn = {}
        while i < len(list_lbl):
            key = data['diagnosis'][i]['case'][-4:]
            key = '{:04d}'.format(int(key))
            value = data['diagnosis'][i]['classification']
            if value[0][0] == 'ABN':
                value_abn = value[0][1]
            else:
                value_abn = value[1][1]
            dict_abn[key] = value_abn
            i += 1

        # Read each label
        i = 0
        while i < len(list_lbl):

            progress = '(' + str(i + 1) + '/' + str(len(list_lbl)) + ')'
            print(progress, list_lbl[i])

            pos = False
            lbl = Image.open(path + '/MAP/' + list_lbl[i]).convert("P", palette=Image.WEB)
            lbl = np.array(lbl)

            for array in lbl:
                for j in range(len(lbl)):
                    if array[j] != 255:
                        pos = True
                    j += 1

            if pos is True:
                list_y.append(2)
            else:
                list_y.append(1)

            scores = float(dict_abn[list_lbl[i][-13:-9]]) / float(100)
            scores = format(scores, '.2f')
            list_scores.append(float(scores))

            i += 1

        return list_y, list_scores
