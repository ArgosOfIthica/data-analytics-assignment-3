# Histogram

## Dataset

The dataset used for the line chart is the 
[NYC Dog Licensing Dataset](https://data.cityofnewyork.us/Health/NYC-Dog-Licensing-Dataset/nu7n-tubp/data)

The dataset contains information about the name, breed, age, and location of all the registered dogs in New York City.

## Data Analytics Performed

All entries in the dataset are imported using SODApy 
(Socrata Open Data API for Python) to be processed by Pandas. The week of each license application date is extracted by a query filter.

## Data Visualization

The data is plotted in a histogram that shows the date of every time a dog license has
been applied for. This chart is both useful and meaningful since it gives a quick visual
way of showing trends in when people acquire dogs. 

From this, one might determine the most popular time to get a dog, or when dog related
products might be in greatest demand.
