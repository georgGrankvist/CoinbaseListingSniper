# @author GG
# @version 1.0
#


import json

import requests
from binance.client import Client

bearer_token = ""
headers = {'Content-Type': "application/json", "Authorization": "Bearer " + bearer_token}


def delete_all_rules(rules):
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        headers=headers,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


def get_rules():
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", headers=headers
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def get_twitter_feed():
    # todo: add rule to filter for asset listing tweets
    rules = [{"value": "from:coinbaseassets inbound transfers", "tag:": "inbound transfers"},
             ]
    payload = {"add": rules}
    print(payload)

    rules_req = requests.post(url="https://api.twitter.com/2/tweets/search/stream/rules", headers=headers, json=payload)
    print("Request status code = " + rules_req.status_code.__str__())
    print("Request content= " + rules_req.text)

    get_rules()

    feed_fetch_res = requests.get("https://api.twitter.com/2/tweets/search/stream", headers=headers, stream=True, )

    if feed_fetch_res.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                feed_fetch_res.status_code, feed_fetch_res.text
            )
        )

    for response_line in feed_fetch_res.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            data = (json.dumps(json_response['data'], indent=4, sort_keys=True))
            ticker = (data[data.find("(") + 1:data.find(")")])
            create_binance_buy_order(ticker)


def create_binance_buy_order(ticker):
    client = Client("api_key", "api_secret")
    pair = ticker + "/USDT"
    new_asset_price = client.get_symbol_ticker(pair)

    buy_quantity = round(100 / float(new_asset_price['price']))

    try:
        client.create_order(symbol=pair,
                            side=Client.SIDE_BUY,
                            type=Client.ORDER_TYPE_MARKET,
                            quantity=buy_quantity)
    except Exception as e:
        print("Couldn't load order")
        print(e)


if __name__ == '__main__':
    delete_all_rules(get_rules())
    get_twitter_feed()
