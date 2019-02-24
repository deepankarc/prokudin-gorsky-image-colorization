import sys
import numpy as np
import cv2
from skimage import feature
import matplotlib.pyplot as mp_plt
import time
import preprocess_image

# src files
import preprocess_image as ppi
import image_colorization as imgc

def main_routine(MAX_PYMD_LEVEL, SIM_INDEX, CROP, EDGE_DET, IMAGE_NAME, DATA_ROOT):
  start_time = time.time()
  img, true_img = ppi.preprocess_image(DATA_ROOT+IMAGE_NAME, SIM_INDEX, MAX_PYMD_LEVEL, EDGE_DET, (CROP,CROP))
  print("Time required for preprocessing: %d secs" % (time.time() - start_time))

  # colorize image
  [rshift, cshift] = imgc.image_colorization(img, 0, MAX_PYMD_LEVEL, SIM_INDEX)

  # align image
  colorized_image = np.empty_like(true_img)
  colorized_image[0,:,:] = true_img[0,:,:]
  colorized_image[1,:,:] = np.roll(true_img[1,:,:], (rshift[0],cshift[0]), axis=(0,1))
  colorized_image[2,:,:] = np.roll(true_img[2,:,:], (rshift[1],cshift[1]), axis=(0,1))
  
  # show the image
  mp_plt.figure(figsize=(16,16))
  view_img = np.transpose(colorized_image, (1,2,0))
  mp_plt.imshow(view_img[:,:,[2,1,0]])
  
  # save the image
  save_img = np.transpose(colorized_image, (1,2,0)) * 255
  save_img = save_img.astype(np.uint8)
  cv2.imwrite(IMAGE_NAME[:-4]+".jpg",save_img,[cv2.IMWRITE_JPEG_QUALITY,50])
  print("Total computation time: %d secs" % (time.time() - start_time))
      
  return save_img

if __name__ == '__main__':
  print("Running Image Colorisation...")
  arglist = sys.argv.split() 
  MAX_PYMD_LEVEL = int(arglist[1])
  SIM_INDEX = arglist[2]
  CROP = int(arglist[3])
  EDGE_DET = int(arglist[4])
  IMAGE_NAME = arglist[5]
  DATA_ROOT = arglist[6]
  main_routine(MAX_PYMD_LEVEL, SIM_INDEX, CROP, EDGE_DET, IMAGE_NAME, DATA_ROOT)