import requests
import json
from datetime import datetime
# import pandas as pd
import time
from re import search



with open('dataset.csv', 'r') as f:
		card_details = json.load(f)
print(len(card_details))

# function to get the prediction of tennis event from goal serve for yesterday
#http://127.0.0.1:8000/prediction
def test2(card_details):
	dataList = []
	for info in team_details:
		url = "http://127.0.0.1:8000/prediction"
		if (info["player_one_win_percentage"] == "0.0") or (info["player_one_win_percentage"] == "0.0"):
			dataList.append(info)
		else:
			payload = json.dumps({
			  "V1": info["V1"],
			  "V2": info["V2"],
			  "V3": info["V3"],
			  "V4": info["V4"],
			  "V5": info["V5"],
			  "V6": info["V6"],
			  "V7": info["V7"],
			  "V8": info["V8"],
			  "V9": info["V9"],
			  "V10": info["V10"],
			  "V11": info["V12"],
			  "V13"  : info["V14"],
			  "V14"  : info["V14"],
			  "V15"  : info["V15"],
			  "V16"  : info["V16"],
			  "V17"  : info["V17"],
			  
			
			  "V18" : info["V18"],
			  "V19" : info["V19"],
			  "V20" : info["V20"],
			  "V21" : info["V21"],
			  "V22" : info["V22"],
			  "V23" : info["V23"],
			  "V24" : info["V24"],
			  "V25" : info["V25"],
			  "V26" : info["V26"]
                          "V27" : info["V27"]
                          "V28" : info["V28"]
                          "Amount" : info["Amount"]
			})
			headers = {
			  'Content-Type': 'dataset/csv'
			}
			response = requests.request("POST", url, headers=headers, data=payload)
			data = response.csv()
			info.update(data)
			dataList.append(info)
			print(dataList)


	return dataList

raw_data_1 = test2(team_details)

with open("dataset.csv", 'w') as f:
 	f.write(csv.dumps(raw_data_1, indent=3))

#import pandas as pd
#df = pd.read_json("tennis_for_september27.json")
#df.to_csv("tennis_matches prediction september27.csv",index=False)


