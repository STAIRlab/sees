import numpy as np

def _split(a, value, source=None):
    # like str.split, but for arrays
    if source is None:
        source = a
    if np.isnan(value):
        idx = np.where(~np.isnan(source))[0]
    else:
        idx = np.where(source != value)[0]
    return np.split(a[idx],np.where(np.diff(idx)!=1)[0]+1)


XYZ = np.random.random((15,3))

CON = np.arange(len(XYZ))

for i in (0, 1, 4, 8, 9, 12, 14):
    XYZ[i, :] = np.nan

for indices in _split(CON, np.nan, XYZ[:,0]):
    n = sum(np.isnan(XYZ[:indices[0], 0]))
    print(indices-n)

