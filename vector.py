from _global import EPSILON
import math

class Vector:

    def __init__(self, lst):
        self._values = list(lst)

    def __add__(self, another):
        """向量加法，返回结果向量"""
        assert len(self) == len(another), "Error in adding, Length of vectors must be same"

        return Vector([a + b] for a, b in zip(self, another))

    def __sub__(self, another):
        """向量减法，返回结果向量"""
        assert len(self) == len(another), "Error in subing, Length of vectors must be same"

        return Vector([a - b] for a, b in zip(self, another))

    def __mul__(self, k):
        """返回数量乘法的结果向量"""
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        """返回数量乘法的结果向量"""
        return Vector([e * k for e in self])

    def __truediv__(self, k):
        """返回数量除法的结果向量"""
        return (1 / k) * self

    def dot(self, another):
        """点乘向量，返回结果标量"""
        assert len(self) == len(another), "Error to dot, Vector len must be same"

        return sum(a * b for a, b in zip(self, another))

    def __pos__(self):
        """返回向量取正的结果向量"""
        return 1 * self

    @classmethod
    def zore(cls, dim):
        """返回一个 dim 维的零向量"""
        return cls([0] * dim)

    def norm(self):
        """返回向量的模"""
        return math.sqrt(sum(e**2 for e in self))
    
    def normalize(self):
        """返回向量的单位向量"""
        if self.norm() < EPSILON:
            raise ZeroDivisionError("Normalize error！norm is zero")
        return Vector(self._values) / self.norm()

    def __neg__(self):
        """返回向量取负的结果向量"""
        return -1 * self

    def __iter__(self):
        """返回向量的迭代器""" 
        return self._values.__iter__()

    def __getitem__(self, index):
        """取向量的第 index 个元素"""
        return self._values[index]

    def __len__(self):
        """返回向量长度 (有多少个元素)"""
        return len(self._values)

    def __repr__(self):
        return "Vector({})".format(self._values)
    
    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))


