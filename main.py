import os
from dotenv import load_dotenv

load_dotenv()
import requests
from datetime import datetime
USERNAME = "niizzaarr"
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID="graph1"
pixela_endpoint="https://pixe.la/v1/users"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# response1= requests.post(url=pixela_endpoint,json=user_params)
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id":GRAPH_ID,
    "name":"Sea Service Day Log",
    "unit":"day",
    "type":"int",
    "color":"sora"
}
headers={
    "X-USER-TOKEN":TOKEN
}

response2 = requests.post(url=graph_endpoint,json=graph_config, headers=headers)


pixel_creation_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today=datetime.now()
# print(today)

pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":"1",

}
response = requests.post(url=pixel_creation_endpoint, json=pixel_data,headers=headers)
print(response.text)