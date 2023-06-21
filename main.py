"""
Created on 2022, 13 Sept (13/09/22) at 19:33
    Title: main.py - ...
    Description:
        -   ...
@author: Supantha Sen, sunnymac, IISc Bangalore
"""

# Importing Modules
import rasterio
from rasterio.plot import show, adjust_band
import numpy as np

# Importing Custom Modules
from roi_selection import *
from browse_gui import *

...
file_path = browse_file('Select the TIF file')

dataset = rasterio.open(file_path)
print(dataset.meta)

# Defining the ROI in WGS584 coordinates
#T, B, L, R = 38.181, 37.881, 78.721, 79.021
T, B, L, R = 38.152, 37.852, 77.827, 78.127

# Cropping the image to the selected ROI
crop_img = crop_roi(dataset, T, B, L, R)

# Plotting the Image
imgdata = np.array([adjust_band(dataset.read(i)) for i in (3,2,1)])
show(imgdata)

# Plotting Cropped Image of the ROI
crop_img = adjust_band(crop_img[3:6,:,:])
show(crop_img[::-1])