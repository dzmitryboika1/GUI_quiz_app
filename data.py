import requests
import html

parameters = {
    "amount": 10,
    "type": "boolean",
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]
for question in question_data:
    # decoding html characters like &quot
     question["question"] = html.unescape(question["question"])



