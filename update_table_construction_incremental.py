import pandas_gbq
from sodapy import Socrata
import pandas as pd

project_id = "sipa-adv-c-naga-will"
table_id = 'nyc_construction_property.construction_applications'

def incremental_load():

    # get the latest filing_date from bigquery
    sql = """
        SELECT MAX(filing_date) AS latest_date FROM `sipa-adv-c-naga-will.nyc_construction_property.construction_applications`
    """
    latest_date_df = pandas_gbq.read_gbq(sql, project_id=project_id)
    latest_date = latest_date_df["latest_date"].iloc[0]

    # create filter for new data
    if pd.isna(latest_date):
        filter = None
    else:
        filter = f"filing_date > '{latest_date}'"

    # fetch data from nyc open data
    client = Socrata("data.cityofnewyork.us", None)
    df_list = []
    offset = 0

    while True:
        if filter:
            results = client.get('w9ak-ipjd', where=filter, limit=5000, offset=offset)

        else:
            results = client.get('w9ak-ipjd', limit=5000, offset=offset)

        offset += 5000

        print(len(results), offset)
        
        if len(results)==0:
            break

        df_list.extend(results)

    # prepare data frame and upload
    if df_list:
        df_construction = pd.DataFrame.from_dict(df_list)

        # Keep only the required columns
        columns_to_keep = [
            'job_filing_number',
            'filing_status',
            'borough',
            'building_type',
            'proposed_no_of_stories',
            'proposed_height',
            'proposed_dwelling_units',
            'filing_date',
            'latitude',
            'longitude',
            'job_type'
        ]
        df_construction = df_construction[columns_to_keep]

        # Upload to BigQuery
        pandas_gbq.to_gbq(df_construction,
                                table_id,
                                project_id=project_id,
                                if_exists='append')
        print("Incremental data uploaded.")

    else:
        print("No new data to upload.")

if __name__ == "__main__":
    incremental_load()