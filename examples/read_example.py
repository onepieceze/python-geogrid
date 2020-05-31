from python_geogrid import geogrid
import gdal, osr
import numpy as np

ds = geogrid("read")

array, geotransform = ds.read_geogrid(data_root="./data/modis_landuse_15s", dtype=np.uint8)

description = ds.get_index(key="description")

print(f"read {description}\n")

nz = array.shape[0]
ny = array.shape[1]
nx = array.shape[2]

driver = gdal.GetDriverByName("GTiff")
out    = driver.Create("modis_landuse_15s.tif", nx, ny, 1, gdal.GDT_Byte)
outRasterSRS = osr.SpatialReference()
outRasterSRS.ImportFromEPSG(4326)      #  代码4326表示WGS84坐标
out.SetProjection(outRasterSRS.ExportToWkt())
out.SetGeoTransform(geotransform)

outband = out.GetRasterBand(1)
outband.WriteArray(array[0,:,:])
outband.FlushCache()