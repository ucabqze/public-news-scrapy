
"""
爬取每一个网页时需要定向修改xpath语句，
xpath_list 里的xpath语句排序有先后，排在前面的会被先执行，如果没有找到正文，则会使用下一个语句
xpath教程：https://www.runoob.com/xpath/xpath-tutorial.html

web_name需要与excel中‘来源’对应

save_path是爬取到正文后储存的json文件路径
"""

import os
from easydict import EasyDict as edict

cfg = edict()
cfg.GENERAL = edict()
cfg.GENERAL.excel_folder = '/home/QiqiZENG/PublicOpinionAnalysis/data/origin_data/'
# cfg.GENERAL.required_column = ['统一社会信用代码', '公司名称', '发布时间', '摘要描述', '来源', '标题', '网址', '本地html文件名']
cfg.GENERAL.BOT_NAME = 'chrome'

# 储存html网页
cfg.WEB_html = edict()
cfg.WEB_html.spider_name = "spider_html"
cfg.WEB_html.web_name = 'html'
cfg.WEB_html.save_path = os.path.join('saved_html', 'ALL_1') # 详细到网页储存的文件夹即可
cfg.WEB_html.xpath_list = []


# 企鹅号
cfg.WEB_3 = edict()
cfg.WEB_3.spider_name = "universal_spider"
cfg.WEB_3.web_name = '企鹅号'
cfg.WEB_3.save_path = '/home/QiqiZENG/scrapyProject1/saved_json/3_企鹅号.json'
cfg.WEB_3.xpath_list = ["/html/body//div[@id='content']//section[@class='article']//p//descendant::text()"]


# 网易号
cfg.WEB_4 = edict()
cfg.WEB_4.spider_name = "universal_spider"
cfg.WEB_4.web_name = '网易号'
cfg.WEB_4.save_path = '/home/QiqiZENG/scrapyProject1/saved_json/4_网易号.json'
cfg.WEB_4.xpath_list = ["/html/body//div[@class='post_body']//p//descendant::text()",
                        "/html/body//article//p//descendant::text()"]


# 一点资讯
cfg.WEB_5 = edict()
cfg.WEB_5.spider_name = "universal_spider"
cfg.WEB_5.web_name = '一点资讯'
cfg.WEB_5.save_path = '/home/QiqiZENG/scrapyProject1/saved_json/5_一点资讯.json'
cfg.WEB_5.xpath_list = ["/html/body//div[@class='content-bd']//p//descendant::text()",
                        "/html/body//div[@id='yidian-content']//p//descendant::text()",
                        "/html/body//div[@class='content-bd']//section//descendant::text()"]


# 懂车帝
cfg.WEB_6 = edict()
cfg.WEB_6.spider_name = "universal_spider"
cfg.WEB_6.web_name = '懂车帝'
cfg.WEB_6.save_path = '/home/QiqiZENG/scrapyProject1/saved_json/6_懂车帝.json'
cfg.WEB_6.xpath_list = ["/html/body//article[@id='article']//p//descendant::text()"]


# 百家号
cfg.WEB_7 = edict()
cfg.WEB_7.spider_name = "universal_spider"
cfg.WEB_7.web_name = '百家号'
cfg.WEB_7.save_path = '/home/QiqiZENG/scrapyProject1/saved_json/7_百家号111.json'
cfg.WEB_7.xpath_list = ["/html/body//div[@id='ssr-content']//p//descendant::text()",
                        "/html/body//div[@id='container']//article//p//descendant::text()"]


# 凤凰网
cfg.WEB_8 = edict()
cfg.WEB_8.spider_name = "universal_spider"
cfg.WEB_8.web_name = '凤凰网'
cfg.WEB_8.save_path = '/home/QiqiZENG/scrapyProject1/saved_json/8_凤凰网.json'
cfg.WEB_8.xpath_list = ['/html/body/div[1]/section/section[1]/div[1]/div[2]/div/div/div/p/descendant::text()',
                        "/html/body//div[@class='main']//div[@id='main_content']/p/descendant::text()",
                        "/html/body//div[@id='root']//h1/parent::div/following-sibling::div//p//text()",
                        "/html/body//div[@class='content-info']//p/descendant::text()"]


# 36氪
cfg.WEB_10 = edict()
cfg.WEB_10.spider_name = "universal_spider"
cfg.WEB_10.web_name = '36氪'
cfg.WEB_10.save_path = '/home/QiqiZENG/scrapyProject1/saved_json/10_36氪.json'
cfg.WEB_10.xpath_list = ["/html/body//div[@class='article-content']//p//descendant::text()",
                        "/html/body//div[@id='ssr-content']//p//descendant::text()",
                        "/html/body//div[@class='item-desc']//pre//descendant::text()"]


