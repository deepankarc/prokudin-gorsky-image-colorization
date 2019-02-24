===================== FUNCTIONS ======================

cov() - computes covariance between two images

get_similarity() - computes similarity measures

align_image_channels() - computes the optimal shift for green and red channels of the images

pyramid_reduce() - contructs the image pyramid

image_colorization() - recursively calls pyramid_reduce and encapsulates alignment of image channels using using image pyramids

preprocess_image() - loads the image and preprocesses it for computation

main_routine() - the main handling routine of the code which strings together the above modules and saves the final image

run_image_color.py - Can be used to run the program. Accepts 6 arguments given below. Please prefer using the .ipynb version if any problems are encountered with the .py file.

Image Colorization Final.ipynb - Contains the implementation of the program as a self-descriptive jupyter notebook. Please run all cells to generate the outputs.

====================== PARAMETERS ======================

MAX_PYMD_LEVEL - no. of image pyramids. Integer.
SIM_INDEX - metric used to compute similarity. String (SSD, NCC, SSIM)
CROP - image cropping factor. Integer
EDGE_DET - whether edge detection should be used with current image. Boolean for .ipynb and interger for .py
IMAGE_NAME - image name. String. eg. 'self_portrait.tif'
DATA_ROOT - root folder path. String. eg.'F:/Projects/CSCE 689 - Computational Photography/'

====================== RUNNING THE CODE ======================
Please use the .ipynb file to run the code if the .py file doesn't run. The notebook is self contained. The .py files have been generated from the notebook. Each cell of the note has been saved as a .py file for greater clarity understand the codebase.