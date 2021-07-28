import scrapy.commands.crawl as crawl
from scrapy.exceptions import UsageError
from scrapy.commands import ScrapyCommand

# scrapy run -w '企鹅号' -s '3_企鹅号.json' -x "/html/body//div[@id='content']//section[@class='article']//p//descendant::text()"
# scrapy run -w '网易号' -s '4_网易号.json' -x "/html/body//div[@class='post_body']//p//descendant::text()" -x "/html/body//article//p//descendant::text()"
# scrapy run -w '一点资讯' -s '5_一点资讯.json' -x "/html/body//div[@class='content-bd']//p//descendant::text()" -x "/html/body//div[@id='yidian-content']//p//descendant::text()" -x "/html/body//div[@class='content-bd']//section//descendant::text()"
# scrapy run -w '懂车帝' -s '6_懂车帝.json' -x "/html/body//article[@id='article']//p//descendant::text()"
# scrapy run -w '百家号' -s '7_百家号.json' -x "/html/body//div[@id='ssr-content']//p//descendant::text()" -x "/html/body//div[@id='container']//article//p//descendant::text()"
# scrapy run -w '凤凰网' -s '8_凤凰网.json' -x '/html/body/div[1]/section/section[1]/div[1]/div[2]/div/div/div/p/descendant::text()' -x "/html/body//div[@class='main']//div[@id='main_content']/p/descendant::text()" -x "/html/body//div[@id='root']//h1/parent::div/following-sibling::div//p//text()" -x "/html/body//div[@class='content-info']//p/descendant::text()"
# scrapy run -w '36氪' -s '10_36氪.json' -x "/html/body//div[@class='article-content']//p//descendant::text()"  -x "/html/body//div[@id='ssr-content']//p//descendant::text()" -x "/html/body//div[@class='item-desc']//pre//descendant::text()"
# scrapy run -w '中华网' -s '11_中华网.json' -x "/html/body//div[@id='chan_newsDetail']//p//descendant::text()"  -x "/html/body//div[@id='arti-detail']//p//descendant::text()"
# scrapy run -w '东方财富网' -s '12_东方财富网.json' -x "/html/body//div[@id='ContentBody']//p//descendant::text()"  -x "/html/body//div[@class='article-body']//p//descendant::text()"
# scrapy run -w 'wind金融' -s '15_wind金融.json' -x "/html/body//div[@id='content-line']//p//descendant::text()" -x "/html/body//div[@id='content-line']//descendant::text()"
# scrapy run -w '亿欧' -s '18_亿欧.json' -x "/html/body//div[@class='post-body']//p//descendant::text()" -x "/html/body//div[@class='post-content eo-flex m-b-48']//p//descendant::text()"
# scrapy run -w '新浪财经' -s '20_新浪财经.json' -x "/html/body//div[@class='blk_container']//p//descendant::text()" -x "/html/body//div[@id='artibody']//p//descendant::text()"
# scrapy run -w '网经社' -s '21_网经社.json' -x "/html/body//div[@class='text']//p//descendant::text()"
# scrapy run -w '投资界' -s '23_投资界.json' -x "/html/body//div[@id='news-content']//p//descendant::text()"
# scrapy run -w '中国网' -s '25_中国网.json' -x "/html/body//div[@class='newsflash__Main-k0iwkz-5 huKJCq']/text()" -x "/html/body//div[@class='PostDetail__Content-sc-19yo6og-6 jyjtnC']//p//descendant::text()" -x "/html/body//div[@id='fontzoom']//p//descendant::text()" -x "/html/body//div[@class='Content']//p//descendant::text()"  -x "/html/body//div[@class='d3_left_text']//p//descendant::text()"  -x "/html/body//p//descendant::text()"
# scrapy run -w '中金在线' -s '29_中金在线.json' -x "/html/body//div[@class='Article']//text()"


# scrapy run -w '财联社' -s '30_财联社.json' -x "/html/body//div[@class='m-b-40']/div[2]/text()"
# scrapy run -w '萝卜投研' -s '28_萝卜投研.json' -x "/html/body//div[@id='mp-editor']//p//descendant::text()"
# scrapy run -w '搜狐' -s '27_搜狐.json' -x "/html/body//div[@id='mp-editor']//p//descendant::text()"
# scrapy run -w '资本邦' -s '26_资本邦.json' -x "/html/body//div[@class='c-article__detail']//p//descendant::text()"
# scrapy run -w '全天候科技' -s '22_全天候科技.json' -x "/html/body//div[@id='content']//p//descendant::text()"
# scrapy run -w '企查查' -s '19_企查查.json' -x "/html/body//div[@class='content']//p//descendant::text()"
# scrapy run -w '腾讯自选股' -s '15_腾讯自选股.json' -x "/html/body//div[@id='news-text']//p//descendant::text()"
# scrapy run -w '搜狐财经' -s '14_搜狐财经.json' -x "/html/body//article//p//descendant::text()"
# scrapy run -w '同花顺财经' -s '9_同花顺财经.json' -x "/html/body//div[@class='main-text atc-content']//p//descendant::text()" -x "/html/body//div[@id='content']//p//descendant::text()" -x "/html/body//div[@class='news-body-content']//p//descendant::text()" -x "/html/body//div[@class='content']//p//descendant::text()"  -x "/html/body//section[@class='article']//p//descendant::text()" -x "/html/body//div[@class='main-text atc-content']/p/text()"
# scrapy run -w '同花顺财经' -s '9_同花顺财经.json' -x "//p//descendant::text()"
class Command(crawl.Command):

    def add_options(self, parser):
        # 为命令添加选项
        ScrapyCommand.add_options(self, parser)
        parser.add_option("-w", "--web_name", type='str', action="append", dest="web_name", default=[],
                          help="which web to crawl")
        parser.add_option("-x", "--xpath_sent", type="str", action="append", dest="xpath_sent", default=[],
                          help="set the xpath sentence to crawl the web")
        parser.add_option("-e", "--excel_folder", type="str", action="store", dest="excel_folder", default='/home//QiqiZENG/PublicOpinionAnalysis/data/origin_data/',
                          help="set the original data folder path")
        parser.add_option("-s", "--save_path", type="str", action="store", dest="save_path", default='default.txt',
                          help="set the save path")
        parser.add_option("-r", "--required_column", type="str", action="append", dest="required_column", default=['统一社会信用代码', '公司名称', '发布时间', '摘要描述', '来源', '标题', '网址', '本地html文件名',],
                          help="choose the columns from excel files")
        parser.add_option("-p", "--spider_name", type="str", action="store", dest="spider_name", default="universal_spider")


    def process_options(self, args, opts):
        # 处理从命令行中传入的选项参数
        ScrapyCommand.process_options(self, args, opts)
        self.settings.set('web_name', opts.web_name, priority='cmdline')
        self.settings.set('xpath_sent', opts.xpath_sent, priority='cmdline')
        self.settings.set('excel_folder', opts.excel_folder, priority='cmdline')
        self.settings.set('save_path', opts.save_path, priority='cmdline')
        self.settings.set('required_column', opts.required_column, priority='cmdline')

    def run(self, args, opts):
        # 启动爬虫
        self.crawler_process.crawl(opts.spider_name)
        self.crawler_process.start()
