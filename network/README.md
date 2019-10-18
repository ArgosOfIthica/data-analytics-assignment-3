# Network Graph

## Dataset

The dataset used for the network graph is the 
[NYC Hotspot Wi-Fi Locations](https://data.cityofnewyork.us/City-Government/NYC-Wi-Fi-Hotspot-Locations/yjub-udmw/data)

The dataset contains information about the name, provider, and location of every open Wi-Fi hotspot in NYC.

## Data Analytics Performed

All entries in the dataset are imported using SODApy 
(Socrata Open Data API for Python) to be processed by Pandas.

Using pandas, the top 4 Wi-Fi networks from every borough in New York are calculated by 
counting the number of networks provided by a specific provider in each borough, 
then storing the results in a dictionary.

## Data Visualization

The data is visualized in a network graph, where the each borough is connected to its most popular network provider.

From this, one might determine which networks have the most infastructure in NYC, or 
perhaps which boroughs to avoid if some providers are undesirable.
