# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE_MAGIC_CELL
# Automatically replaced inline charts by "no-op" charts
# %pylab inline
import matplotlib
matplotlib.use("Agg")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
import dataiku
from dataiku import pandasutils as pdu
import pandas as pd

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
from preprocessing.weather import TM_handling

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read the dataset as a Pandas dataframe in memory
# Note: here, we only read the first 100K rows. Other sampling options are available
dataset_weather = dataiku.Dataset("weather")
df = dataset_weather.get_dataframe(limit=1000)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df = TM_handling(df, ["PrecipTotal", "SnowFall", "Water1"])

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Recipe outputs
weather_cleaned = dataiku.Dataset("weather_cleaned")
weather_cleaned.write_with_schema(pandas_dataframe)