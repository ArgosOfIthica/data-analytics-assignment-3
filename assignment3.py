import networkx
import matplotlib.pyplot as plt
import pandas as pd
from sodapy import Socrata

NEW_YORK_DATA_AUTH_TOKEN = "QwLSoW0YRtDKSHtGNty0L7b8G"
NEW_YORK_DATA_CLIENT = Socrata("data.cityofnewyork.us", NEW_YORK_DATA_AUTH_TOKEN)
FIRE_RESOURCE_NAME = "8m42-w767"


def plot_bar():
    # Ingest: Load Fire Incident Dispatch Data
    data = NEW_YORK_DATA_CLIENT.get(FIRE_RESOURCE_NAME, limit=100000)  # TODO: Replace with 10000 after testing
    firedata = pd.DataFrame.from_records(data)
    # Data Analysis: Find average response time for each borough
    boroughs = firedata.alarm_box_borough.unique()
    average_response_times = dict()
    response_times_std = dict()
    for borough in boroughs:
        borough_incidents = firedata.loc[(firedata["alarm_box_borough"] == borough) & (
                firedata["valid_incident_rspns_time_indc"] == "Y")]
        borough_average_response_time = borough_incidents["incident_response_seconds_qy"].astype(float).mean()
        borough_response_time_std = borough_incidents["incident_response_seconds_qy"].astype(float).std()
        average_response_times[borough] = borough_average_response_time
        response_times_std[borough] = borough_response_time_std
    # Data Visualization
    plt.figure(figsize=(10, 6))
    plt.title("Fire Response Time by Borough in NYC")
    plt.ylabel("Average Incident Response Time (seconds)")
    plt.xlabel("Borough Name")
    plt.bar(boroughs, average_response_times.values(), yerr=response_times_std.values(), color="bgrcmyk")
    plt.tight_layout()
    plt.savefig("./bar/chart.jpg")
    plt.show()


def plot_pie():
    pass


def plot_line():
    # dates = firedata["incident_datetime"].astype("datetime64").dt.date.unique()
    # for date in dates:
    #     incidents = firedata.loc[firedata["incident_datetime"].astype("datetime64").dt.date == date]
    #     incident_count = len(incidents.index)
    #     print(date, incident_count)
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
