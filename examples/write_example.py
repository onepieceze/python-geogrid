from python_geogrid import geogrid
import gdal

ds = gdal.Open("./data/MCD12Q1_LandUse_2001.tif")
if not ds: print("Error: fail to open file.")

geotranform = ds.GetGeoTransform()
projection  = ds.GetProjection()
xsize       = ds.RasterXSize
ysize       = ds.RasterYSize

in_band = ds.GetRasterBand(1)
data    = in_band.ReadAsArray()

out = geogrid("write")

out.set_index(key="type"        , value="categorical")
out.set_index(key="category_min", value=1)
out.set_index(key="category_min", value=20)
out.set_index(key="projection"  , value="regular_ll")
out.set_index(key="dx"          , value=geotranform[1])
out.set_index(key="dy"          , value=abs(geotranform[5]))
out.set_index(key="known_x"     , value=1)
out.set_index(key="known_y"     , value=1)
out.set_index(key="known_lat"   , value=geotranform[3]+geotranform[5]*ysize)
out.set_index(key="known_lon"   , value=geotranform[0])
out.set_index(key="wordsize"    , value=1)
out.set_index(key="tile_x"      , value=xsize)
out.set_index(key="tile_y"      , value=ysize)
out.set_index(key="tile_z"      , value=1)
out.set_index(key="units"       , value="\"category\"")
out.set_index(key="description" , value="\"MODIS modified-IGBP landuse - 500 meter\"")
out.set_index(key="mminlu"      , value="\"MODIFIED_IGBP_MODIS_NOAH\"")
out.set_index(key="iswater"     , value=17)
out.set_index(key="isice"       , value=15)
out.set_index(key="isurban"     , value=13)

index_root = "./"

out.write_geogrid(data, index_root=index_root)




