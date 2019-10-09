import networkx
import matplotlib.pyplot as plt
import pandas as pd
from sodapy import Socrata

NEW_YORK_DATA_AUTH_TOKEN = "QwLSoW0YRtDKSHtGNty0L7b8G"
NEW_YORK_DATA_CLIENT = None
FIRE_RESOURCE_NAME = "8m42-w767"
FIRE_DATAFRAME = None


def load_data():
    # Load Fire Incident Dispatch Data
    global NEW_YORK_DATA_CLIENT, FIRE_DATAFRAME
    NEW_YORK_DATA_CLIENT = Socrata("data.cityofnewyork.us", NEW_YORK_DATA_AUTH_TOKEN)
    firedata = NEW_YORK_DATA_CLIENT.get(FIRE_RESOURCE_NAME, limit=100)  # TODO: Replace with 10000 after testing
    FIRE_DATAFRAME = pd.DataFrame.from_records(firedata)


def plot_bar():
    # Data Analysis: Find average response time for each borough
    boroughs = FIRE_DATAFRAME.alarm_box_borough.unique()
    average_response_times = dict()
    for borough in boroughs:
        borough_incidents = FIRE_DATAFRAME.loc[(FIRE_DATAFRAME["alarm_box_borough"] == borough) & (FIRE_DATAFRAME["valid_incident_rspns_time_indc"] == "Y")]
        borough_average_response_time = borough_incidents["incident_response_seconds_qy"].astype(float).mean()
        average_response_times[borough] = borough_average_response_time



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
    load_data()
    plot_bar()
    plot_pie()
    plot_line()
    plot_scatter()
    plot_histogram()
    plot_network()
