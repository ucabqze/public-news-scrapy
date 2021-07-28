import scrapy
import os
import re
from scrapyProject1.utils.io_readAndWrite import read_excel

class Universal(scrapy.Spider):
    name = 'universal_spider'

    def __init__(self, *args, **kwargs):
        # print(self.xpath_sent)
        self.web_df = None

    def get_webpath_df(self):
        # 获取所有excel列表
        input_path_list = [os.path.join(self.excel_folder, file) for file in os.listdir(self.excel_folder) if
                           file.endswith('xlsx') and not file.startswith('.')]
        # 读取所有Excel，转换为dataframe
        data_df = read_excel(input_path_list, self.required_column)

        # 选取相关的网站
        web_df = data_df[data_df['来源'].isin(self.web_name)]
        return web_df

    def parse_detail(self, response, **kwargs):
        input_info = response.meta['input_info']
        try:
            print("*****",response.url)
            # print("*****",response.body)

            output_dict = {}
            for pth in self.xpath_sent:
                print("###########",pth)
                # print("!!!!!",response.xpath(pth))
                body_content = response.xpath(pth).extract()
                if body_content:
                    body_content = [re.sub('\s+', ' ',S6) for S6 in body_content]
                    break

            output_dict['统一社会信用代码'] = input_info['统一社会信用代码']
            output_dict['公司名称'] = input_info['公司名称']
            output_dict['发布时间'] = input_info['发布时间']
            output_dict['摘要描述'] = input_info['摘要描述']
            output_dict['来源'] = input_info['来源']
            output_dict['标题'] = input_info['标题']
            output_dict['网址'] = input_info['网址']
            output_dict['正文'] = body_content
            yield output_dict
        except:
            print('Failed: ', response.url)
            output_dict = {}
            output_dict['统一社会信用代码'] = input_info['统一社会信用代码']
            output_dict['公司名称'] = input_info['公司名称']
            output_dict['发布时间'] = input_info['发布时间']
            output_dict['摘要描述'] = input_info['摘要描述']
            output_dict['来源'] = input_info['来源']
            output_dict['标题'] = input_info['标题']
            output_dict['网址'] = input_info['网址']
            output_dict['正文'] = 'Failed'
            yield output_dict

    def parse(self, response):
        if self.web_df is None:
            self.web_df = self.get_webpath_df()

        for i in range(self.web_df.shape[0]):
                input_info = self.web_df.iloc[i]
                if type(input_info['网址']) == str:
                    yield scrapy.Request(url=input_info['网址'], callback=self.parse_detail, meta={'input_info':input_info})


