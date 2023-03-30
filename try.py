import geopandas as gpd
import pandas as pd
site_locations = pd.read_csv('data/LOCAR_Site_Information.csv',
                             skipfooter=11, engine='python',
                             usecols = ['Site Code', 'Longitude', 'Latitude'],
                             index_col='Site Code')
site_geometry = gpd.points_from_xy(site_locations['Longitude'],
                                   site_locations['Latitude'], crs='EPSG:4326')
site_gdf = gpd.GeoDataFrame(site_locations, geometry=site_geometry)
site_gdf
site_gdf.crs

site_gdf_ll = site_gdf.to_crs('EPSG:4326')
site_gdf_ll
site_gdf_ll.crs

FP_catchment = gpd.GeoDataFrame.from_file('data/river_catchments/frome_piddle_catchment.shp')
FP_catchment
FP_catchment.crs

import matplotlib.pyplot as plt
PL_catchment = gpd.GeoDataFrame.from_file('data/river_catchments/pang_lambourn_catchment.shp')
PL_catchment
PL_catchment.plot()
plt.show()


from geopandas.tools import sjoin
site_locations = pd.read_csv('data/LOCAR_Site_Information.csv',
                             skipfooter=11, engine='python',
                             usecols = ['Site Code', 'Longitude', 'Latitude'],
                             index_col='Site Code')
site_geometry = gpd.points_from_xy(site_locations['Longitude'],
                                   site_locations['Latitude'], crs='EPSG:4326')
site_gdf = gpd.GeoDataFrame(site_locations, geometry=site_geometry)

FP_catchment = gpd.GeoDataFrame.from_file('data/river_catchments/frome_piddle_catchment.shp')

FP_sites = sjoin(site_gdf, FP_catchment)

FP_sites

def is_site_within_catchment(site_dataframe, catchment_dataframe):
    answer_dataframe = sjoin(site_dataframe, catchment_dataframe)
    if answer_dataframe.size:
        return True
    else:
        return False

#is_site_within_catchment(site_gdf.loc[['FP23']], FP_catchment)