import requests
key = "uxns42qzqutpg8zvcth9pmkm"
hurts_id = "64bd0f02-6a5d-407e-98f1-fd02048ea21d"
brady_id = "41c44740-d0f6-44ab-8347-3b5d515e5ecf"
rodgers_id= "0ce48193-e2fa-466e-a986-33f751add206"
jackson_id= "e06a9c07-453a-4bb0-a7e9-2c3a64166dad"
wentz_id = "e9a5c16b-4472-4be9-8030-3f77be7890cb"
tua_id = "26ad9c27-de38-495e-913c-6fb2428e76d3"
import pandas as pd


#hurts season statistics
api_url = f"https://api.sportradar.us/nfl/official/trial/v7/en/players/{hurts_id}/profile.json?api_key={key}"
response = requests.get(api_url)
#print(response.json())
import json
hurtsdata = response.json()
formatted_data = json.dumps(hurtsdata['seasons'][2]['teams'][0]['statistics']['passing'],indent=2)
print(formatted_data)

def get_hurts_passing_stats():
  api_url = f"https://api.sportradar.us/nfl/official/trial/v7/en/players/{hurts_id}/profile.json?api_key={key}"
  response = requests.get(api_url)
  #print(response.json())
  import json
  hurtsdata = response.json()['seasons'][2]['teams'][0]['statistics']['passing']
  df_hurts = pd.json_normalize(hurtsdata)
  return df_hurts

get_hurts_passing_stats()

# brady season statistics
api_url = f"https://api.sportradar.us/nfl/official/trial/v7/en/players/{brady_id}/profile.json?api_key={key}"
response = requests.get(api_url)
#print(response.json())
import json
bradydata = response.json()
formatted_data = json.dumps(bradydata['seasons'][40]['teams'][0]['statistics']['passing'],indent=2)
print(formatted_data)

def get_brady_passing_stats():
   api_url = f"https://api.sportradar.us/nfl/official/trial/v7/en/players/{brady_id}/profile.json?api_key={key}"
   response = requests.get(api_url)
   #print(response.json())
   import json
   bradydata = response.json()['seasons'][40]['teams'][0]['statistics']['passing']
   df_brady = pd.json_normalize(bradydata)
   return(df_brady)

get_brady_passing_stats()

# rodgers season statistics
api_url = f"https://api.sportradar.us/nfl/official/trial/v7/en/players/{rodgers_id}/profile.json?api_key={key}"
response = requests.get(api_url)
#print(response.json())
import json
rodgersdata = response.json()
formatted_data = json.dumps(rodgersdata['seasons'][28]['teams'][0]['statistics']['passing'],indent=2)
print(formatted_data)

def get_rodgers_passing_stats():
  api_url = f"https://api.sportradar.us/nfl/official/trial/v7/en/players/{rodgers_id}/profile.json?api_key={key}"
  response = requests.get(api_url)
  #print(response.json())
  import json
  rodgersdata = response.json()['seasons'][28]['teams'][0]['statistics']['passing']
  df_rodgers = pd.json_normalize(rodgersdata)
  return(df_rodgers)

get_rodgers_passing_stats()





