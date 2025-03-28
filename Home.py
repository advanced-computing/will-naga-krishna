import streamlit as st

st.set_page_config(page_title="Mapping Construction Information in NYC", page_icon="🏠")

st.title('Mapping Construction Information in NYC')
st.title('by Will & Naga & Krishna')

st.sidebar.header("Construction Information in NYC")

'''
Description: This project takes the NYC Department of Construction construction applications
 and maps them across the city to understand the amount of housing construction the city is
   undertaking to combat the affordability crisis, where the construction is located and what 
   type of construction there is.
'''

st.header('Proposal',divider=True)

st.markdown('''
**What dataset are you going to use?**:  
The dataset we are going to use is the NYC Department of Building Job Application Filings dataset.  
This dataset shows the applications for construction that have been filed in the city. It is updated daily.  
Link: https://data.cityofnewyork.us/Housing-Development/DOB-Job-Application-Filings/ic3t-wcy2/about_data
  
*Change*:  
Because the original dataset we found couldn't be filtered by date from the API, we opted for a newer version.  
Link: https://data.cityofnewyork.us/Housing-Development/DOB-NOW-Build-Job-Application-Filings/w9ak-ipjd/about_data  
We are also using a dataset that yearly property sale information.  
Link: https://data.cityofnewyork.us/City-Government/NYC-Citywide-Annualized-Calendar-Sales-Update/w2pb-icbu/about_data  

**What are your research question(s)? It should be specific, and objectively answerable through the data available.**  
- What areas of the city (borough, community district, etc.) are seeing the most construction of housing? How many units can be expected?
- What kinds of housing are being prioritized by the city? New developments? Renovations? Low density? High density? Luxury? Affordable?
- Are certain kinds of construction types being approved more readily over another?
- *Is there a way to identify the affordability of the construction?*  

**What's the link to your notebook?**  
Notebook: https://colab.research.google.com/drive/1jmjXjNDOjwjSoi0ZG1TnKZNoQJJdMslJ?usp=sharing
We weren’t able to access the full API without Colab crashing but we have the first 2000 rows at the bottom. 
*Change: We are now able to access the full API.*  

**What's your target visualization? Include a picture.
Ideally we can show each community board and the amount of units or the amount of construction that is going on using a bar like the one below and then some nuance for the type of construction.
''')
st.image('targetvisual.png')

st.markdown('''  
**What are your known unknowns?**
- Some measure of affordability
- How heavy is our visualization map? How much can the site show while still being functional and quick to load.

**What challenges do you anticipate?**
- The amount of data is quite large
- The quality of the city’s data may be questionable at times
- Determining the best way of visualizing a huge dataset will be a challenge
- Determining the best ways of filtering permitted applications from all applications as well as any that were cancelled. Do we want to look at just applications or approved permits or some combination of them?
            ''')