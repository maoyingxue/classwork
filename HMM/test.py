# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 21:37:02 2017

@author: maoyingxue
"""

#import myHMM
import tushare as ts
import datetime
import numpy as np
alpha = np.ones((2,10))
a=np.array([[2,1],[3,4]])
alpha[0,0]=sum(alpha[:,0]*a[:,0])
print(alpha)
#test_start_date = '2017-01-01'
#test_end_date = '2017-11-11'
#all_data = hist_prices = myHMM.parseStockPrices(test_start_date, test_end_date, '002415')
#
#print(all_data.shape)
#
#hist_prices = ts.get_k_data('002415', test_start_date, test_end_date, ktype="D", autype="none")
#print(hist_prices)
#print(len(hist_prices))
#np_hist_prices = np.empty(shape=[len(hist_prices),7])
#np_hist_prices[:, 2] = [datetime.datetime.strptime(dt, "%Y-%m-%d").toordinal() for dt in hist_prices.date.values]
#np_hist_prices[:, 1] = hist_prices["close"]
#hist_moves=np_hist_prices[:-1,1]-np_hist_prices[1:,1]
#print(hist_moves)
#print(hist_moves.shape)
#hist_Observation = np.array(list(map(lambda x: 1 if x>0 else (0 if x<0 else 2), hist_moves)))
#print(hist_Observation)
#hist_Observation = hist_Observation[::-1]
#print(hist_Observation)
#print(hist_Observation.shape,np.shape(hist_Observation))
#b = np.arange(6)
#print(np.argmax(b))
#phi = np.zeros((2,3))
#phi[0,0]=np.argmax(b)
#print(phi)
