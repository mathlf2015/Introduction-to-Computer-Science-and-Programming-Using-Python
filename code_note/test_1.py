class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError('width must be a number')
        else:
            self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError('height must be a number')
        else:
            self._height = value
    @property
    def resolution(self):
         return self._width*self.height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__



class Fib:
    def __getitem__(self, item):
        if isinstance(item, int):
            if item > 0:
                index, a, bb = 1, 1, 1
                while index < item:
                    a, bb = bb, a + bb
                    index += 1
                return a
        elif isinstance(item, slice):
            print(item.start, item.step, item.stop)
            start, step, stop = item.start, item.step, item.stop
            if item.start is None:
                start = 0
            if item.step is None:
                step = 1
            if item.stop is None:
                stop = 0
            if start < 0 or step <= 0 or stop < 0:
                raise TypeError("start<0||step<=0||stop<0")
            elif start + step > stop:
                raise TypeError("start + step > stop")
            else:
                result = []
                index, a, bb = 1, 1, 1
                while index <= stop:
                    a, bb = bb, a + bb
                    if index >= start and (index - start) % step == 0:
                        result.append(a)
                    index += 1
                return result

        return "不支持"


print(Fib()[4:-1:1])
