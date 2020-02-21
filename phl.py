
# coding: utf-8

import pandas as pd
import numpy as np


#指标库
def EMA(close, timePeriod=20):
    ema = pd.Series(close.ewm(span=timePeriod, min_periods=timePeriod).mean(), name='EMA_' + str(timePeriod))
    return ema

def SMA(close, timePeriod=20):
    sma = pd.Series(close.rolling(timePeriod, min_periods=timePeriod).mean(), name='SMA_' + str(timePeriod))
    return sma

def STD(close, timePeriod=20):
    std = pd.Series(close.rolling(timePeriod, min_periods=timePeriod).std(), name='STD_' + str(timePeriod))
    return std

def RSI(close, timePeriod=14):
    #N日RSI = N日内收盘涨幅的平均值 / (N日内收盘涨幅均值 + N日内收盘跌幅均值) ×100
    upDif = close - close.shift(1)
    upDif[np.isnan(upDif)]=0
    upDif[upDif<0]=0
    dnDif = close - close.shift(1)
    dnDif[np.isnan(dnDif)]=0
    dnDif[dnDif>0]=0
    dnDif = abs(dnDif)

    rs = EMA(upDif, timePeriod)/EMA(dnDif, timePeriod)
    rsi = 100 - 100/(1+rs)
    rsi = pd.Series(rsi, name='RSI_' + str(timePeriod))
    return rsi

def STOCHRSI(close, rsiPeriod=14, prePeriod=14, kPeriod=3, dPeriod=3):
    #StochRSI = (RSI - Lowest Low RSI) / (Highest High RSI - Lowest Low RSI)
    rsi = RSI(close, rsiPeriod)
    h = rsi.rolling(rsiPeriod).max()
    l = rsi.rolling(rsiPeriod).min()
    k = EMA((rsi-l)/kPeriod)/EMA((h-l)/kPeriod) * 100
    d = EMA(k, dPeriod)
    k = pd.Series(k, name='k')
    d = pd.Series(d, name='d')
    return k, d
        
def CCI(high, low, close, timePeriod=14):
    #TP =（最高价 + 最低价 + 收盘价）÷3
    tp = (high + low + close)/3
    #MA = 最近n日(TP)价的累计和÷n
    ma = SMA(tp,timePeriod)
    #MD = 最近n日 (MA - TP)的绝对值的累计和 ÷ n
    md = SMA(abs(ma-tp),timePeriod)
    #CCI（N日）=（TP－MA）÷MD÷0.015
    cci = (tp - ma)/md/0.015
    return cci
    
def ATR(high, low, close, timePeriod=50):   
    #TR = MAX(Ht,Ct-1)-MIN(Lt,Ct-1)
    maxHC = pd.DataFrame([high,close.shift(1)]).apply(max)
    minLC = pd.DataFrame([low,close.shift(1)]).apply(min)
    tr = maxHC - minLC
    atr = EMA(tr, timePeriod)
    return atr

def BOLL(close, timePeriod=20):
    ma = SMA(close, timePeriod)
    std = STD(close, timePeriod)
    up = ma + 2*std
    low = ma - 2*std
    return up, ma, low
