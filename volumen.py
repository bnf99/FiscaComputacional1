import numpy as np
from matplotlib import pyplot as plt


def UltimaSuperficieDeContorno(archivo):
    datos = np.loadtxt(archivo, delimiter="\t")
    a = []
    b = []
    for i in range(len(datos)):
        if datos[i, 1] < 0:
            a.append(datos[i])
        else:
            b.append(datos[i])
    y1 = np.array(b)
    y2 = np.array(a)
    p1 = np.polyfit(y1[:, 0], y1[:, 1], len(y1))
    p2 = np.polyfit(y2[:, 0], y2[:, 1], len(y2))
    area1 = np.polyval(np.polyint(p1), np.max(y1[:, 0])) - np.polyval(np.polyint(p1), np.min(y1[:, 0]))
    area2 = -1*(np.polyval(np.polyint(p2), np.max(y2[:, 0])) - np.polyval(np.polyint(p2), np.min(y2[:, 0])))
    area = area1 + area2
    x = np.poly1d([1, 0])
    m = np.polymul(x, p1)
    n = np.polymul(x, p2)
    mint = np.polyval(np.polyint(m), np.max(y1[:, 0])) - np.polyval(np.polyint(m), np.min(y1[:, 0]))
    nint = -1*(np.polyval(np.polyint(n), np.max(y2[:, 0])) - np.polyval(np.polyint(n), np.min(y2[:, 0])))
    centroidex = (mint+nint)/area
    # que madre se fue todo la tarde para darme cuenta que de igual al eje magnético
    return centroidex, area
