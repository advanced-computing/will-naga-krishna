# Project Title: Mapping Construction in NYC

## Description
This project takes maps of construction applications and prices of sold properties in NYC and combines them to understand the relationsship between the amount of housing construction and the property prices.

## Instruction
We are in the progress of developing the project but we hope that this can provide policymakers and those curious about the city a constant understanding of the current housing construction environment.

<a target="_blank" href="https://colab.research.google.com/github/advanced-computing/willnaga">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

## Proposal 

### Research Questions
- What areas of the city (borough, community district, etc.) are seeing the most construction of housing? How many units can be expected?
- What kinds of housing are being prioritized by the city? New developments? Renovations? Low density? High density? Luxury? Affordable?
- Do people apply for construction permits in areas with high property prices?

### Datasets
- [Construction Applications](https://data.cityofnewyork.us/Housing-Development/DOB-NOW-Build-Job-Application-Filings/w9ak-ipjd/about_data)
- [Prices of Sold Properties](https://data.cityofnewyork.us/City-Government/NYC-Citywide-Annualized-Calendar-Sales-Update/w2pb-icbu/about_data)
  
### Data Loading Method: Incremental
- We are using an incremental data load method to load data from the NYC OpenData API.
- This method is preferable to using the append method because it allows us to update data that is already in the Google BigQuery table as well as add additional rows that are new.
- Additonally, this method should be faster than using a truncate and load method which would recreate the entire table each time the script is run.
- We are hoping that using an incremental method not only captures the most up to date data but also helps speed up the site.

## Instruction to Set Up our APP
- 1. Open a new window in VS Code.
- 2. Click "Clone Git Repository."
- 3. Copy the URL "https://github.com/advanced-computing/will-naga-krishna" and paste it in the search bar. And Enter.
- 4. Select the repository destination. Select "Open." 
- 5. Open a new Terminal. 
- 6. Run the following command `python -m venv .venv` to set up the virtual environment. 
- 7. Right click on the file path for the virtual environment and copy the file path. Activate the environment by running the following command `source (filepath)/bin/activate`
- 8. Install the requirements using `pip install -r requirements.txt`.
- 9. Run the app by putting `streamlit run Home.py`.