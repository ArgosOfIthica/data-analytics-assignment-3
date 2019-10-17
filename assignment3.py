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
    #Ryan Sims
    data = NEW_YORK_DATA_CLIENT.get(FIRE_RESOURCE_NAME, limit=100000)  # TODO: Replace with 10000 after testing
    firedata = pd.DataFrame.from_records(data)
    # Data Analysis: Find number of incidents per zipcode for each borough
    dict={}
    for i in firedata.incident_classification_group:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1
    plt.figure(figsize=(10, 6))
    plt.title("Percentage of Firebox calls of certain types")
    plt.pie(x=dict.values(), labels=dict.keys())
    plt.savefig("./pie/chart.jpg")
    plt.show()


def plot_scatter():
    #Ryan Sims
    data = NEW_YORK_DATA_CLIENT.get(FIRE_RESOURCE_NAME, limit=10000)  # TODO: Replace with 10000 after testing
    firedata = pd.DataFrame.from_records(data)
    firedata=firedata.dropna(axis=0, subset = ['incident_datetime', 'incident_travel_tm_seconds_qy'])
    for i in range(len(firedata.incident_datetime)):
        hms=list(map(float, firedata.incident_datetime[i].split("T")[1].split(":")))
        firedata.incident_datetime[i]=hms[0]+hms[1]/60+hms[2]/60/60
    plt.figure()
    plt.title("Plot of Time of day against response time")
    plt.ylabel("Incident Response Time (minutes)")
    plt.xlabel("Time of day")
    plt.yticks([60*i for i in range(24)],[i for i in range(24)])
    plt.xticks([i for i in range(24)],[str(i)+":00" for i in range(24)])
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=90)
    plt.scatter(x=firedata.incident_datetime,y=firedata.incident_travel_tm_seconds_qy, s=2, )
    plt.savefig("./scatter/chart.jpg")
    plt.show()


def plot_histogram():
    #Ingest
    data = NEW_YORK_DATA_CLIENT.get(DOG_RESOURCE_NAME,
                                    select="date_extract_woy(licenseissueddate), rownumber, animalname, `extract-year` ",
                                    where="`extract-year` == '2018' and licenseissueddate between '2017-01-01T00:00:00' and '2018-01-01T00:00:00'",
                                    limit=1000000)
    dog_data = pd.DataFrame.from_records(data)
    dog_data.drop_duplicates(keep=False, inplace=True)

    #Analytics
    listdata = dog_data.date_extract_woy_licenseissueddate.tolist()
    listdata = list(map(lambda x: int(x), listdata))
    # Visualization
    plt.hist(x=listdata, bins=52)
    plt.title("Number of Licenses Issued in 2017 over Time")
    plt.ylabel("Number of Licenses")
    plt.xlabel("Weeks ")

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
