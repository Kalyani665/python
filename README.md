
# Python code for analysis of historic weather data
 The 10+ years Weather data consist of mean daily maximum temprature (tmax), mean daily minimum temperature(tmin), Days of air frost(af), total rainfall(rain), and total sunshine duration(sun) for different locations. 
 
## Requirements
   1. python 3.9
   2. jupyter notebook anaconda3

## How the code works:

libraries used: pandas, re, matplotlib

I have taken a sample dataset from https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data for a random location and saved it into a local .txt file. 
output_file1 contains pre-processed raw data in dataframe format.
created a empty dataframe(with same keys as in output_file1) named new_df to store average values for all columns w.r.t. year.

A 'for' loop iterates to get dataframe containing values for all the months in a particular year using argxy() function. The x and y values are updated to get next dataframe values for the next year's month.
The function avg() returns a short dataframe- new_row, containing average values for minimum and maximum temprature, Days of air frost(af), rainfall(rain).
new_df dataframe contains average vlaues for all the variables for all years.

matplotlib and pandas libraries are used to generate plots. Published the charts in Jupyter notebook.
1.minimum and maximum temprature
![minimum and maximum temprature](https://github.com/Kalyani665/python/blob/main/avg_min_max_temp.PNG)

2. Average Days of air frost(af) and Average rainfall(rain)
![avg_af_rain](https://github.com/Kalyani665/python/blob/main/avg_af_rain.PNG)

##TODO
1. The code is not fully automated. 
2. selection of the city or location by user is not handled.  
3. The data is not called through API, it's manually stored in a local file.
