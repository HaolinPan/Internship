import OandaClient
import time
import datetime
import phl
def GetLogistic():
    return 0

if __name__ == "__main__":
    time1 = datetime.datetime.now()
    practice = OandaClient.Oanda("1a3db7b457b7eb5b62d0ef5810b01ef2-7f7f0bcd5f9c82bc58c210705f86d552",
        "https://api-fxpractice.oanda.com/v3/",
        "https://stream-fxpractice.oanda.com/v3/")
    ID = practice.getOandaAccount()[0]["id"]
    trailingStop = OandaClient.TrailingStopLossDetails(distance=100).GetDict()
    # print("initialize time",datetime.datetime.now() - time1)
    # time1 = datetime.datetime.now()
    # unit = 0
    # signal = GetLogistic()
    # if(signal>0.5):
    #     unit = 100
    # else:
    #     unit = -100
    # print("signal time",datetime.datetime.now() - time1)
    # time1 = datetime.datetime.now()
    # order = OandaClient.LimitOrderRequest("WTICO_USD", units = unit, trailingStopLossOnFill= trailingStop).GetDict()
    # result = practice.postOandaOrders(ID, orderRequest = order)
    # print("order time",datetime.datetime.now() - time1)
    
    # for i in range(5):
    #     print("waiting", 5-i)
    #     time.sleep(1)
    # time1 = datetime.datetime.now()
    # if(signal>0.5):
    #     practice.putOandaClosePosition(ID,"WTICO_USD",longUnits= "ALL")
    # else:
    #     practice.putOandaClosePosition(ID,"WTICO_USD",shortUnits= "ALL")
    # print("close time",datetime.datetime.now() - time1)

    transaction = 0
    rsiTrend = 0
    stopPoint = 0.2
    reSet = False
    resetThreshold = 0.15
    resetPoint = 0.05

    while(True):
        times = datetime.datetime.now()
        second = times.second
        
        if times > datetime.datetime(2019,4,17,22,30): #开始时间
            if second  % 5 == 0:
                #获取5s数据
                try:
                    candles = practice.getOandaCandles(instrument = "WTICO_USD", granularity="S5",count=5000)
                    candles['close'] = candles['close'].apply(float)
                    candles['high'] = candles['high'].apply(float)
                    candles['low'] = candles['low'].apply(float)
                    closePrice = float(candles['close'][-1])


                    #指标
                    atr = phl.ATR(candles['high'], candles['low'], candles['close'], 10)

                    ma10 = phl.SMA(candles['close'],10)
                    ma20 = phl.SMA(candles['close'],20)
                    ma40 = phl.SMA(candles['close'],40)
                    ma80 = phl.SMA(candles['close'],80)
                
                    up = ma40[-1]>ma80[-1]
                    dn = ma40[-1]<ma80[-1]

                    #进场
                    if atr[-1]>0.035 and atr[-2]<0.035:
                        if up :
                            priceDirection = 1

                        elif dn :
                            priceDirection = -1
                        else:
                            priceDirection = 0
                    else:
                        priceDirection = 0
                    
                    #仓位
                    position = practice.getOandaOpenPositions(ID)
                    try:
                        posLong = int(position[0]['long']['units'])
                        posShort = abs(int(position[0]['short']['units']))
                    except:
                        posLong = 0
                        posShort = 0

                    print('')
                    print(times)
                    print('ma40: ' + str(round(ma40[-1],4)) + '   ma80: ' + str(round(ma80[-1],4)))
                    print('up: ' + str(up) + '   dn: ' + str(dn))
                    print('ma10: ' + str(round(ma10[-1],4)) + '   ma20: ' + str(round(ma20[-1],4)))
                    print('atr: ' + str(round(atr[-1],4)))
                    print('position: ' + str(priceDirection))
                    print('long: ' + str(posLong) + '   short: ' +  str(posShort))


                    #交易
                    if priceDirection == 1 and posLong == 0:
                        if posShort > 0:
                            practice.putOandaClosePosition(ID,"WTICO_USD",shortUnits="ALL")
                            print('Cover Close')
                        order = OandaClient.LimitOrderRequest("WTICO_USD", units = 5000, price = round((closePrice + 0.1),2)).GetDict()
                        result = practice.postOandaOrders(ID, orderRequest = order)
                        transaction = closePrice
                        reSet = False
                        print("Buy Open")
                    elif priceDirection == -1 and posShort == 0:
                        if posLong > 0:
                            practice.putOandaClosePosition(ID,"WTICO_USD",longUnits="ALL")
                            print('Sell Close')
                        order = OandaClient.LimitOrderRequest("WTICO_USD", units = -5000, price = round((closePrice - 0.1),2)).GetDict()
                        result = practice.postOandaOrders(ID, orderRequest = order)
                        transaction = closePrice
                        reSet = False
                        print("Short Open")
                
                    #出场
                    if posLong == 0 and posShort == 0:
                        stopLong = 0
                        stopShort = 99999
                    

                    elif posLong > 0:
                        #止损
                        if not reSet:
                            stopLong = transaction - stopPoint
                        if closePrice >= transaction + resetThreshold:
                            reSet = True
                            stopLong = transaction + resetPoint
                            print('Reset StopPoint')
                        if (closePrice < stopLong) or (ma10[-1]<ma20[-1] and ma10[-2]>ma20[-2]):
                            print('transaction: ' + str(transaction) + '   close:' + str(closePrice))
                            practice.putOandaClosePosition(ID,"WTICO_USD",longUnits="ALL")
                            print('Long StopLoss')
                    
                        #止盈
                        if (ma10[-1]<ma20[-1] and ma10[-2]>ma20[-2]) or dn:
                            print('transaction: ' + str(transaction) + '   close:' + str(closePrice))
                            practice.putOandaClosePosition(ID,"WTICO_USD",longUnits="ALL")
                            print('Long TakeProfit')
                    

                    elif posShort > 0:
                        #止损
                        if not reSet:
                            stopShort = transaction + stopPoint
                        if closePrice <= transaction - resetThreshold:
                            reSet = True
                            stopShort = transaction - resetPoint
                            print('Reset StopPoint')
                        if (closePrice > stopShort) or (ma10[-1]>ma20[-1] and ma10[-2]<ma20[-2]):
                            print('transaction: ' + str(transaction) + '   close:' + str(closePrice))
                            practice.putOandaClosePosition(ID,"WTICO_USD",shortUnits="ALL")
                            print('Short StopLoss')
                    
                        #止盈
                        if (ma10[-1]>ma20[-1] and ma10[-2]<ma20[-2]) or up:
                            print('transaction: ' + str(transaction) + '   close:' + str(closePrice))
                            practice.putOandaClosePosition(ID,"WTICO_USD",shortUnits="ALL")
                            print('Short TakeProfit')
                except:
                    pass
                
            if times > datetime.datetime(2019,4,17,23,00): #结束时间
                if posLong > 0:
                    practice.putOandaClosePosition(ID,"WTICO_USD",longUnits="ALL")
                if posShort > 0:
                    practice.putOandaClosePosition(ID,"WTICO_USD",shortUnits="ALL")
                print('time out')
                break

        
        time.sleep(1)

    
