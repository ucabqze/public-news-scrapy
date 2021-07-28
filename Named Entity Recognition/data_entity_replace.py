import copy
import itertools
import random
import math
import string
import os
import sys
sys.path.append("…")

"""
本文件中的wt_list基本上都是这种形式：
[
[('山', 'B-ORG'), ('东', 'I-ORG'), ('顺', 'I-ORG'), ('骋', 'I-ORG'), ('集', 'I-ORG'), ('团', 'I-ORG')],  
[('利', 'B-ORG'), ('和', 'I-ORG'), ('兴', 'I-ORG')]
]
"""
#################################################################################################################
### read and write ##############################################################################################
#################################################################################################################
def read_file(input_filename):
    """该函数读取一个文件，并返回generator object"""
    niter = 0
    i = 0
    with open(input_filename, encoding='utf-8') as f:
        words_tags = []
        for line in f:
            i += 1
            line = line.strip()
            if (len(line) == 0 or line.startswith("-DOCSTART-")):
                if len(words_tags) != 0:
                    niter += 1
                    yield words_tags
                    words_tags = []
            else:
                ls = line.split(' ')
                try:
                    word, tag = ls[0], ls[1]
                    if not tag.strip():
                        print("line", i, "is null")
                except:
                    print(ls)
                    print("line", i)
                words_tags += [(word, tag)]

def write_txt2(labeling_list,save_dir):
    """
    :param labeling_list: [[('山', 'B-ORG'), ('东', 'I-ORG'), ('顺', 'I-ORG'), ('骋', 'I-ORG'), ('集', 'I-ORG'), ('团', 'I-ORG')],  [('利', 'B-ORG'), ('和', 'I-ORG'), ('兴', 'I-ORG')]]
    :param save_dir: 储存地址
    :return: 储存好的文件
    """
    save_path = save_dir
    ttfp = open(save_path, 'w')
    for sent in labeling_list:
        for word_tag in sent:
            word, tag = word_tag
            ttfp.write(word + " " + tag + "\n")
        ttfp.write('\n')
    ttfp.close()

def random_writer(input_filename):
    """将文件中的句子顺序打乱"""
    input_list = list(read_file(input_filename))
    random.shuffle(input_list)
    write_txt2(input_list, input_filename)


#################################################################################################################
### get #################################################################
#################################################################################################################
def get_entity_list(candi_list, entity_name):
    """
    生成可以替换的实体列表
    :param candi_list: 数据，需要替换的原列表。 e.g., [[('Port','O'),('of','O'),('Discharge','O'), ('Shanghai','B-port'), ('Port','I-port']]
    :param entity_name: 需要替换的实体tag e.g., 'port'
    :return: 实体组成的list e.g., ['Shanghai Port', 'Qingdao Port', ‘ANY PORT IN CHINA’]
    """
    words_tags_list = candi_list
    entity_list = []
    for words_tags in words_tags_list:
        for key, group in itertools.groupby(words_tags, key=lambda m: m[1][2:]):  # 本来是想按 DRAWN ON 分开再进行，但是这么和规则没什么区别了，还是先相信模型，总数凑不上100再按规则进行吧
            # print(key, ' '.join([w for w,t in list(group)])
            if key == entity_name:
                entity_list.append(list(group))
    return entity_list

def date_generator():
    """生成任意一种形式、任意一天的日期"""
    date_ = random.choice(range(1,32))
    date = '0' + str(date_) if date_<10 and random.choice([0,1,1,1]) else str(date_)
    date = date + 'TH' if date_ in list(range(4,20))+list(range(24,32)) and random.choice([0,1,1,1]) else date
    month = random.choice(range(1,13))
    month = '0' + str(month) if month<10 and random.choice([0,1,1,1]) else str(month)
    year = random.choice([2018,2019,2020])
    year = str(year)
    month2 = ['JANUARY', 'FEBRUARY','MARCH',"APRIL",'MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER', "DECEMBER"]
    month2 = random.choice(month2)
    month3 = ['JAN.','FEB.','MAR.','APR.','MAY.','JUNE.','JULY.','AUG.','SEP.','OCT.','NOV.','DEC.']
    month3 = random.choice(month3)

    which_option = random.choice([0,1,2,3,3,4,4])
    if which_option == 0:
        output = year+'-'+month+'-'+date
    elif which_option == 1:
        output = year+'.'+month+'.'+date
    elif which_option == 2:
        output = date + '.' + month + random.choice([',', ', ']) + year
    elif which_option == 3:
        output = date + random.choice([' ',',',', ']) + random.choice([month2,month3]) +  random.choice([' ',',',', '])  + year
    elif which_option == 4:
        output = random.choice([month2,month3])  + random.choice([' ',',',', ','.']) + date +  random.choice([' ',',',', '])  + year

    return output

