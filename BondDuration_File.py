import numpy as np
def getBondDuration(y, face, couponRate, m, ppy=1):
    times = np.arange(1, m*ppy + 1)
    pv = (1+y/ppy)**-times
    cf = face*couponRate/ppy
    pvcf = pv*cf

    bondprice = np.sum(pvcf) + face*pv[-1]
    pvcf_t = np.sum(times*pvcf) + times[-1]*face*pv[-1]

    duration = pvcf_t/bondprice

    return duration
#unit test
#print(round(getBondDuration(.03, 2000000, .04, 10,1),2))