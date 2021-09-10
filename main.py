__author__ = 'Junghwan Kim'
__copyright__ = 'Copyright 2016-2019 Junghwan Kim. All Rights Reserved.'
__version__ = '1.0.0'

from getData import GetData
from drawGraph import DrawGraph

single = GetData('/home/jkim/data/SET2/CLS1FCN1_SINGLE').list()
cascade = GetData('/home/jkim/data/SET2/CLS2FCN2_CASCADE').list()

graph = DrawGraph()
graph.add(single[0], single[1], 'SINGLE ROC', 'blue')
graph.add(cascade[0], cascade[1], 'CASCADE ROC', 'red')
graph.show()

print('\n[SUCCESS] Finished all process.')
