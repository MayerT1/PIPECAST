import argparse
from raster_ops import tif_merger
from raster_ops import tif_clipper
from raster_ops import reproject
from iceye_utils import get_metadata
from iceye_utils import gcps2geotransform
from iceye_utils import rpc_warp
from hydrafloods_prep import get_inc_angle
from hydrafloods_prep import add_inc_angle_band
from vector2raster import vec2rast
#from osgeo import gdal

"""
gdal.Warp(
    "arcticdem_1024_reproj.tif",
    "arcticdem_1024_native.tif",
    dstSRS="EPSG:32603",
    srcSRS="EPSG:3413",
    xRes=4,
    yRes=4,
    resampleAlg="bilinear",
    targetAlignedPixels=True
)
"""

if __name__ == "__main__":
    #vec2rast('ground_truth_polys.shp', 'reproj_s1_kipnuk.tif', 'ground_truth_rasterized_v2.tif')
    #rpc_warp(
    #    '20251024T230532_ICEYE_X41_GRD_SM_951749491.tif',
    #    'arcticdem_1024_reproj.tif',
    #    'EPSG:32603',
    #    4,
    #    'rpc_warP_v3_20251024T230532_ICEYE_X41_GRD_SM_951749491.tif'
    #)
    #gcps2geotransform('20251028T014758_ICEYE_X37_GRD_SC_951754404.tif', 'geotransformed_20251028T014758_ICEYE_X37_GRD_SC_951754404.tif')
    #tif_clipper('clippin_1217.tif', 'test_vv.tif', -86.8191, 34.5776, -86.4964, 34.7719)
    #print(x)
    get_metadata('20251014T091912_ICEYE_X34_GRD_SLF_951726975.tif')
    #reproject(
    #    'reprojected_20251024T230532_ICEYE_X41_GRD_SM_951749491.tif',
    #    'geotransformed_20251024T230532_ICEYE_X41_GRD_SM_951749491.tif',
    #    'EPSG:32603',
    #    4
    #)
    #inc_angle = get_inc_angle('20251014T091912_ICEYE_X34_GRD_SLF_951726975.tif')   #'20251012T091343_ICEYE_X33_GRD_SLF_951721361.tif')
    #print(inc_angle)
    #add_inc_angle_band("modded_s1_kipnuk.tif", "reproj_s1_kipnuk.tif", inc_angle)
    #tif_merger('sentinel_merged_1205_1311.tif', ['s1a-iw-grd-vv-20251125t234657-20251125t234722-062041-07c2fb-001.tiff', 's1a-iw-grd-vv-20251125t234722-20251125t234747-062041-07c2fb-001.tiff'])#['sentinel1_hsv.tif', 'sentinel1_hsv_pt2.tif'])