# scrapy run -w '中华网' -s '11_中华网.json'
# -x "/html/body//div[@id='chan_newsDetail']//p//descendant::text()"
# -x "/html/body//div[@id='arti-detail']//p//descendant::text()"
# 中华网
cfg.WEB_11 = edict()
cfg.WEB_11.spider_name = "universal_spider"
cfg.WEB_11.web_name = '中华网'
cfg.WEB_11.save_path = '/home/QiqiZENG/scrapyProject1/saved_json/11_中华网.json'
cfg.WEB_11.xpath_list = ["/html/body//div[@id='chan_newsDetail']//p//descendant::text()",
                         "/html/body//div[@id='arti-detail']//p//descendant::text()"]


# 东方财富网
cfg.WEB_12 = edict()
cfg.WEB_12.spider_name = "universal_spider"
cfg.WEB_12.web_name = '东方财富网'
cfg.WEB_12.save_path = '/home/QiqiZENG/scrapyProject1/saved_json/12_东方财富网.json'
cfg.WEB_12.xpath_list = ["/html/body//div[@id='ContentBody']//p//descendant::text()",
                         "/html/body//div[@class='article-body']//p//descendant::text()"]


# wind金融
cfg.WEB_15 = edict()
cfg.WEB_15.spider_name = "universal_spider"
cfg.WEB_15.web_name = 'wind金融'
cfg.WEB_15.save_path = '/home/QiqiZENG/scrapyProject1/saved_json/15_wind金融.json'
cfg.WEB_15.xpath_list = ["/html/body//div[@id='content-line']//p//descendant::text()",
                         "/html/body//div[@id='content-line']//descendant::text()"]


# 亿欧
cfg.WEB_18 = edict()
cfg.WEB_18.spider_name = "universal_spider"
cfg.WEB_18.web_name = '亿欧'
cfg.WEB_18.save_path = '/home/QiqiZENG/scrapyProject1/saved_json/18_亿欧.json'
cfg.WEB_18.xpath_list = ["/html/body//div[@class='post-body']//p//descendant::text()",
                         "/html/body//div[@class='post-content eo-flex m-b-48']//p//descendant::text()"]


# 新浪财经
cfg.WEB_20 = edict()
cfg.WEB_20.spider_name = "universal_spider"
cfg.WEB_20.web_name = '新浪财经'
cfg.WEB_20.save_path = '/home/QiqiZENG/scrapyProject1/saved_json/20_新浪财经.json'
cfg.WEB_20.xpath_list = ["/html/body//div[@class='blk_container']//p//descendant::text()",
                         "/html/body//div[@id='artibody']//p//descendant::text()"]


# 网经社
cfg.WEB_21 = edict()
cfg.WEB_21.spider_name = "universal_spider"
cfg.WEB_21.web_name = '网经社'
cfg.WEB_21.save_path = '/home/QiqiZENG/scrapyProject1/saved_json/21_网经社.json'
cfg.WEB_21.xpath_list = ["/html/body//div[@class='text']//p//descendant::text()"]


# 投资界
cfg.WEB_23 = edict()
cfg.WEB_23.spider_name = "universal_spider"
cfg.WEB_23.web_name = '投资界'
cfg.WEB_23.save_path = '/home/QiqiZENG/scrapyProject1/saved_json/23_投资界.json'
cfg.WEB_23.xpath_list = ["/html/body//div[@id='news-content']//p//descendant::text()"]


# 中国网
cfg.WEB_25 = edict()
cfg.WEB_25.spider_name = "universal_spider"
cfg.WEB_25.web_name = '中国网'
cfg.WEB_25.save_path = '/home/QiqiZENG/scrapyProject1/saved_json/25_中国网.json'
cfg.WEB_25.xpath_list = ["/html/body//div[@class='newsflash__Main-k0iwkz-5 huKJCq']/text()",
                         "/html/body//div[@class='PostDetail__Content-sc-19yo6og-6 jyjtnC']//p//descendant::text()",
                         "/html/body//div[@id='fontzoom']//p//descendant::text()",
                         "/html/body//div[@class='Content']//p//descendant::text()",
                         "/html/body//div[@class='d3_left_text']//p//descendant::text()",
                         "/html/body//p//descendant::text()"]


# 中金在线
cfg.WEB_29 = edict()
cfg.WEB_29.spider_name = "universal_spider"
cfg.WEB_29.web_name = '中金在线'
cfg.WEB_29.save_path = '/home/QiqiZENG/scrapyProject1/saved_json/29_中金在线.json'
cfg.WEB_29.xpath_list = ["/html/body//div[@class='Article']//text()"]


