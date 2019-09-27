import numpy as np
import cv2
import skimage.feature as feature
import matplotlib.pyplot as mp_plt

def preprocess_image(DATA_ROOT, SIM_INDEX, MAX_PYMD_LEVEL, EDGE_DET, crop=(0,0)):
  C = 3 # no. of channels

  # slice image into RGB channels and generate crops to 
  # deal with black border artifacts
  glass_plate_image = cv2.imread(DATA_ROOT,0)
  glass_plate_image = cv2.normalize(glass_plate_image.astype('float'), 
                                    None, 0.0, 1.0, norm_type=cv2.NORM_MINMAX)
  
  H,W = glass_plate_image.shape
  H = (H - (H % 3)) // C # make image height a multiple of 3
  fig = mp_plt.figure(figsize=(16,16))
  true_img = np.empty((C, H, W))
  img = np.empty((C, H - 2*crop[0], W - 2*crop[1]))
  for i in range(C):
    true_img[i,:,:] = glass_plate_image[i*H:(i+1)*H,:]
    img[i,:,:] = glass_plate_image[i*H+crop[0]:(i+1)*H-crop[0],crop[1]:W-crop[1]]
    fig.add_subplot(1,3,i+1)
    imgplot = mp_plt.imshow(true_img[i,:,:])
    imgplot.set_cmap('gist_gray')
      
  # get colorized image
  if(EDGE_DET is True):
    transformed_img = np.empty_like(img)
    transformed_img[0,:,:] = feature.canny(img[0,:,:])
    transformed_img[1,:,:] = feature.canny(img[1,:,:])
    transformed_img[2,:,:] = feature.canny(img[2,:,:])
  else:
    transformed_img = img
    
  return [transformed_img, true_img]
