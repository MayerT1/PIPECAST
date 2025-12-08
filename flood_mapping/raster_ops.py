from osgeo import gdal
from osgeo_utils import gdal_merge
import subprocess

gdal_merge_py = r"C:\Users\micky\anaconda3\Scripts\gdal_merge.py"

# A function to compute the bounds of multiple rasters for merging
def tif_merger(out_tif, input_tifs):
    cmd = ["python", gdal_merge_py, "-o",out_tif]+input_tifs  # + ".tif" #gdal_merge.py
    subprocess.call(cmd)

    #subprocess.call(cmd.split()+input_tifs)


from osgeo import gdal
import os
