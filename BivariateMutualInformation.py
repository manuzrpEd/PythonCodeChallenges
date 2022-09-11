# Starting code

import numpy as np

def mutual_information(arr):
    def p_j(arr):
        return np.sum(arr, axis=1)#row sum
    def p_i(arr):
        return np.sum(arr, axis=0)#column sum
    def sum_px_logpx(px):
        prod = px*np.log(px + 0.0000000001)
        return sum(prod)
    def sum_pxy_logpxy(pxy):
        prod = pxy*np.log(pxy + 0.0000000001)
        return np.sum(prod)
    return sum_pxy_logpxy(arr) - sum_px_logpx(p_i(arr)) - sum_px_logpx(p_j(arr))

arr = np.array([[0, 0, 0], [0, 0, 0]])

print(mutual_information(arr))