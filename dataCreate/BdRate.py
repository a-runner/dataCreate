#Author: Ylonge
#Data: 20190406
#Function: Compute BD-rate between anchor data and test data.
#Input: (dictAnchorData, dictTestData) 
# where dict contains 4 dict, each of which contains {'bit': *, 'y': *, 'u': *, 'v': *, 'yuv': *}
#Output: (BdRate_data_dict) where dict contains {'y': *, 'u': *, 'v': *, 'yuv': *}

from math import log10

def Pchipend(h1, h2, delta1, delta2):
    """This child function is reused by BdRint."""
    d = ((2 * h1 + h2) * delta1 - h1 * delta2) / (h1 + h2)
    if (d * delta1) < 0:
        d = 0
    elif ((delta1 * delta2) < 0) and (abs(d) > abs(3 * delta1)):
        d = 3 * delta1
    else:
        pass
    return d

def BdRint(bitrate, dist, low, high):
    """This child function is used by function bdRateSingle()."""
    logRate = [0] * 4
    logDistortion = [0] * 4
    for i in range(0, 4, 1):
        logRate[i] = log10(bitrate[3 - i])
        logDistortion[i] = dist[3 - i]

    H = [0] * 4
    delta = [0] * 4
    for i in range(0, 3, 1):
        H[i] = logDistortion[i + 1] - logDistortion[i]
        delta[i] = (logRate[i + 1] - logRate[i]) / H[i]

    d = [0] * 4
    d[0] = Pchipend(H[0], H[1], delta[0], delta[1])
    for i in range(1, 3, 1):
        d[i] = (3 * H[i - 1] + 3 * H[i]) / ((2 * H[i] + H[i - 1]) / delta[i - 1] + (H[i] + 2 * H[i - 1]) / delta[i])
    d[3] = Pchipend(H[2], H[1], delta[2], delta[1])
    
    c = [0] * 4
    b = [0] * 4
    for i in range(0, 3, 1):
        c[i] = (3 * delta[i] - 2 * d[i] - d[i + 1]) / H[i]
        b[i] = (d[i] - 2 * delta[i] + d[i + 1]) / (H[i] * H[i])

    result = 0
    for i in range(0, 3, 1):
        s0 = logDistortion[i]
        s1 = logDistortion[i + 1]
        
        s0 = max(s0, low)
        s0 = min(s0, high)
        
        s1 = max(s1, low)
        s1 = min(s1, high)
        
        s0 = s0 - logDistortion[i]
        s1 = s1 - logDistortion[i]
        
        if s1 > s0:
            result = result + (s1 - s0) * logRate[i]
            result = result + (s1 * s1 - s0 * s0) * d[i] / 2
            result = result + (s1 * s1 * s1 - s0 * s0 * s0) * c[i] / 3
            result = result + (s1 * s1 * s1 * s1 - s0 * s0 * s0 * s0) * b[i] / 4
    return result

def ComputeBdrate(dictAnchorData, dictTestData):
  """This function computes BD-rate between anchor data and test data."""
  rateAnchor = []
  rateTest = []
  listQP = list(dictAnchorData.keys())
  for key in listQP:
    rateAnchor.append(dictAnchorData[key]['bit'])
    rateTest.append(dictTestData[key]['bit'])
  if len(rateAnchor) != 4 or len(rateTest) != 4:
    raise NameError(f"Distortion {rateAnchor} is less than 4.")
  
  listComponent = ['y', 'u', 'v', 'yuv']
  gain = {}
  for comp in listComponent:
    if comp not in dictAnchorData[listQP[0]] or comp not in dictTestData[listQP[0]] or dictAnchorData[listQP[0]][comp] == 0 or dictTestData[listQP[0]][comp] == 0:
      continue
    
    distAnchor = []
    distTest = []
    for key in dictAnchorData.keys():
      distAnchor.append(dictAnchorData[key][comp])
      distTest.append(dictTestData[key][comp])
    if len(distAnchor) != 4 or len(distTest) != 4:
      raise NameError(f"Distortion {distAnchor} is less than 4.")
    
    minPSNR = max(min(distAnchor), min(distTest))
    maxPSNR = min(max(distAnchor), max(distTest))
    vA = BdRint(rateAnchor, distAnchor, minPSNR, maxPSNR)
    vB = BdRint(rateTest, distTest, minPSNR, maxPSNR)
    average = (vB - vA) / (maxPSNR - minPSNR)
    gain[comp] = 10**average - 1

  return gain