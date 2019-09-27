import time

import numpy as np
import cv2

import align_image_channels_pyramids as aicp


# form image pyramids
def pyramid_reduce(img):
  fil_img = np.transpose(img, (1,2,0))
  fil_img = cv2.resize(fil_img, None, fx=0.5, fy=0.5) # decimate by factor of 2
  
  return np.transpose(fil_img, (2,0,1))

def image_colorization(img, level, MAX_PYMD_LEVEL, SIM_INDEX):  
  # recursively downsample image till pyramid level MAX_PYMD_LEVEL
  if(level < MAX_PYMD_LEVEL):
    [rshift, cshift] = image_colorization(pyramid_reduce(img), level+1, MAX_PYMD_LEVEL, SIM_INDEX)
  else:
    rshift = np.zeros(2,dtype=np.int32)
    cshift = np.zeros(2,dtype=np.int32)
  
  start_time = time.time()
  # estimate alignment parameters
  if(level ==  MAX_PYMD_LEVEL):
    rshift, cshift = aicp.align_image_channels_pyramids(img, rshift, cshift, 20, SIM_INDEX) # coarse, search larger region
  else:
    rshift, cshift = aicp.align_image_channels_pyramids(img, 2*rshift, 2*cshift, 2, SIM_INDEX) # precision search
  print(rshift,cshift)
  print("Computation time at level %d: %d secs" % (level, time.time() - start_time))

  return [rshift, cshift]