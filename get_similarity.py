# compute covariance
def cov(x1,x2):
  return np.mean((x1 - np.mean(x1)) * (x2 - np.mean(x2)))

# compute image similarity
def get_similarity(img1, img2, SIM_INDEX):
  if(SIM_INDEX == 'SSD'):
    # sum of squared differences
    score = np.sum(np.square(img1 - img2))
  elif(SIM_INDEX == 'NCC'):
    # normalised cross-correlation
    score = np.sqrt(abs(cov(img1,img2) / (cov(img1,img1) * cov(img2,img2))))
  elif(SIM_INDEX == 'SSIM'):
    # structural similarity index, note: L = 1
    c1 = 0.01
    c2 = 0.03
    p1 = ((img1 - np.mean(img1)) * (img2 - np.mean(img2)) + c1) / (
      np.square(img1 - np.mean(img1)) + np.square(img2 - np.mean(img2)) + c1)
    p2 = 2 * (np.sqrt(abs(cov(img1,img2))) + c2) / (cov(img1,img1) + cov(img2,img2) + c2)
    score = np.mean(p1 * p2)
    
  return score