import networkx
import matplotlib.pyplot as plt
import pandas as pd
from sodapy import Socrata
from datetime import datetime

NEW_YORK_DATA_AUTH_TOKEN = "QwLSoW0YRtDKSHtGNty0L7b8G"
NEW_YORK_DATA_CLIENT = Socrata("data.cityofnewyork.us", NEW_YORK_DATA_AUTH_TOKEN)
FIRE_RESOURCE_NAME = "8m42-w767"
DOG_RESOURCE_NAME = "nu7n-tubp"


def plot_bar():
    # Bradley Shrader
    # Ingest: Load Fire Incident Dispatch Data
    query = f"""
    select 
        incident_datetime, 
        alarm_box_borough, 
        incident_response_seconds_qy
    where
        valid_incident_rspns_time_indc = 'Y' and
        date_extract_y(incident_datetime) = {datetime.now().year - 1}
    limit 2000000
    """
    data = NEW_YORK_DATA_CLIENT.get(FIRE_RESOURCE_NAME, query=query)
    firedata = pd.DataFrame.from_records(data)
    # Data Analysis: Find average response time for each borough
    boroughs = firedata.alarm_box_borough.unique()
    average_response_times = dict()
    response_times_std = dict()
    for borough in boroughs:
        borough_incidents = firedata.loc[firedata["alarm_box_borough"] == borough]
        borough_average_response_time = borough_incidents["incident_response_seconds_qy"].astype(float).mean()
        borough_response_time_std = borough_incidents["incident_response_seconds_qy"].astype(float).std()
        average_response_times[borough] = borough_average_response_time
        response_times_std[borough] = borough_response_time_std
    # Data Visualization
    plt.figure(figsize=(10, 6))
    plt.title(
        f"Fire Response Time by Borough in NYC\n({firedata.incident_datetime.astype('datetime64').min():%B %Y} - {firedata.incident_datetime.astype('datetime64').max():%B %Y})")
    plt.ylabel("Average Incident Response Time (seconds)")
    plt.xlabel("Borough Name")
    plt.bar(boroughs, average_response_times.values(), yerr=response_times_std.values(), color="bgrcmyk")
    plt.tight_layout()
    plt.savefig("./bar/chart.jpg")


def plot_line():
    # Bradley Shrader
    # Ingest
    data = NEW_YORK_DATA_CLIENT.get(DOG_RESOURCE_NAME,
                                    select="animalbirth, animalgender, breedname, animalname, zipcode",
                                    where="breedname not like 'Unknown'",
                                    limit=1000000)
    dog_data = pd.DataFrame.from_records(data)
    dog_data.drop_duplicates(keep=False, inplace=True)
    # Analytics
    top_breeds = dog_data.breedname.value_counts().index[:20]
    unique_years = sorted([year for year in dog_data.animalbirth.astype('int').unique() if year > 1997])
    # Visualization
    plt.figure(figsize=(10, 6))
    plt.title("Dogs Born Each Year Since 1997 of the Top 20 Breeds in NYC")
    plt.ylabel("Number of Dogs")
    plt.xlabel("Year")
    plt.xticks(unique_years, unique_years, rotation="vertical")
    for breed in top_breeds:
        # print(breed)
        plt.plot(unique_years, [
            len(dog_data.loc[(dog_data["breedname"] == breed) & (dog_data["animalbirth"].astype("int") == year)].index)
            for year in unique_years], label=breed)
    plt.legend(loc='upper left', fontsize="small")
    plt.savefig("./line/chart.jpg")


def plot_pie():
    pass


def plot_scatter():
    pass


def plot_histogram():
    pass


def plot_network():
    pass


if __name__ == "__main__":
    plot_bar()
    plot_line()
    plot_pie()
    plot_scatter()
    plot_histogram()
    plot_network()
    plt.show()  # Show all plots at end
