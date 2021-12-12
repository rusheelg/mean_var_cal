

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate(list1):
  
  print("Length of list is :",len(list1))

# setting condition for value error
  if len(list1) < 9:
    print("Value error, number of list elements should be 9")

#reshaping into 3X3 array
  n = np.array(list1)
  na = n.reshape(3,3)
  
  #calculating mean and converting to list
  mean0 = na.mean(axis=0).tolist()
  mean1 = na.mean(axis=1).tolist()
  meanf = na.mean().tolist()

  #variance
  var0 = na.var(axis=0).tolist()
  var1 = na.var(axis=1).tolist()
  varf = na.var().tolist()

  #std deviation
  std0 = na.std(axis=0).tolist()
  std1 = na.std(axis=1).tolist()
  stdf = na.std().tolist()

  #sum
  sum0 = na.sum(axis=0).tolist()
  sum1 = na.sum(axis=1).tolist()
  sumf = na.sum().tolist()

  #minimum
  min0 = na.min(axis=0).tolist()
  min1 = na.min(axis=1).tolist()
  minf = na.min().tolist() 

  #maximum
  max0 = na.max(axis=0).tolist()
  max1 = na.max(axis=1).tolist()
  maxf = na.max().tolist()

  result = {'mean':[mean0,mean1,meanf],
          'variance':[var0,var1,varf],
          'stddev':[std0,std1,stdf],
          'sum':[sum0,sum1,sumf],
          'minimum':[min0,min1,minf],
          'maximum':[max0,max1,maxf]}

  print(result)

list1 = [2,1,4,5,3,4,6,9,7]
calculate(list1)