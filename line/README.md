# Bar Chart

## Dataset

The dataset used for the line chart is the 
[NYC Dog Licensing Dataset](https://data.cityofnewyork.us/Health/NYC-Dog-Licensing-Dataset/nu7n-tubp/data)

The dataset contains information about the name, breed, age, and location of all the registered dogs in New York City.

## Data Analytics Performed

All entries in the dataset where the breed of dog is not unknown are imported using SODApy 
(Socrata Open Data API for Python) to be processed by Pandas.

Using pandas, the data are sorted by the year the dog was born and what breed it is. Then, 
the total number of dogs of each breed born each year is calculated.

## Data Visualization

The data are plotted in a line chart which shows the total number of dogs by each breed 
(of the 20 most popular in NYC) born in each year. This chart is both useful and meaningful since 
it gives at-a-glance information about both the number and type of dogs being born each year in NYC.

From this, one might determine the relative popularity of breeds over time, or what breed-specific policies
may need to be implemented.
