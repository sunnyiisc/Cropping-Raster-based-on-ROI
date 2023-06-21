"""
Created on 2022, 13 Sept (13/09/22) at 23:12
    Title: Cropping_based_on_Selected_ROI.py - ...
    Description:
        -   ...
@author: Supantha Sen, sunnymac, IISc Bangalore
"""

# Importing Modules
from rasterio.crs import CRS
from rasterio.warp import transform_geom
from shapely.geometry import Polygon
from rasterio.mask import mask

# Importing Custom Modules
...

...
def crop_roi(dataset, Top_Lat, Bot_Lat, Lft_Lon, Rgt_Lon):

    img_crs = dataset.crs  # image reference coordinates
    wgs84_crs = CRS.from_epsg(4326)  # standard WGS84 coordinates

    roi = Polygon([(Lft_Lon, Top_Lat),
                   (Rgt_Lon, Top_Lat),
                   (Rgt_Lon, Bot_Lat),
                   (Lft_Lon, Bot_Lat)])

    # Transforming WGS84 roi to Image CRS ROI
    roi_img = transform_geom(wgs84_crs, img_crs, roi)

    # Cropping based on the ROI
    crop_img, crop_transform = mask(dataset, shapes=[roi_img], crop=True)

    return crop_img