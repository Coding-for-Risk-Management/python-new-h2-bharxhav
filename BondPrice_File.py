import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    coupon = (couponRate/ppy)*face
    pv = (1+(y/ppy))**(-np.arange(1, m*ppy+1))
    pvcf = coupon*pv.sum()
    pv_face = face*pv[-1]
    bondprice = pvcf + pv_face
    return bondprice

# unit test
# x = getBondPrice(.03, 2000000, .04, 10,  1)
# y = getBondPrice(.03, 2000000, .04, 10,  2)
# print(round(x,0))
# print(round(y,0))