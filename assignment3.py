import networkx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sodapy import Socrata
from datetime import datetime

NEW_YORK_DATA_AUTH_TOKEN = "QwLSoW0YRtDKSHtGNty0L7b8G"
NEW_YORK_DATA_CLIENT = Socrata("data.cityofnewyork.us", NEW_YORK_DATA_AUTH_TOKEN)
FIRE_RESOURCE_NAME = "8m42-w767"


def plot_bar():
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
    print(firedata)
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
    plt.title(f"Fire Response Time by Borough in NYC\n({firedata.incident_datetime.astype('datetime64').min():%B %Y} - {firedata.incident_datetime.astype('datetime64').max():%B %Y})")
    plt.ylabel("Average Incident Response Time (seconds)")
    plt.xlabel("Borough Name")
    plt.bar(boroughs, average_response_times.values(), yerr=response_times_std.values(), color="bgrcmyk")
    plt.tight_layout()
    plt.savefig("./bar/chart.jpg")
    plt.show()


def plot_pie():
    pass


def plot_line():
    pass


def plot_scatter():
    pass


def plot_histogram():
    pass


def plot_network():
    pass


if __name__ == "__main__":
    plot_bar()
    plot_pie()
    plot_line()
    plot_scatter()
    plot_histogram()
    plot_network()
