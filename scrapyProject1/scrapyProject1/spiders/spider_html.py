import scrapy
import os
import re
from scrapyProject1.utils.io_readAndWrite import read_excel

class Html(scrapy.Spider):
    name = 'spider_html'

    def __init__(self, *args, **kwargs):
        # print(self.xpath_sent)
        self.web_df = None

    def get_webpath_df(self):
        # 获取所有excel列表
        input_path_list = [os.path.join(self.excel_folder, file) for file in os.listdir(self.excel_folder) if
                           file.endswith('xlsx') and not file.startswith('.')]
        # 读取所有Excel，转换为dataframe
        data_df = read_excel(input_path_list, self.required_column)
        return data_df

    def parse_detail(self, response, **kwargs):
        input_info = response.meta['input_info']
        print("###",self.web_name)
        save_folder = self.save_path
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        try:
            filename = os.path.join(save_folder, input_info['本地html文件名'] + '.html')
            with open(filename, 'wb') as fp:
                fp.write(response.body)
            print("Success:")
        except:
            print('Failed: Please check if you have add the column "本地html文件名" to the origin Excel')

    def parse(self, response):
        if self.web_df is None:
            self.web_df = self.get_webpath_df()

        for i in range(self.web_df.shape[0]):
                input_info = self.web_df.iloc[i]
                if type(input_info['网址']) == str:
                    yield scrapy.Request(url=input_info['网址'], callback=self.parse_detail, meta={'input_info':input_info})


