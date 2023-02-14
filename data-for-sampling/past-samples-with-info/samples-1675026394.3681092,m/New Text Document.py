import numpy as np
import pandas as pd
import statistics

df= pd.read_csv('book2.csv')
# wav_arr=[]
# for i in df['Wavelength']: # column of values of wavelength dim
#     if i > 800: # signifies all data points with near-IR wavelength criteria
#         wav_arr.append(i)
#     wav_mean = np.mean(wav_arr)
# #x = statistics.mean(df['Z-LII1'])
# #print(x)

print(np.mean(df['Z-LII3']))
