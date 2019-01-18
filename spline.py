def Spline(*points):
  assert(len(points) >= 2)
  return _SplineEval(points, _SplineNormal(points))


def _IPolyMult(prod, poly):
  if not prod:
    return
  if not poly:
    prod[:] = []
    return
  for i in xrange(len(poly)-1):
    prod.append(0)
  for i in xrange(len(prod)-1, -1, -1):
    for j in xrange(len(poly)):
      if j == 0:
        prod[i] = poly[j]*prod[i]
      elif i >= j:
        prod[i] += poly[j]*prod[i-j]


def _IPolyAdd(sum, poly):
  for i in xrange(len(poly)):
    if i == len(sum):
      sum.append(poly[i])
    else:
      sum[i] += poly[i]


def _PolyCompose(f, g):
  sum = []
  for i in xrange(len(f) - 1, -1, -1):
    _IPolyMult(sum, g)
    _IPolyAdd(sum, [f[i]])
  return sum


def _PolyEval(f, x):
  sum = 0
  for i in xrange(len(f) - 1, -1, -1):
    sum = sum*x + f[i]
  return sum


def _IPoly3Fit(poly3, x, y):
  actual = _PolyEval(poly3, x)
  poly3[3] = float(y - actual) / x**3


def _Poly3Shift(poly3, x):
  result = _PolyCompose(poly3, [x, 1])
  result[3] = 0.0
  return result


def _Spline(points, x, x2):
  assert points
  cubic = [float(points[0][1]), x, x2, 0]
  result = []
  for i in xrange(len(points)-1):
    xdiff = float(points[i+1][0]-points[i][0])
    _IPoly3Fit(cubic, xdiff, float(points[i+1][1]))
    result.append(cubic)
    cubic = _Poly3Shift(cubic, xdiff)
  result.append(cubic)
  return result


def _SplineNormal(points):
  splines0 = _Spline(points, 0.0, 0.0)
  splines1 = _Spline(points, 1.0, 0.0)
  plen = len(points)
  end2nd0 = splines0[plen-1][2]
  end2nd1 = splines1[plen-1][2]
  start1st = -end2nd0 / (end2nd1-end2nd0)
  return _Spline(points, start1st, 0.0)


class _SplineEval(object):

  def __init__(self, points, splines):
    self._points = points
    self._splines = splines

  def __call__(self, x):
    plen = len(self._points)
    assert x >= self._points[0][0]
    assert x <= self._points[plen-1][0]
    first = 0
    last = plen-1
    while first + 1 < last:
      mid = (first + last) / 2
      if x >= self._points[mid][0]:
        first = mid
      else:
        last = mid
    return _PolyEval(self._splines[first], x - self._points[first][0])

