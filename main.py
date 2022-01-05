import requests
USERNAME = "brylimz"
TOKEN = "9384u23423hdsksdfkj"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "cylcing graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}


headers = {
    "X-USER-TOKEN": TOKEN
}

#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
pixel_creation_endpoint =  f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
