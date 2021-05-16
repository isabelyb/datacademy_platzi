import numpy as np
import matplotlib.pyplot as plt


def estimate_b0_b1(x, y):
    n = np.size(x)

    # Promedios de X e Y
    m_x = np.mean(x)
    m_y = np.mean(y)

    # Sumatoria de XY y sumatoria de XX
    sumatoria_xy = np.sum((x-m_x)*(y-m_y))
    sumatoria_xx = np.sum((x-m_x)**2)    # (x-m_x)**2 == x*(x-m_x)

    # Coeficientes de regresión
    b_1 = sumatoria_xy / sumatoria_xx
    b_0 = m_y - b_1*m_x

    return(b_0, b_1)