import os
import subprocess
# import commands

from config import cfg

def subprocess_run(web_crawl):
    command = ["scrapy", "run",
               "-w", web_crawl.web_name,
               "-s", web_crawl.save_path,
               "-p", web_crawl.spider_name,
               "-e", cfg.GENERAL.excel_folder,
               ]
    for xpath in web_crawl.xpath_list:
        command.append("-x")
        command.append(xpath)
    print(command)
    subprocess.run(command)

if __name__=="__main__":
    # 保存网页
    web_crawl = cfg.WEB_html
    subprocess_run(web_crawl)

    # 爬取某个网页的正文
    # web_crawl = cfg.WEB_5
    # subprocess_run(web_crawl)
