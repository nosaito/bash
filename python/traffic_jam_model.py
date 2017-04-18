#!/usr/bin/env python
# -*- coding: sjis -*-

# traffic jam simulation test
# http://qiita.com/jabberwocky0139/items/e2526fc5ee3b0dbf144b?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items


# case in Python 2.6~
# same print behavior as python 3
from __future__ import print_function


import numpy as np
from scipy.integrate import odeint


def trafficJam(f, t, a, c, L):
    """
    微分方程式の定義(odeint)
    f = [x, v]
    """
    x, v = f[:N], f[N:]

    def V(h):
        return np.tanh(h - c) + np.tanh(c)

    x_dot = v
    x = np.append(x, [x[0]])
    diff_x = np.diff(x)
    diff_x = np.array([i if i > 0 else L + i for i in diff_x])

    v_dot = a * (V(diff_x) - v)

    return np.append(x_dot, v_dot)


# 各定数
N, a, c, L = 30, 1.3, 2, 60

# 初期位置
x = np.arange(N) * L / N

# 初期速度
v = [(1 + np.tanh(c)) / 2] + ([1 + np.tanh(c)] * (N - 1)) # 最初の1台がブレーキをかける

# 時刻
t = np.arange(0, 200, 0.1)

# 微分方程式を解く
var = odeint(trafficJam, np.append(x, v), t, args=(a, c, L), full_output=False)
x_arr, v_arr = var[:, :N], var[:, N:]
