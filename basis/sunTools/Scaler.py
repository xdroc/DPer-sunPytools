# -*- coding: utf-8 -*-
# @Time    : 2021-10-09 10:37
# @Author  : ForestNeo
# @Email   : dr.forestneo@gmail.com
# @Software: PyCharm

"""
This script is used for data scaling

@ 2021.10.09: initialized
"""


class Normalizer:
    """
    数据归一化，默认归一化到区间[0,1]
    """
    def __init__(self, input_domain, output_domain=(0, 1)):
        self._in_min, self._in_max = input_domain[0], input_domain[1]
        self._out_min, self._out_max = output_domain[0], output_domain[1]
        self.slope = (self._out_max - self._out_min) / (self._in_max - self._in_min)

    def normalize(self, v):
        if v > self._in_max or v < self._in_min:
            raise Exception("ERR: input out of range! input = %.2f, range = [%.2f, %.2f]" % (v, self._in_min, self._in_max))
        return self.slope * v + self._out_min - self.slope * self._in_min

    def de_normalize(self, v):
        return (v - self._out_min + self.slope * self._in_min) / self.slope


if __name__ == '__main__':
    input_domain = [0, 100]
    output_domain = [0, 1]

    normalizer = Normalizer(input_domain, output_domain)
    print(normalizer.normalize(50))
    print(normalizer.de_normalize(0.5))