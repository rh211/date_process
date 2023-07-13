import pandas as pd
import numpy as np
import os
from tqdm import tqdm
from datetime import datetime


path_list = os.listdir('./IEEE30_AIMMS')

Time = []
Load = []
Loss = []
ReserveNeg = []
AGCRes = []

for name in tqdm(path_list):
    data_path = './IEEE30_AIMMS/' + name + '/input' + '/load_def.csv'
    df = pd.read_csv(data_path, encoding='gbk')

    Time.extend(df['时间'].values[1::12].tolist())
    Load.extend(df['系统负荷'].values[1::12].tolist())
    Loss.extend(df['网损'].values[1::12].tolist())
    # ReserveNeg.extend(df['下调节旋转备用'].values[1::12].tolist())
    # AGCRes.extend(df['AGC备用'].values[1::12].tolist())

Time = [i for i in Time if str(i) != 'nan']
Load = [i for i in Load if str(i) != 'nan']
Loss = [i for i in Loss if str(i) != 'nan']
# ReserveNeg = [i for i in ReserveNeg if str(i) != 'nan']
# AGCRes = [i for i in AGCRes if str(i) != 'nan']

for i in range(len(Time)):######## Unknown string format: 20200101_00:00:00zhuanhua
    date = Time[i].split('_')[0]
    hour = Time[i].split('_')[1]
    # date = Time[i][:4] + '-' + Time[i][4:6] + '-' + Time[i][6:8]

    # datetime_obj = datetime.strptime(date, '%Y%m%d')
    # formatted_date_str = datetime_obj.strftime('%Y/%#m/%#d')
    #
    # time_obj = datetime.strptime(hour, '%H:%M:%S')
    # formatted_time_str = time_obj.strftime('%#H:%M:%S')

    Time[i] = date + ' ' + hour
    time_obj = datetime.strptime(Time[i], '%Y%m%d %H:%M:%S')
    formatted_date_str = time_obj.strftime('%Y/%#m/%#d %#H:%M:%S')

    Time[i] = formatted_date_str

new_data = pd.DataFrame({'date':Time, 'Load':Load,'Loss':Loss})

header_name = ["date","Load","Loss"]

new_data.to_csv('./new_data.csv',index=False,header=header_name)
print(new_data['date'][:10])


'''
from datetime import datetime

date_str = '20200101'
datetime_obj = datetime.strptime(date_str, '%Y%m%d')
formatted_date_str = datetime_obj.strftime('%Y/%#m/%#d')

print(formatted_date_str)  # 输出: '2020/1/1'
'''