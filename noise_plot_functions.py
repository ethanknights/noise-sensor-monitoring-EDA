import geopandas as gpd
from matplotlib import pyplot as plt

# Read in the GeoJSON file
gdf = gpd.read_file('./data/LSOA_Dec_2021_Boundaries_Generalised_Clipped_EW_BGC_2022_5605507071095448309.geojson')

# Plot the GeoDataFrame
# gdf.plot()

code = 'E01004647'  # Replace with the code for your desired LSOA
geom = gdf.loc[gdf['LSOA21CD'] == code, 'geometry'].iloc[0]
gdf = gpd.GeoDataFrame(geometry=[geom], crs=gdf.crs)


gdf.plot()
plt.show()