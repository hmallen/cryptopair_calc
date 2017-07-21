#!/usr/env python3

# Cryptocurrency pair arbitrage calculator (GDAX)

import gdax
import sys
import time

public_client = gdax.PublicClient()


def display_current():
    # BTCUSD
    btcusd_bidask = public_client.get_product_order_book('BTC-USD', level=1)

    btcusd_bid = btcusd_bidask['bids'][0][0]
    btcusd_ask = btcusd_bidask['asks'][0][0]
        
    # LTCUSD
    ltcusd_bidask = public_client.get_product_order_book('LTC-USD', level=1)

    ltcusd_bid = ltcusd_bidask['bids'][0][0]
    ltcusd_ask = ltcusd_bidask['asks'][0][0]

    # LTCBTC
    ltcbtc_bidask = public_client.get_product_order_book('LTC-BTC', level=1)

    ltcbtc_bid = ltcbtc_bidask['bids'][0][0]
    ltcbtc_ask = ltcbtc_bidask['asks'][0][0]

    # ETHUSD
    ethusd_bidask = public_client.get_product_order_book('ETH-USD', level=1)

    ethusd_bid = ethusd_bidask['bids'][0][0]
    ethusd_ask = ethusd_bidask['asks'][0][0]

    # ETHBTC
    ethbtc_bidask = public_client.get_product_order_book('ETH-BTC', level=1)

    ethbtc_bid = ethbtc_bidask['bids'][0][0]
    ethbtc_ask = ethbtc_bidask['asks'][0][0]

    # CALCULATE ARBITRAGE OPPORTUNITIES
    ltcusd_viabtc = float(ltcbtc_ask) * float(btcusd_ask)
    ltc_diff = float(ltcusd_viabtc) - float(ltcusd_ask)

    ethusd_viabtc = float(ethbtc_ask) * float(btcusd_ask)
    eth_diff = float(ethusd_viabtc) - float(ethusd_ask)

    print()
    print('LTCUSD:  ' + str(ltcusd_ask))
    print('L-B-USD: ' + str(ltcusd_viabtc))
    print('LTC ARB: ' + str(ltc_diff))
    print()
    print('ETCUSD:  ' + str(ethusd_ask))
    print('E-B-USD: ' + str(ethusd_viabtc))
    print('ETH ARB: ' + str(eth_diff))
    print()
    print('------------------------')


try:
    while True:
        display_current()
        time.sleep(1)

except KeyboardInterrupt:
    print('Exiting program.')
    sys.exit()
        
except:
    print('Exiting program with exception.')
    sys.exit()
