import requests
from difflib import get_close_matches
import xml.etree.ElementTree as ET

states = {'Maharashtra', 'Gujarat', 'Delhi', 'Tamil Nadu', 'Rajasthan',
'Madhya Pradesh', 'Uttar Pradesh', 'Andhra Pradesh', 'Punjab', 'West Bengal',
'Telangana', 'Jammu and Kashmir', 'Karnataka', 'Haryana', 'Bihar', 'Kerala',
'Odisha', 'Chandigarh', 'Jharkhand', 'Tripura', 'Uttarakhand', 'Chhattisgarh', 'Assam',
'Himachal Pradesh', 'Ladakh', 'Andaman and Nicobar Islands', 'Meghalaya', 'Puducherry', 'Goa', 'Manipur',
'Mizoram', 'Arunachal Pradesh','Dadra and Nagar Haveli', 'Nagaland', 'Daman and Diu',
'Lakshadweep', 'Sikkim', 'Total', 'India'}

def get_state_data(state):    
    url = "https://api.covid19india.org/data.json"
    repsonse = requests.get(url).json()
    if state == "India":
        state = "Total"

    if state == "Dadra and Nagar Haveli":
        state = "Dadra and Nagar Haveli and Daman and Diu"
    
    statewise_response = repsonse['statewise']
    state_information = [s for s in statewise_response if s['state'] == state][0]
    
    return state_information
        

def check_state(state):
    state_split = state.split(' ')
    state = ' '.join([x.title() for x in state_split if x != 'and'])
    if state not in states:
        closest_match = get_close_matches(state, states, n=1, cutoff=0.6)
        return closest_match[0], False
    else:
        return state, True

def get_news_links():
    '''
    Grabs the top links from WHO website
    '''
    news_link = 'https://www.who.int/rss-feeds/news-english.xml'
    repsonse = requests.get(news_link)
    tree = ET.fromstring(repsonse.text)
    links =  tree.findall('.//link')
    return links[2:7]



# def get_district_data(state):
#     url = "https://api.covid19india.org/zones.json"
#     repsonse = requests.get(url).json()
#     if district == "Delhi":
#         district = "Green"
#
#     if district == "Delhi":
#         district = "Delhi"
#
#     zones_response = repsonse['zones']
#     district_information = [s for s in zones_response if s['district'] == district][0]
#
#     return district_information

if __name__ == '__main__':
    total = get_state_data('Total')
    print(f"Total {total}")