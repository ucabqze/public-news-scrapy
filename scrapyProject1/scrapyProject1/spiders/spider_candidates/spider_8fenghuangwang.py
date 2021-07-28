import scrapy
import os
from .io_readAndWrite import read_excel

# https://ishare.ifeng.com/c/s/v0023t2n6tj6-_Q2vODC9ognpt4BfID0Odkar--oxnPD--0Pew__
# scrapy crawl fenghuang -o item.json -a excel_folder = '/home/QiqiZENG/PublicOpinionAnalysis/data'

class Fenghuangwang(scrapy.Spider):
    name = 'fenghuang'
    def __init__(self, excel_folder=None,
                 web_name=['凤凰网'],
                 required_column = ['统一社会信用代码', '公司名称', '发布时间', '摘要描述', '来源', '标题', '网址', ],
                 *args,
                 **kwargs):
        super(Fenghuangwang, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.baidu.com']
        self.excel_folder = excel_folder
        self.web_name = web_name
        self.required_column = required_column
        self.web_df = self.get_webpath_df()

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
            print(response.url)
            output_dict = {}
            body_content = response.xpath('/html/body/div[1]/section/section[1]/div[1]/div[2]/div/div/div/p/descendant::text()').extract() # p/descendant::text() 获得p下面所有子孙节点的文字
            if not body_content:
                body_content = response.xpath("/html/body//div[@class='main']//div[@id='main_content']/p/descendant::text()").extract()
            if not body_content:
                body_content = response.xpath("/html/body//div[@id='root']//h1/parent::div/following-sibling::div//p//text()").extract()
            if not body_content:
                body_content = response.xpath("/html/body//div[@class='content-info']//p/descendant::text()").extract()

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
        for i in range(self.web_df.shape[0]):
            input_info = self.web_df.iloc[i]
            yield scrapy.Request(url=input_info['网址'], callback=self.parse_detail, meta={'input_info':input_info} )


