# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings
import json

import requests


bearer_token = ""
rule_headers = {'Content-Type': "application/json", "Authorization": "Bearer " + bearer_token}


def get_twitter_feed():
 #todo: add rule to filter for asset listing tweets
 rules = [{"value": "from:coinbaseassets"}]
 payload = {"add": rules}
 print(payload)

 rules_req = requests.post(url="https://api.twitter.com/2/tweets/search/stream/rules", headers=rule_headers, json=payload)
 print("Request status code = " + rules_req.status_code.__str__())
 print("Request content= " + rules_req.text)







if __name__ == '__main__':
    get_twitter_feed()
