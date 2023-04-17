import geopandas as gpd
from matplotlib import pyplot as plt
import matplotlib as mpl

## Environment
base_geojson_file = './data/LSOA_Dec_2021_EK-westminster.geojson' # see init_write_geojson_westminster_lsoa_subset()


def init_write_geojson_westminster_lsoa_subset():
    # Create a smaller geojson file as the one from ONS is huge and time-consuming to load

    # Geo-boundaries from:
    # https://geoportal.statistics.gov.uk/datasets/ons::lsoa-dec-2021-boundaries-generalised-clipped-ew-bgc/aboutß
    all_gdf = gpd.read_file(
        './data/LSOA_Dec_2021_Boundaries_Generalised_Clipped_EW_BGC_2022_5605507071095448309.geojson')

    # Subset to LSOAs that contain 'Westminster' in their name
    gdf = all_gdf.loc[all_gdf['LSOA21NM'].str.contains('Westminster')]

    # Write the GeoDataFrame to a new GeoJSON file
    out_file = base_geojson_file
    gdf.to_file(out_file, driver='GeoJSON')

    print('written: ', out_file)

    return


def plot_highlighted_lower_super_output_areas(keys_list):

    gdf = gpd.read_file(base_geojson_file)

    # Plot the GeoDataFrame with all LSOAs in a single colour
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf.plot(ax=ax, color='gray')

    # Plot subset of GeoDataFrames
    highlighted_codes = keys_list  # gdf = gdf.loc[gdf['LSOA21CD'].isin(codes)]

    # Get geometries of the highlighted LSOAs and plot them with a different color
    highlighted_geoms = gdf.loc[gdf['LSOA21CD'].isin(highlighted_codes), 'geometry']
    gpd.GeoSeries(highlighted_geoms).plot(ax=ax, color='red')

    return fig


def plot_heatmap_lower_super_output_areas(list_of_tuples_lsoa_value):

    gdf = gpd.read_file(base_geojson_file)

    # Create a new column for the values to be plotted
    gdf['plot_value'] = None

    # Assign gdf['plot_value'] from list_of_tuples_lsoa_value
    for lsoa, value in list_of_tuples_lsoa_value:
        gdf.loc[gdf['LSOA21CD'] == lsoa, 'plot_value'] = value

    gdf['plot_value'].fillna(0, inplace=True)

    # Normalise values (optional) - lose context!
    # norm = mpl.colors.Normalize(vmin=gdf['plot_value'].min(), vmax=gdf['plot_value'].max())
    # gdf['plotvalue'] = gdf['plot_value'].apply(norm)

    # Plot the GeoDataFrame with a heatmap based on the 'normalized_value' column
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf.plot(ax=ax, column='plot_value',
             cmap='Reds', alpha=0.5, edgecolor='black', linewidth=0.8, legend=True, cax=plt.axes([0.9, 0.1, 0.02, 0.8]))

    return fig
