import GDAX
import json
import sys

publicClient = GDAX.PublicClient()

global bidBU, bidBUVol, askBU, askBUVol
global bidLU, bidLUVol, askLU, askLUVol
global bidEU, bidEUVol, askEU, askEUVol
global bidLB, bidLBVol, askLB, askLBVol
global bidEB, bidEBVol, askEB, askEBVol


def getBooks():
    global bidBU, bidBUVol, askBU, askBUVol
    global bidLU, bidLUVol, askLU, askLUVol
    global bidEU, bidEUVol, askEU, askEUVol
    global bidLB, bidLBVol, askLB, askLBVol
    global bidEB, bidEBVol, askEB, askEBVol

    bookBU = publicClient.getProductOrderBook(level=1, product='BTC-USD')
    bidBU = float(bookBU['bids'][0][0])
    bidBUVol = float(bookBU['bids'][0][1])
    askBU = float(bookBU['asks'][0][0])
    askBUVol = float(bookBU['asks'][0][1])

    bookLU = publicClient.getProductOrderBook(level=1, product='LTC-USD')
    bidLU = float(bookLU['bids'][0][0])
    bidLUVol = float(bookLU['bids'][0][1])
    askLU = float(bookLU['asks'][0][0])
    askLUVol = float(bookLU['asks'][0][1])

    bookEU = publicClient.getProductOrderBook(level=1, product='ETH-USD')
    bidEU = float(bookEU['bids'][0][0])
    bidEUVol = float(bookEU['bids'][0][1])
    askEU = float(bookEU['asks'][0][0])
    askEUVol = float(bookEU['asks'][0][1])

    bookLB = publicClient.getProductOrderBook(level=1, product='LTC-BTC')
    bidLB = float(bookLB['bids'][0][0])
    bidLBVol = float(bookLB['bids'][0][1])
    askLB = float(bookLB['asks'][0][0])
    askLBVol = float(bookLB['asks'][0][1])

    bookEB = publicClient.getProductOrderBook(level=1, product='ETH-BTC')
    bidEB = float(bookEB['bids'][0][0])
    bidEBVol = float(bookEB['bids'][0][1])
    askEB = float(bookEB['asks'][0][0])
    askEBVol = float(bookEB['asks'][0][1])


print('Beginning program. Press \"ctrl + c\" to quit.')

try:
    while True:
        getBooks()
        print(bidEU)

except KeyboardInterrupt:
    print('Quitting program.')
    sys.exit()
