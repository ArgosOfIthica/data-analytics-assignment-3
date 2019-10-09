import networkx
import matplotlib
import pandas as pd
from sodapy import Socrata

NEW_YORK_DATA_AUTH_TOKEN = "QwLSoW0YRtDKSHtGNty0L7b8G"
FIRE_RESOURCE_NAME = "8m42-w767"


def load_data():
    # Load Fire Incident Dispatch Data
    global NEW_YORK_DATA_CLIENT, FIRE_DATAFRAME
    NEW_YORK_DATA_CLIENT = Socrata("data.cityofnewyork.us", NEW_YORK_DATA_AUTH_TOKEN)
    firedata = NEW_YORK_DATA_CLIENT.get(FIRE_RESOURCE_NAME, limit=10000)
    FIRE_DATAFRAME = pd.DataFrame.from_records(firedata)


def plot_bar():
    pass


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
