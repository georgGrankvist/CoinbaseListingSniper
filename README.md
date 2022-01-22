# Coinbase Listing Sniper

Script that listens to the @CoinbaseAssets twitter to find information about new Coinbase listings,
and automatically buys 100 USDT worth of the new listing on Binance as soon as it is posted on Twitter.
As Coinbase is one of the largest exchanges in terms of active users and trading volume, you can generally
expect some positive price action in an asset if it is listed on their platform.
This script will help you react  early to listing news and allow you to purchase the asset before most manual traders. 

Installation/run instructions:
1. Import requests, json and Client from binance.client ( https://github.com/binance/binance-connector-python ) 
2. Create a twitter developer account, and create a Twitter developer project. 
3. Get an authentication bearer token from your project page, and set the "bearer_token" variable on line 15 in coinbase_listing_sniper.py to your token.
4. Create a Binance account 
5. Get a balance of 100 USDT or more. 
6. Get your Binance api_key and api_secret keys, and pass them into the Client object on line 82.  
7. Run coinbase_listing_sniper.py

If you don't want to have to run this script locally on your computer i'd recommend setting up a VPS that'll run it for you. It's also based on current formatting on Coinbase asset listing tweets, so if they change the format up it won't work. Future versions will introduce some error handling for when the Twitter API goes down, and multi-listing tweets. 
