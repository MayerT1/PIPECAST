import argparse
from raster_ops import tif_merger
from iceye_utils import get_metadata
from hydrafloods_prep import get_inc_angle
from hydrafloods_prep import add_inc_angle_band

if __name__ == "__main__":
    #get_metadata('20251014T091912_ICEYE_X34_GRD_SLF_951726975.tif')
    #inc_angle = get_inc_angle('20251014T091912_ICEYE_X34_GRD_SLF_951726975.tif')   #'20251012T091343_ICEYE_X33_GRD_SLF_951721361.tif')
    #print(inc_angle)
    #add_inc_angle_band("v15_modded_20251014T091912_ICEYE_X34_GRD_SLF_951726975.tif", "20251014T091912_ICEYE_X34_GRD_SLF_951726975.tif", inc_angle)
    #tif_merger('sentinel_merged_1205_1311.tif', ['s1a-iw-grd-vv-20251125t234657-20251125t234722-062041-07c2fb-001.tiff', 's1a-iw-grd-vv-20251125t234722-20251125t234747-062041-07c2fb-001.tiff'])#['sentinel1_hsv.tif', 'sentinel1_hsv_pt2.tif'])
