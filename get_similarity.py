import numpy as np

# compute image similarity
def get_similarity(img1, img2, SIM_INDEX):
  if(SIM_INDEX == 'SSD'):
    # sum of squared differences
    score = np.sum(np.square(img1 - img2))
  elif(SIM_INDEX == 'NCC'):
    # normalised cross-correlation
    score = np.sqrt(np.cov(img1,img2) / (np.cov(img1) * np.cov(img2)))
  elif(SIM_INDEX == 'SSIM'):
    # structural similarity index, note: L = 1
    c1 = 0.01
    c2 = 0.03
    p1 = ((np.mean(img1) * np.mean(img2)) + c1) / (np.mean(img1)**2 + np.mean(img2)**2 + c1)
    p2 = ((2 * np.cov(img1,img2)) + c2) / (np.cov(img1) + np.cov(img2) + c2)
    score = np.mean(p1 * p2)
    
  return score