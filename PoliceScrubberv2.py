# 25 Nov 2017
# Western Kentucky University, in their efforts to support transparency,
# supports the public by giving access to crime reports that take place
# within their jurisdiction.

# Users are expected to enter a report category, report year and report
# month. From that, they submit a POST request and cypher throught the
# the table outputs.

# If locations were "rounded" to the nearest landmark, WKU UPD could
# autmoate and analyse crime statistics based on location but still
# have absolute locations as denoted in the official reports.



# import necessary libaries to parse data from POST respones
from bs4 import BeautifulSoup
import requests

# Set up to iterate through applicable years and months
for y in range(2000,2018):

    # Years are enter as strings versus integer (don't ask me why)
    year_str = str(y)

    # For each month in each year, snag the data
    for i in range (1,12):

        # Inspected the form and found the necessary fields to submit
        userdata = {"type": "P", "month": i, "year": year_str}

        # https://stackoverflow.com/questions/4214231/sending-data-using-post-in-python-to-php
        resp = requests.post('https://intranet.wku.edu/php/prod/POLICE/WKU_POLICE_SEARCH.php', params=userdata)

        # Set up to be parsed
        soup = BeautifulSoup(resp.text, 'html.parser')

        # Table was pretty gritty; only concerned with the displayTable class
        for each in soup.find_all('table',"displayTable"):
            data = each.find_all('td')
            entry = ""
            for tbl in data:

                # Data is filled with special characters (as denoted with polic reports
                # decided to go with the carrat (carret?) b/c not expected to be used
                # in police report. Easy to delimit later
                add_data = tbl.get_text() + "^"
                entry += add_data
                
            # Could write to file but no need; copy out of output shell
            print entry