#################################################################################################################
### generate training data by data perturbation #################################################################
#################################################################################################################
def replace_entity(entity_name, wt_list, candi_list):
    """
    将句子中的tag为entity_name的实体换成另一个同tag的实体。
    :param entity_name: 需要替换的tag。e.g., "port"
    :param wt_list: 数据，需要替换的原列表。 e.g., [[('Port','O'),('of','O'),('Discharge','O'), ('Shanghai','B-port'), ('Port','I-port']]
    :param candi_list: 通过get_entity_list得到可替换的实体列表，与entity_name对应, e.g., ['Shanghai Port', 'Qingdao Port', ‘ANY PORT IN CHINA’]
    :return: 被替换后的wt_list， e.g.,  [[('Port','O'),('of','O'),('Discharge','O'), ('Qingdao','B-port'), ('Port','I-port']]
    """
    new_wt_list = []
    for words_tags in wt_list:
        new_wt = []
        changed = False
        for key, group in itertools.groupby(words_tags, key=lambda m: m[1][2:]):  # 本来是想按 DRAWN ON 分开再进行，但是这么和规则没什么区别了，还是先相信模型，总数凑不上100再按规则进行吧
            # print(key, ' '.join([w for w,t in list(group)])
            if key==entity_name:
                new_wt = new_wt + random.choice(candi_list) ### random
                changed = True
            else:
                new_wt = new_wt + list(group)
        if changed:
            new_wt_list.append(new_wt)
    return new_wt_list

def repalce_char(wt_list, entity_name, th_sent = 0.8, th_char = 0.2):
    """替换一个wt_list中"""
    change_list = random.sample(wt_list, math.ceil(len(wt_list)*th_sent))
    new_wt_list = []
    for temp in change_list:
        replaced = False
        new_wt = []
        for w, t in temp:
            if t[2:] == entity_name:
                idx_list = random.sample(range(len(w)), math.ceil(len(w)*th_char))
                new_w = ''.join([random.choice(string.ascii_uppercase+string.digits) if i in idx_list else w[i] for i in range(len(w))])
                replaced = True
            else:
                new_w = w
            new_wt.append((new_w, t))
        if replaced:
            new_wt_list.append(new_wt)
    return new_wt_list

def generate_data(input_filename_list, new_file_name, entity_list, char_entity_list, candi_filename_list = None):
    # read
    wt_list = []
    for input_filename in input_filename_list:
        wt_list = wt_list + list(read_file(input_filename))

    if not candi_filename_list:
        candi_filename_list = input_filename_list
    candi_wt_list = []
    for candi_filename in input_filename_list:
        candi_wt_list = candi_wt_list + list(read_file(candi_filename))


    # replace
    # (1) replace entity
    # change only one entity each time
    # if entity_list:
    #     new_wt_list = []
    #     for entity_name in entity_list:
    #         candi_list = get_entity_list(candi_wt_list, entity_name)
    #         new_wt_list = new_wt_list + replace_entity(entity_name, wt_list, candi_list)

    # # change multi-entity at same time
    if entity_list:
        new_wt_list = []
        for i in range(10):
            temp_list = copy.deepcopy(wt_list)
            for entity_name in entity_list:
                candi_list = get_entity_list(candi_wt_list, entity_name)
                temp_list = replace_entity(entity_name, temp_list, candi_list)
                # temp_list = replace_date(temp_list)
            new_wt_list = new_wt_list + temp_list

    # (2) replace char
    if char_entity_list:
        for char_entity in char_entity_list:
            new_wt_list = new_wt_list + repalce_char(new_wt_list, char_entity, th_sent = 0.8, th_char = 0.2)


    #write
    write_txt2(new_wt_list, new_file_name)


if __name__ == "__main__":
    # # 1. convert data splited by date to splited by words cell
    # input_filename_list = ["data/0916_nertag.txt"]
    # bydate2byfield(input_filename_list)
    father_path = os.path.abspath(os.path.dirname(os.getcwd()))
    # 2. replace entity
    generate_data(input_filename_list = [os.path.join(father_path, "data/train.txt")], # 输入文件
                  new_file_name = os.path.join(father_path,'data/gener_1.txt'), # 输出文件
                  entity_list = ['ORG', 'LOC'], # 需要在那些tag下的实体中替换整个实体
                  char_entity_list = [], # 需要在那些tag下的实体中替换字母
                  candi_filename_list=None # 提供可以选的被替换实体，应该是和input_filename_list格式一样的list，输入文件路径
                  )
    # 3. random the order
    random_writer(os.path.join(father_path,'data/gener_1.txt'))
