import heapq

class CPoly(object):

  def __init__(self, coef):
    self._coef = coef
    self._vals = [0.0, 1.0]

  def __call__(self, x):
    if x >= len(self._vals):
      prod = self._vals[-1]
      for i in xrange(len(self._vals)-1, x):
        prod = prod * (i + self._coef) / i
        self._vals.append(prod)
    return self._vals[x]


class Ugly(object):

  def __init__(self, *factors):
    self._vals = [1]
    mult_iters = []
    for factor in factors:
      mult_iters.append((lambda f: (f*x for x in self._vals))(factor))
    self._iter = _unique(heapq.merge(*mult_iters))

  def __call__(self, x):
    x -= 1
    while x >= len(self._vals):
      self._vals.append(self._iter.next())
    return self._vals[x]


def _unique(stream):
  last = None
  for x in stream:
    if x != last:
      last = x
      yield x


class Cake(object):

  def __init__(self):
    self._table = [[1]]
    self._n = 0
    self._k = 0

  def __call__(self, n, k):
    if k > self._k:
      for ni in xrange(self._n + 1):
        for ki in xrange(self._k + 1, k + 1):
          if ni == 0:
            self._table[ni].append(1)
          else:
            self._table[ni].append(self._table[ni][ki-1] + self._table[ni-1][ki-1])
      self._k = k
    if n > self._n:
      for ni in xrange(self._n + 1, n + 1):
        self._table.append([1])
        for ki in xrange(1, self._k + 1):
          self._table[ni].append(self._table[ni][ki-1] + self._table[ni-1][ki-1])
      self._n = n
    return self._table[n][k]


class Partition(object):

  def __init__(self):
    self._table = [[1]]
    self._n = 0

  def __call__(self, n):
    while n > self._n:
      self._n += 1
      j = self._n
      i = 0
      while j > 0:
        self._table[i].append(self._compute(i, j))
        i += 1
        j -= 1
      self._table.append([1])
    return self._table[0][n]

  def _compute(self, row, col):
    if row + 1 > col:
      return 0
    return self._add_diagonal(row, col-row-1)

  def _add_diagonal(self, row, col):
    result = 0
    i = row
    j = col
    while j >= 0:
      result += self._table[i][j]
      i += 1
      j -= 1
    return result
