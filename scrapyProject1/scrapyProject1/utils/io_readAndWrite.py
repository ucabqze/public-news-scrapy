import math
import os
import collections
import random
import eventlet
import time
import pandas as pd
from urllib import request
from tqdm import tqdm, trange


def read_excel(input_path_list, required_column):
    """此函数将多个excel表格中的内容读出来合并成一个dataframe返回出来， 注意多个Excel格式需要一致。"""
    if len(input_path_list) == 0:
        return None
    elif len(input_path_list) == 1:
        return pd.read_excel(input_path_list[0])
    else:
        data_df = pd.read_excel(input_path_list[0]).loc[:,required_column]
        for input_path in input_path_list[1:]:
            data_df = pd.concat([data_df,pd.read_excel(input_path).loc[:,required_column]], axis=0, ignore_index=True)
        return data_df

def check_url(url):
    """这个函数检查输入的url是否是一个有效的链接"""
    try:
        eventlet.monkey_patch()  # 必须加这条代码
        with eventlet.Timeout(30,False):
            with request.urlopen(url) as file:
                return True
        print("Time out")
        return False
    except Exception as e:
        return False

def web_statistic(data_df):
    # 1. 统计网页占比
    count_all = collections.Counter(data_df.loc[:, '来源'])
    count_all = count_all.most_common(len(count_all))
    f = open("data/count_all.txt", "w")
    for x,y in count_all:
        f.write("Count Number: {}   Website: {}\n".format(y, x))
    f.close()

    # # 2. 统计有效网页占比
    # valid_web_list = []
    # start = time.time()
    # for i in range(data_df.shape[0]):
    #     if check_url(data_df.loc[i,'网址']):
    #         valid_web_list.append(data_df.loc[i, '来源'])
    #
    # count_valid = collections.Counter(data_df.loc[:, '来源'])
    # count_valid.most_common(len(count_valid))
    # end = time.time()
    # write_txt(count_valid, "data/count_valid.txt")
    # # 3. 统计公司与网页的对应关系
    # # for i in range(data_df.loc[:, 'in']):
    return count_all

def validation_test(data_df):
    """本函数只针对有50个网页以上的网站做有效性检测，
    每个网站抽查50个网页，算出有效网站的比例"""
    count_all = web_statistic(data_df)
    count_valid = []
    for web, count in tqdm(count_all):
        if count<50:
            break
        else:
            web_df = data_df[data_df['来源'] == web]
            valid_sample_count = [check_url(x) for x in random.sample(list(web_df.loc[:, '网址']), min(100, web_df.shape[0]))].count(True)
            rate = valid_sample_count/100
            count_valid.append((web, count, rate))

            # write to excel
            f = open('data/count_valid.txt', "a")
            f.write(
                "Count Number: {}  estimated valid rate: {}  estimiate valid Count: {}  Website: {}\n".format(count,
                                                                                                              rate,
                                                                                                              math.floor(count*rate),
                                                                                                              web))
            f.close()

    # # write to excel
    # f = open('data/count_valid.txt', "w")
    # for x,y,z in count_valid:
    #     f.write("Count Number: {}  estimated valid rate: {}  estimiate valid Count: {}  Website: {}\n".format(y, z, math.floor(y*z), x))
    # f.close()

if __name__=='__main__':

    input_path = 'data/头部私募基金投资链_舆情信息_深圳.xlsx'
    input_folder = 'data'
    required_column = ['统一社会信用代码', '公司名称', '发布时间', '摘要描述', '来源', '标题', '网址', ]

    input_path_list = [os.path.join(input_folder,file) for file in os.listdir(input_folder) if file.endswith('xlsx') and not file.startswith('.')]
    data_df = read_excel(input_path_list, required_column)
    # print('data_df readed')
    # validation_test(data_df)

    # web_list = []
    # for i in range(data_df.shape[0]):
    #     if data_df.loc[i, '来源'] == '同花顺财经':
    #         web_list.append(data_df.loc[i, '网址'])
    web_list = [data_df.loc[i, '网址'] for i in range(data_df.shape[0]) if data_df.loc[i, '来源']=='今日头条']
    for web in web_list:
        print(web)




