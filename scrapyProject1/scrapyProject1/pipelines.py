# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from scrapy.exporters import JsonItemExporter


class Scrapyproject1Pipeline:
    # def process_item(self, item, spider):
    #     return item

    def __init__(self, settings):
        self.settings = settings
        # write json
        if "html" not in self.settings['web_name']:
            self.file = open(self.settings['save_path'], 'wb')
            # self.file.write('['.encode('utf-8'))
            self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
            self.exporter.start_exporting()

    @classmethod
    def from_settings(cls, settings):
        return cls(settings)

    def open_spider(self, spider):
        # 开启爬虫
        spider.start_urls = ['https://www.baidu.com'] # 在spider就可以直接self.start_url
        spider.excel_folder = self.settings['excel_folder'] # 在spider就可以直接self.excel_folder
        spider.web_name = self.settings['web_name'] # 在spider就可以直接self.web_name
        spider.xpath_sent = self.settings['xpath_sent']
        spider.required_column = self.settings['required_column']
        spider.save_path = self.settings['save_path']

    def close_spider(self, spider):
        # 关闭爬虫
        if "html" not in self.settings['web_name']:
            # 关闭json write
            self.exporter.finish_exporting()
            # self.file.write(']'.encode('utf-8'))
            self.file.close()

    def process_item(self, item, spider):
        # 将帖子内容保存到文件
        # with open(self.settings['save_path'], 'a', encoding='utf-8') as f:
        #     json.dump(dict(item), f, ensure_ascii=False, indent=2)

        # line = json.dumps(dict(item), ensure_ascii=False) +"," + "\n"
        # self.file.write(line.encode('utf-8'))

        # write json
        self.exporter.export_item(item)

        return item


    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

