'''

Wheel built for Oanda Api v20

All rights reserved.

_(:з」∠)_

2019-3-14 12:44:46
'''

import pandas as pd
from datetime import datetime, timedelta
import requests
import json
import abc

# OrderRequest
# Finished 2019-3-15 10:53:32


class OrderRequest(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def GetDict(self):
        pass

    @abc.abstractmethod
    def GetJson(self):
        pass


class MarketOrderRequest(OrderRequest):
    '''
        A MarketOrderRequest specifies the parameters that may be set when creating a Market Order.
    '''

    def __init__(self, instrument: str, units: float,
                 timeInForce="FOK", priceBound=None,  positionFill="DEFAULT", clientExtensions=None, takeProfitOnFill=None,
                 stopLossOnFill=None,trailingStopLossOnFill =None, tradeClientExtensions=None):

        self.request_dict = dict()
        self.request_dict["type"] = "MARKET"
        self.request_dict["instrument"] = instrument
        self.request_dict["units"] = str(units)
        self.request_dict["timeInForce"] = timeInForce
        if(priceBound != None):
            self.request_dict["priceBound"] = str(priceBound)
        self.request_dict["positionFill"] = positionFill
        if(clientExtensions != None):
            self.request_dict["clientExtensions"] = clientExtensions
        if(takeProfitOnFill != None):
            self.request_dict["takeProfitOnFill"] = takeProfitOnFill
        if(stopLossOnFill != None):
            self.request_dict["stopLossOnFill"] = stopLossOnFill
        if(trailingStopLossOnFill != None):
            self.request_dict["trailingStopLossOnFill"] = trailingStopLossOnFill
        if(tradeClientExtensions != None):
            self.request_dict["tradeClientExtensions"] = tradeClientExtensions
        self.request_Object = json.dumps(self.request_dict)

    def GetDict(self):
        return self.request_dict

    def GetJson(self):
        return self.request_Object


class LimitOrderRequest(OrderRequest):
    '''
        A LimitOrderRequest specifies the parameters that may be set when creating a Limit Order.
    '''

    def __init__(self, instrument: str, units: float, price: float,
                 timeInForce="GTC", gtdTime=None, positionFill="DEFAULT", triggerCondition="DEFAULT",
                 clientExtensions=None, takeProfitOnFill=None,
                 stopLossOnFill=None, tradeClientExtensions=None):

        self.request_dict = dict()
        self.request_dict["type"] = "LIMIT"
        self.request_dict["instrument"] = instrument
        self.request_dict["units"] = str(units)
        self.request_dict["price"] = str(price)
        self.request_dict["timeInForce"] = timeInForce
        if(gtdTime != None):
            self.request_dict["gtdTime"] = str(gtdTime)
        self.request_dict["positionFill"] = positionFill
        self.request_dict["triggerCondition"] = triggerCondition
        if(clientExtensions != None):
            self.request_dict["clientExtensions"] = clientExtensions
        if(takeProfitOnFill != None):
            self.request_dict["takeProfitOnFill"] = takeProfitOnFill
        if(stopLossOnFill != None):
            self.request_dict["stopLossOnFill"] = stopLossOnFill
        if(tradeClientExtensions != None):
            self.request_dict["tradeClientExtensions"] = tradeClientExtensions
        self.request_Object = json.dumps(self.request_dict)

    def GetDict(self):
        return self.request_dict

    def GetJson(self):
        return self.request_Object


class StopOrderRequest(OrderRequest):
    '''
        StopOrderRequest specifies the parameters that may be set when creating a Stop Order.
    '''

    def __init__(self, instrument: str, units: float, price: float,
                 priceBound=None, timeInForce="GTC", gtdTime=None, positionFill="DEFAULT", triggerCondition="DEFAULT",
                 clientExtensions=None, takeProfitOnFill=None,
                 stopLossOnFill=None, tradeClientExtensions=None):

        self.request_dict = dict()
        self.request_dict["type"] = "STOP"
        self.request_dict["instrument"] = instrument
        self.request_dict["units"] = str(units)
        self.request_dict["price"] = str(price)
        if(priceBound != None):
            self.request_dict["priceBound"] = str(priceBound)
        self.request_dict["timeInForce"] = timeInForce
        if(gtdTime != None):
            self.request_dict["gtdTime"] = str(gtdTime)
        self.request_dict["positionFill"] = positionFill
        self.request_dict["triggerCondition"] = triggerCondition
        if(clientExtensions != None):
            self.request_dict["clientExtensions"] = clientExtensions
        if(takeProfitOnFill != None):
            self.request_dict["takeProfitOnFill"] = takeProfitOnFill
        if(stopLossOnFill != None):
            self.request_dict["stopLossOnFill"] = stopLossOnFill
        if(tradeClientExtensions != None):
            self.request_dict["tradeClientExtensions"] = tradeClientExtensions
        self.request_Object = json.dumps(self.request_dict)

    def GetDict(self):
        return self.request_dict

    def GetJson(self):
        return self.request_Object


class MarketIfTouchedOrderRequest(OrderRequest):
    '''
        A MarketIfTouchedOrderRequest specifies the parameters that may be set when creating a Market-if-Touched Order.
    '''

    def __init__(self, instrument: str, units: float, price: float,
                 priceBound=None, timeInForce="GTC", gtdTime=None, positionFill="DEFAULT", triggerCondition="DEFAULT",
                 clientExtensions=None, takeProfitOnFill=None,
                 stopLossOnFill=None, tradeClientExtensions=None):

        self.request_dict = dict()
        self.request_dict["type"] = "MARKET_IF_TOUCHED"
        self.request_dict["instrument"] = instrument
        self.request_dict["units"] = str(units)
        self.request_dict["price"] = str(price)
        if(priceBound != None):
            self.request_dict["priceBound"] = str(priceBound)
        self.request_dict["timeInForce"] = timeInForce
        if(gtdTime != None):
            self.request_dict["gtdTime"] = str(gtdTime)
        self.request_dict["positionFill"] = positionFill
        self.request_dict["triggerCondition"] = triggerCondition
        if(clientExtensions != None):
            self.request_dict["clientExtensions"] = clientExtensions
        if(takeProfitOnFill != None):
            self.request_dict["takeProfitOnFill"] = takeProfitOnFill
        if(stopLossOnFill != None):
            self.request_dict["stopLossOnFill"] = stopLossOnFill
        if(tradeClientExtensions != None):
            self.request_dict["tradeClientExtensions"] = tradeClientExtensions
        self.request_Object = json.dumps(self.request_dict)

    def GetDict(self):
        return self.request_dict

    def GetJson(self):
        return self.request_Object


class TakeProfitOrderRequest(OrderRequest):
    '''
        A TakeProfitOrderRequest specifies the parameters that may be set when creating a Take Profit Order. 
        Only one of the price and distance fields may be specified.
    '''

    def __init__(self, tradeID: str,  price: float,
                 clientTradeID=None, timeInForce="GTC", gtdTime=None, triggerCondition="DEFAULT",
                 clientExtensions=None):

        self.request_dict = dict()
        self.request_dict["type"] = "TAKE_PROFIT"
        self.request_dict["tradeID"] = tradeID
        if(clientTradeID != None):
            self.request_dict["clientTradeID"] = clientTradeID
        self.request_dict["price"] = str(price)
        self.request_dict["timeInForce"] = timeInForce
        if(gtdTime != None):
            self.request_dict["gtdTime"] = str(gtdTime)
        self.request_dict["triggerCondition"] = triggerCondition
        if(clientExtensions != None):
            self.request_dict["clientExtensions"] = clientExtensions
        self.request_Object = json.dumps(self.request_dict)

    def GetDict(self):
        return self.request_dict

    def GetJson(self):
        return self.request_Object


class StopLossOrderRequest(OrderRequest):
    '''
        A StopLossOrderRequest specifies the parameters that may be set when creating a Stop Loss Order. 
        Only one of the price and distance fields may be specified.
    '''

    def __init__(self, tradeID: str, price: float,
                 clientTradeID=None, distance=None, timeInForce="GTC", gtdTime=None, triggerCondition="DEFAULT",
                 guaranteed=None, clientExtensions=None):

        self.request_dict = dict()
        self.request_dict["type"] = "STOP_LOSS"
        self.request_dict["tradeID"] = tradeID
        if(clientTradeID != None):
            self.request_dict["clientTradeID"] = clientTradeID
        self.request_dict["price"] = str(price)
        if(distance != None):
            self.request_dict["distance"] = str(distance)
        self.request_dict["timeInForce"] = timeInForce
        if(gtdTime != None):
            self.request_dict["gtdTime"] = str(gtdTime)
        self.request_dict["triggerCondition"] = triggerCondition
        if(guaranteed != None):
            self.request_dict["guaranteed"] = str(guaranteed)
        if(clientExtensions != None):
            self.request_dict["clientExtensions"] = clientExtensions
        self.request_Object = json.dumps(self.request_dict)

    def GetDict(self):
        return self.request_dict

    def GetJson(self):
        return self.request_Object


class TrailingStopLossOrderRequest(OrderRequest):
    def __init__(self, tradeID: str, distance: float,
                 clientTradeID=None, timeInForce="GTC", gtdTime=None, triggerCondition="DEFAULT",
                 clientExtensions=None):
        '''
            A TrailingStopLossOrderRequest specifies the parameters that may be set when creating a Trailing Stop Loss Order.
        '''
        self.request_dict = dict()
        self.request_dict["type"] = "TRAILING_STOP_LOSS"
        self.request_dict["tradeID"] = tradeID
        if(clientTradeID != None):
            self.request_dict["clientTradeID"] = clientTradeID
        self.request_dict["distance"] = str(distance)
        self.request_dict["timeInForce"] = timeInForce
        if(gtdTime != None):
            self.request_dict["gtdTime"] = str(gtdTime)
        self.request_dict["triggerCondition"] = triggerCondition
        if(clientExtensions != None):
            self.request_dict["clientExtensions"] = clientExtensions
        self.request_Object = json.dumps(self.request_dict)

    def GetDict(self):
        return self.request_dict

    def GetJson(self):
        return self.request_Object

# OrderDetail
# Finished 2019-3-15 10:54:02


class OrderDetail(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def GetDict(self):
        pass

    @abc.abstractmethod
    def GetJson(self):
        pass


class TakeProfitDetails(OrderDetail):
    def __init__(self, price=None, distance = None,
                 timeInForce="GTC", gtdTime=None, clientExtensions=None):
        '''
            TakeProfitDetails specifies the details of a Take Profit Order to be created on behalf of a client. 
            This may happen when an Order is filled that opens a Trade requiring a Take Profit, or when a Trade’s dependent Take Profit Order is modified directly through the Trade.
        '''
        self.detail_dict = dict()
        if(price != None):
            self.detail_dict["price"] = str(price)
        if(distance != None):
            self.detail_dict["distance"] = str(distance)    
        self.detail_dict["timeInForce"] = timeInForce
        if(gtdTime != None):
            self.detail_dict["gtdTime"] = str(gtdTime)
        if(clientExtensions != None):
            self.detail_dict["clientExtensions"] = clientExtensions
        self.detail_Onject = json.dumps(self.detail_dict)

    def GetDict(self):
        return self.detail_dict

    def GetJson(self):
        return self.detail_Onject


class StopLossDetails(OrderDetail):
    def __init__(self, price=None,
                 clientTradeID=None, distance=None, timeInForce="GTC", gtdTime=None,
                 guaranteed=None, clientExtensions=None):
        '''
            StopLossDetails specifies the details of a Stop Loss Order to be created on behalf of a client. 
            This may happen when an Order is filled that opens a Trade requiring a Stop Loss, or when a Trade’s dependent Stop Loss Order is modified directly through the Trade.
        '''
        self.detail_dict = dict()

        if(price != None):
            self.detail_dict["price"] = str(price)
        if(distance != None):
            self.detail_dict["distance"] = str(distance)
        self.detail_dict["timeInForce"] = timeInForce
        if(gtdTime != None):
            self.detail_dict["gtdTime"] = str(gtdTime)
        if(guaranteed != None):
            self.detail_dict["guaranteed"] = str(guaranteed)
        if(clientExtensions != None):
            self.detail_dict["clientExtensions"] = clientExtensions
        self.detail_Onject = json.dumps(self.detail_dict)

    def GetDict(self):
        return self.detail_dict

    def GetJson(self):
        return self.detail_Onject


class TrailingStopLossDetails(OrderDetail):
    def __init__(self, distance=None,
                 timeInForce="GTC", gtdTime=None,
                 clientExtensions=None):
        '''
            TrailingStopLossDetails specifies the details of a Trailing Stop Loss Order to be created on behalf of a client. 
            This may happen when an Order is filled that opens a Trade requiring a Trailing Stop Loss, or when a Trade’s dependent Trailing Stop Loss Order is modified directly through the Trade.
        '''
        self.detail_dict = dict()
        if(distance != None):
            self.detail_dict["distance"] = str(distance)
        self.detail_dict["timeInForce"] = timeInForce
        if(gtdTime != None):
            self.detail_dict["gtdTime"] = str(gtdTime)
        if(clientExtensions != None):
            self.detail_dict["clientExtensions"] = clientExtensions
        self.detail_Onject = json.dumps(self.detail_dict)

    def GetDict(self):
        return self.detail_dict

    def GetJson(self):
        return self.detail_Onject


class Oanda:

    # Initialization

    def __init__(self, access: str, restApiUrl: str, streamApiUrl: str):
        self.accessID = access
        self.restApi = restApiUrl
        self.streamApi = streamApiUrl
        return

    # Accounts
    # Finished 2019-3-14 15:41:43

    def getOandaAccount(self):
        '''
            Get a list of all Accounts authorized for the provided token.

            return:
            dictionary<int, dictionary<string, string>>

            Tested 2019-3-14 12:23:05
        '''
        url = self.restApi + "accounts"
        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}
        r = requests.get(url, headers=headers, params=None, timeout=10)
        accounts = dict()
        if(r.status_code == 200):
            text = json.loads(r.content)
            accounts = text["accounts"]
        else:
            print("Error " + str(r.status_code) + ": " + r.text)
            return
        return accounts

    def getOandaAccountDetail(self, accountID: str):
        '''
            Get the full details for a single Account that a client has access to. 
            Full pending Order, open Trade and open Position representations are provided.

            return:
            dictionary<string, value>

            Tested 2019-3-14 12:23:05
        '''
        url = self.restApi + "accounts/" + accountID
        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}
        r = requests.get(url, headers=headers, params=None, timeout=10)
        detail = dict()
        if(r.status_code == 200):
            text = json.loads(r.content)
            detail = text["account"]
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return detail

    def getOandaAccountSummary(self, accountID: str):
        '''
            Get a summary for a single Account that a client has access to.

            return:
            dictionary<string, value>

            Tested 2019-3-14 12:23:05
        '''
        url = self.restApi + "accounts/" + accountID + "/summary"
        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}
        r = requests.get(url, headers=headers, params=None, timeout=10)
        Summary = dict()
        if(r.status_code == 200):
            text = json.loads(r.content)
            Summary = text["account"]
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return Summary

    def getOandaAccountInstruments(self, accountID: str):
        '''
            Get the list of tradeable instruments for the given Account. 
            The list of tradeable instruments is dependent on the regulatory division that the Account is located in, 
            thus should be the same for all Accounts owned by a single user.

            return:
            pandas.DataFrame

            Tested 2019-3-14 12:24:29
        '''
        url = self.restApi + "accounts/" + accountID + "/instruments"
        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}
        r = requests.get(url, headers=headers, params=None, timeout=10)
        Instruments = pd.DataFrame()
        if(r.status_code == 200):
            text = json.loads(r.content)
            Instruments = pd.DataFrame(text["instruments"])
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return Instruments

    def patchOandaConfiguration(self, accountID: str, alias=None, marginRate=None):
        '''
            Set the client-configurable portions of an Account.

            return:
            dictionary<string, value>

            Tested: 2019-3-14 15:31:11
        '''
        url = self.restApi + "accounts/" + accountID + "/configuration"

        data_dict = dict()
        if(alias != None):
            data_dict["alias"] = alias
        if(marginRate != None):
            data_dict["marginRate"] = str(marginRate)
        data = json.dumps(data_dict)

        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}

        r = requests.patch(url, data=data, headers=headers)

        if(r.status_code == 200):
            text = json.loads(r.content)
            Configuration = text["clientConfigureTransaction"]
            return Configuration
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
        return

    def getOandaChanges(self, accountID: str, sinceTransactionID: str):
        '''
            Endpoint used to poll an Account for its current state and changes since a specified TransactionID.

            return:
            dictionary<string, value>

            Tested: 2019-3-14 15:41:06
        '''
        # TODO
        url = self.restApi + "accounts/" + accountID + "/changes"
        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}
        params = {"sinceTransactionID": sinceTransactionID}
        r = requests.get(url, headers=headers, params=params, timeout=10)
        Changes = dict()
        if(r.status_code == 200):
            text = json.loads(r.content)
            Changes = text["changes"]
            return Changes
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return

    # Instruments

    def getOandaCandles(self, instrument: str,
                        price="M", granularity="S5", count=None,
                        time_from=None, time_to=None, smooth=True, includeFirst=True,
                        dailyAlignment=17, alignmentTimezone="America/New_York", weeklyAlignment="Friday"):
        '''
            Fetch candlestick data for an instrument.

            Price：The Price component(s) to get candlestick data for. 
            Can contain any combination of the characters “M” (midpoint candles) “B” (bid candles) and “A” (ask candles). 
            [default=M]

            Granularity：The granularity of the candlesticks to fetch 
            [default=S5]

            Count：The number of candlesticks to return in the reponse. 
            Count should not be specified if both the start and end parameters are provided, 
            as the time range combined with the graularity will determine the number of candlesticks to return. 
            [default=500, maximum=5000]

            From：The start of the time range to fetch candlesticks for.

            To：The end of the time range to fetch candlesticks for.

            Smooth：A flag that controls whether the candlestick is “smoothed” or not. 
            A smoothed candlestick uses the previous candle’s close price as its open price, 
            while an unsmoothed candlestick uses the first price from its time range as its open price. 
            [default=False]

            IncludeFirst：A flag that controls whether the candlestick that is covered by the from time should be included in the results. 
            This flag enables clients to use the timestamp of the last completed candlestick received to poll for future candlesticks but avoid receiving the previous candlestick repeatedly. 
            [default=True]

            DailyAlignment：The hour of the day (in the specified timezone) to use for granularities that have daily alignments. 
            [default=17, minimum=0, maximum=23]

            AlignmentTimezone：The timezone to use for the dailyAlignment parameter. 
            Candlesticks with daily alignment will be aligned to the dailyAlignment hour within the alignmentTimezone. 
            Note that the returned times will still be represented in UTC. 
            [default=America/New_York]

            WeeklyAlignment：The day of the week used for granularities that have weekly alignment. 
            [default=Friday]


            return:
            pandas.DataFrame
        '''

        params_dict = dict()
        params_dict["price"] = price
        params_dict["granularity"] = granularity
        if(count != None):
            params_dict["count"] = count
        if(time_from != None):
            params_dict["from"] = time_from
        if(time_to != None):
            params_dict["to"] = time_to
        params_dict["smooth"] = smooth
        params_dict["includeFirst"] = includeFirst
        params_dict["dailyAlignment"] = str(dailyAlignment)
        params_dict["alignmentTimezone"] = alignmentTimezone
        params_dict["weeklyAlignment"] = weeklyAlignment
        params = json.dumps(params_dict)

        url = self.restApi + "instruments/" + instrument + "/candles"

        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}

        r = requests.get(url, headers=headers, params=params, timeout=10)

        candle_df = pd.DataFrame()
        if(r.status_code == 200):
            text = json.loads(r.content)
            data = pd.DataFrame(text["candles"])
            candles = dict()
            candles["high"] = dict()
            candles["close"] = dict()
            candles["low"] = dict()
            candles["open"] = dict()
            for i in range(0, len(data["mid"])):
                candles["high"][i] = data["mid"][i]['h']
                candles["close"][i] = data["mid"][i]['c']
                candles["low"][i] = data["mid"][i]['l']
                candles["open"][i] = data["mid"][i]['o']
            candle_df = pd.DataFrame(candles)
            candle_df["datetime"] = data["time"].apply(pd.to_datetime)
            candle_df = candle_df.set_index("datetime")
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return candle_df

    def getOandaOrderbook(self, instrument, time=None):
        '''
            Fetch an order book for an instrument.

            return:
            pandas.DataFrame

            Tested 2019-3-14 12:26:28
        '''
        params = dict()
        if(time != None):
            params = {"time": time}
        else:
            params = None
        url = self.restApi + "instruments/" + instrument + "/orderBook"
        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}
        r = requests.get(url, headers=headers, params=params, timeout=10)
        orderbook = pd.DataFrame()
        if(r.status_code == 200):
            text = json.loads(r.content)
            orderbook = pd.DataFrame(text["orderBook"]["buckets"])
            return orderbook
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return

    def getOandaPositionbook(self, instrument, time=None):
        '''
            Fetch an position book for an instrument.

            return:
            pandas.DataFrame

            Tested 2019-3-14 12:26:41
        '''
        if(time != None):
            params = {"time": time}
        else:
            params = None
        url = self.restApi + "instruments/" + instrument + "/positionBook"
        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}
        r = requests.get(url, headers=headers, params=params, timeout=10)
        positionbook = pd.DataFrame()
        if(r.status_code == 200):
            text = json.loads(r.content)
            positionbook = pd.DataFrame(text["positionBook"]["buckets"])
            return positionbook
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
        return

    # Order
    # The instruction to buy or sell a currency at a specified rate.
    # The order remains valid until executed or cancelled.

    def postOandaOrders(self, accountID: str, orderRequest: str):
        '''
            Create an Order for an Account
        '''
        url = self.restApi + "accounts/" + accountID + "/orders"

        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}

        data_dict = dict()
        data_dict["order"] = orderRequest

        data = json.dumps(data_dict)

        r = requests.post(url, headers=headers, data=data, timeout=10)

        if(r.status_code == 201):
            text = json.loads(r.content)
            return text
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
        return

    def getOandaOrders(self, accountID: str,
                       ids=None, state="PENDING", instrument=None,
                       count=50, beforeID=None):
        '''
            Get a list of Orders for an Account
        '''

        params_dict = dict()
        if(ids != None):
            params_dict["ids"] = ids
        params_dict["state"] = state
        if(instrument != None):
            params_dict["instrument"] = instrument
        params_dict["count"] = str(count)
        params_dict["beforeID"] = str(beforeID)
        params = json.dumps(params_dict)

        url = self.restApi + "accounts/" + accountID + "/orders"

        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}

        r = requests.get(url, headers=headers, params=params, timeout=10)

        if(r.status_code == 200):
            text = json.loads(r.content)
            orders = text["orders"]
            return orders
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return

    def getOandaPendingOrders(self, accountID: str):
        '''
            List all pending Orders in an Account
        '''
        url = self.restApi + "accounts/" + accountID + "/pendingOrders"

        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}

        r = requests.get(url, headers=headers, params=None, timeout=10)

        if(r.status_code == 200):
            text = json.loads(r.content)
            orders = text["orders"]
            return orders
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return

    def getOandaOrder(self, accountID: str, orderID: str):
        '''
            Get details for a single Order in an Account
        '''
        url = self.restApi + "accounts/" + \
            accountID + "/orders/" + str(orderID)

        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}

        r = requests.get(url, headers=headers, params=None, timeout=10)

        if(r.status_code == 200):
            text = json.loads(r.content)
            orders = text["orders"]
            return orders
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return

    def putOandaOrderReplace(self, accountID: str, orderID: str, orderRequest: str):
        '''
            Replace an Order in an Account by simultaneously cancelling it and creating a replacement Order
        '''
        url = self.restApi + "accounts/" + \
            accountID + "/orders/" + str(orderID)

        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}

        data_dict = dict()
        data_dict["order"] = orderRequest

        data = json.dumps(data_dict)

        r = requests.put(url, headers=headers, data=data, timeout=10)

        if(r.status_code == 201):
            text = json.loads(r.content)
            return text
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
        return

    def putOandaCancelOrder(self, accountID: str, orderID: str,):
        '''
            Cancel a pending Order in an Account
        '''
        url = self.restApi + "accounts/" + accountID + \
            "/orders/" + str(orderID) + "/cancel"

        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}

        r = requests.put(url, headers=headers, timeout=10)

        if(r.status_code == 200):
            text = json.loads(r.content)
            return text
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
        return

    def putOandaOrderClientExtensions(self):
        '''
            Update the Client Extensions for an Order in an Account. 
            Do not set, modify, or delete clientExtensions if your account is associated with MT4.
        '''
        return

    # Trade
    # The execution of the order.

    def getOandaTrades(self, accountID: str,
                       ids=None, state="OPEN", instrument=None, count=50, beforeID=None):
        '''
            Get a list of Trades for an Account
        '''
        params_dict = dict()
        if(ids != None):
            params_dict["ids"] = ids
        params_dict["state"] = state
        if(instrument != None):
            params_dict["instrument"] = instrument
        params_dict["count"] = str(count)
        params_dict["beforeID"] = str(beforeID)
        params = json.dumps(params_dict)

        url = self.restApi + "accounts/" + accountID + "/trades"

        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}

        r = requests.get(url, headers=headers, params=params, timeout=10)

        if(r.status_code == 200):
            text = json.loads(r.content)
            trades = text["trades"]
            return trades
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return

    def getOandaOpenTrades(self, accountID: str):
        '''
            Get the list of open Trades for an Account
        '''
        url = self.restApi + "accounts/" + accountID + "/openTrades"

        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}

        r = requests.get(url, headers=headers, params=None, timeout=10)

        if(r.status_code == 200):
            text = json.loads(r.content)
            trades = text["trades"]
            return trades
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return

    def getOandaTradeDetail(self, accountID: str, tradeID: str):
        '''
            Get the details of a specific Trade in an Account
        '''
        url = self.restApi + "accounts/" + \
            accountID + "/trades/" + str(tradeID)

        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}

        r = requests.get(url, headers=headers, params=None, timeout=10)

        if(r.status_code == 200):
            text = json.loads(r.content)
            trades = text["trade"]
            return trades
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return

    def putOandaCloseTrade(self):
        '''
            Close (partially or fully) a specific open Trade in an Account
        '''
        return

    def putOandaTradeClientExtensions(self):
        '''
            Update the Client Extensions for a Trade. 
            Do not add, update, or delete the Client Extensions if your account is associated with MT4.
        '''
        return

    def putOandaTradeOrder(self):
        '''
            Create, replace and cancel a Trade’s dependent Orders 
            (Take Profit, Stop Loss and Trailing Stop Loss) through the Trade itself
        '''
        return

    # Position
    # The total of all trades for a specific market.

    def getOandaPositions(self, accountID: str):
        '''
            List all Positions for an Account. 
            The Positions returned are for every instrument that has had a position during the lifetime of an the Account.
        '''
        url = self.restApi + "accounts/" + accountID + "/positions"

        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}

        r = requests.get(url, headers=headers, params=None, timeout=10)

        if(r.status_code == 200):
            text = json.loads(r.content)
            positions = text["positions"]
            return positions
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return

    def getOandaOpenPositions(self, accountID: str):
        '''
            List all open Positions for an Account. 
            An open Position is a Position in an Account that currently has a Trade opened for it.
        '''
        url = self.restApi + "accounts/" + accountID + "/openPositions"

        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}

        r = requests.get(url, headers=headers, params=None, timeout=10)

        if(r.status_code == 200):
            text = json.loads(r.content)
            positions = text["positions"]
            return positions
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return

    def getOandaSinglePosition(self, accountID: str):
        '''
            Get the details of a single Instrument’s Position in an Account. 
            The Position may by open or not.
        '''
        url = self.restApi + "accounts/" + accountID + "/openPositions"

        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}

        r = requests.get(url, headers=headers, params=None, timeout=10)

        if(r.status_code == 200):
            text = json.loads(r.content)
            positions = text["positions"]
            return positions
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return

    def putOandaClosePosition(self, accountID: str, instrument: str,
                              longUnits=None, longClientExtensions=None,
                              shortUnits=None, shortClientExtensions=None):
        '''
            Closeout the open Position for a specific instrument in an Account.
        '''
        url = self.restApi + "accounts/" + accountID + \
            "/positions/" + instrument + "/close"

        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}

        data_dict = dict()
        if(longUnits != None):
            data_dict["longUnits"] = str(longUnits)
        if(shortUnits != None):
            data_dict["shortUnits"] = str(shortUnits)
        if(longClientExtensions != None):
            data_dict["longClientExtensions"] = longClientExtensions
        if(shortClientExtensions != None):
            data_dict["longClientExtensions"] = shortClientExtensions
        
        data = json.dumps(data_dict)

        r = requests.put(url,data = data, headers = headers)

        if(r.status_code == 200):
            text = json.loads(r.content)
            return text
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return

    # Transaction

    def getOandaTransactions(self, accountID: str,
                             time_from=None, time_to=None, pageSize=100):
        '''
            Get a list of Transactions pages that satisfy a time-based Transaction query.        
        '''
        params = {"pageSize": pageSize, }
        url = self.restApi + "accounts/"+accountID+"/transactions"
        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}
        r = requests.get(url, headers=headers, params=params, timeout=10)
        if(r.status_code == 200):
            text = json.loads(r.content)
            pagestrart = text['pages'][0].split(
                '?')[1].split('&')[0].split('=')[1]
            pageend = text['pages'][0].split('?')[1].split('=')[2]
            pagelist = [int(pagestrart), int(pageend)]
            return (pagelist)
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return

    def getOandaTransactionDetail(self, accountID: str, transactionID: str):
        '''
            Get the details of a single Account Transaction.
        '''
        url = self.restApi + "accounts/"+accountID + \
            "/transactions/"+str(transactionID)
        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}
        r = requests.get(url, headers=headers, timeout=10)
        if(r.status_code == 200):
            text = json.loads(r.content)
            return text
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return

    def getOandaTransactionsIDRange(self, accountID: str, ID_from: str, ID_to: str):
        '''
            Get a range of Transactions for an Account based on the Transaction IDs.
        '''
        params = {"from": ID_from, "to": ID_to}
        url = self.restApi + "accounts/"+accountID+"/transactions/idrange"
        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}
        r = requests.get(url, headers=headers, params=params, timeout=10)
        if(r.status_code == 200):
            text = json.loads(r.content)
            return text
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return
# 解析json

    def getOandaTransactionsSinceID(self, accountID: str, ID: str):
        '''
            Get a range of Transactions for an Account starting at (but not including) a provided 
        '''
        params = {"id": ID}
        url = self.restApi + "accounts/"+accountID+"/transactions/sinceid"
        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}
        r = requests.get(url, headers=headers, params=params, timeout=10)
        if(r.status_code == 200):
            text = json.loads(r.content)
            return text
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return
# 问题

    def getOandaTransactionsStream(self, accountID: str):
        '''
            Get a stream of Transactions for an Account starting from when the request is made.

            Note: This endpoint is served by the streaming URLs.
        '''
        url = self.restApi + "accounts/"+accountID+"/transactions/stream"
        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}
        r = requests.get(url, headers=headers, timeout=10)
        return r.status_code

    # Priceing

    def getOandaPricing(self, accountID: str, instruments: str, since: str, includeUnitsAvailable=True, ncludeHomeConversions=False):
        '''
            Get pricing information for a specified list of Instruments within an Account.
        '''
        params = {"instruments": instruments, "since": since,
                  "includeUnitsAvailable": includeUnitsAvailable, "ncludeHomeConversions": ncludeHomeConversions}
        url = self.restApi + "accounts/"+accountID+"/pricing"
        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}
        r = requests.get(url, headers=headers, params=params, timeout=10)
        text = dict()
        if(r.status_code == 200):
            text = json.loads(r.content)
            bids = []
            asks = []
            for i in range(len(text['prices'])):
                bids.append(text['prices'][i]['bids'])
                asks.append(text['prices'][i]['asks'])
            a = pd.DataFrame(bids[0])
            b = pd.DataFrame(asks[0])
            res = {"bids": a, "asks": b, 'closeoutBid': '1298.377', 'closeoutAsk': '1299.827', 'status': 'tradeable',
                   'tradeable': True, 'unitsAvailable': {'default': {'long': '3848', 'short': '3848'},
                                                         'openOnly': {'long': '3848', 'short': '3848'}, 'reduceFirst': {'long': '3848', 'short': '3848'},
                                                         'reduceOnly': {'long': '0', 'short': '0'}}, 'quoteHomeConversionFactors': {'positiveUnits': '1.00000000', 'negativeUnits': '1.00000000'},
                   'instrument': 'XAU_USD'}
            return res
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return
# 问题

    def getOandaPricingStream(self, accountID: str, instruments: str, snapshot=True):
        params = {"instruments": instruments, "snapshot": snapshot}
        url = self.streamApi + "accounts/"+accountID+"/pricing/streaming"
        headers = {"Authorization": "Bearer " +
                   self.accessID, "Content-Type": "application/json"}
        r = requests.get(url, headers=headers, params=params, timeout=10)
        if(r.status_code == 200):
            text = json.loads(r.content)
            return text
        else:
            print("Error" + str(r.status_code) + ": " + r.text)
            return
        return


# print(getOandaPriceing(ID))
