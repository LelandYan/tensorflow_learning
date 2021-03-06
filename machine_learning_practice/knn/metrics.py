# _*_ coding: utf-8 _*_
__author__ = 'LelandYan'
__date__ = '2019/2/19 15:46'
import numpy as np


def accuracy_score(y_true, y_predict):
    """计算y_true和y_predict之间的准确率"""
    assert y_true.shape[0] == y_predict.shape[0], \
        "the size of y_true must be equal to the size of y_predict"
    return np.sum(y_predict == y_true) / len(y_true)
