from vector import Vector

class Matrix:

    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    def __getitem__(self, pos):
        """返回矩阵 pos 位置的元素"""
        r, c = pos
        return self._values[r][c]

    def col_vector(self, index):
        """返回矩阵的第 index 个列向量"""
        return Vector([row[index] for row in self._values])

    def row_vector(self, index):
        """返回矩阵的第 index 个行矩阵"""
        return Vector(self._values[index])

    def row_num(self):
        """返回矩阵的行数"""
        return self.shape()[0]

    def col_num(self):
        """返回矩阵的列数"""
        return self.shape()[1]

    def size(self):
        """返回矩阵的元素个数"""
        r, c = self.shape()
        return r * c

    __len__ = row_num

    def shape(self):
        """返回矩阵的形状：（行数，列数）"""
        return len(self._values), len(self._values[0])

    def __repr__(self):
        return "Matrix({})".format(self._values)

    __str__ = __repr__