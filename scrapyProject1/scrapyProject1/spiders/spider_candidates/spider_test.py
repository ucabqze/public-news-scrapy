import scrapy

#  scrapy crawl test_spider -o item.json
class TestFenghuangSpider(scrapy.Spider):
    name = 'test_spider'
    allowed_domains = ['https://www.toutiao.com/i6746417067567612424/']
    # 8- 凤凰网
    # start_urls = ['https://ishare.ifeng.com/c/s/7woHme3hgcl']
    # start_urls = ['http://biz.ifeng.com/a/20180727/45086685_0.shtml']
    # start_urls = ['https://biz.ifeng.com/c/7oKHlNRkz5s']
    # start_urls = ['https://house.ifeng.com/news/2015_12_30-50661390_0.shtml']

    # 1 - 今日头条
    # start_urls = ['https://www.toutiao.com/i6746417067567612424/']
    # 2 - 微信公众号
    # start_urls = ['https://mp.weixin.qq.com/s?__biz=MzA5ODU0OTIwMw==&mid=2653815031&idx=1&sn=0de3515be3714d7ac8fd82a0a34efb16']
    # start_urls = ['https://mp.weixin.qq.com/s?__biz=MzI3MzA0MTcxMw==&mid=2712122873&idx=1&sn=9186064c8ad5baf238c156a7255d5b7e']
    # start_urls = ['https://mp.weixin.qq.com/s?__biz=MjM5MDMyMjYyMQ==&mid=2649920103&idx=1&sn=ea6820406f587dc4c88aff03393fd4aa']
    # start_urls = ['https://mp.weixin.qq.com/s?__biz=MzA4MjI4MTcyOQ==&mid=2651311487&idx=1&sn=d2450a6050c4f9c20da51151588db3cc']
    start_urls = ["http://www.yidianzixun.com/article/0SwJFD9a"]

    def parse(self, response):

        output_dict = {}
        # 8- 凤凰网
        # body_content = response.xpath('/html/body/div[1]/section/section[1]/div[1]/div[2]/div/div/div/p/descendant::text()').extract()
        # body_content = response.xpath("/html/body//div[@class='main']//div[@id='main_content']/p/descendant::text()").extract()
        # body_content = response.xpath("/html/body//div[@id='root']//h1/parent::div/following-sibling::div//p//text()").extract()
        # body_content = response.xpath("/html/body//div[@class='content-info']//p/descendant::text()").extract()

        # 1 - 今日头条
        # body_content = response.xpath("/html/body/div/div/div[2]/div[1]/div[2]/article/div/p[1]").extract()

        # 2 - 微信
        # body_content = response.xpath("/html/body//section//descendant::text()").extract()

        # 3- 企鹅号
        # body_content = response.xpath("/html/body//div[@id='content']//section[@class='article']//p//descendant::text()").extract()

        # 4 - 网易号
        # body_content = response.xpath("/html/body//div[@class='post_body']//p//descendant::text()").extract()

        # 5_一点资讯
        body_content = response.xpath("/html/body//div[@class='content-bd']//p//descendant::text()").extract()
        output_dict['正文'] = body_content

        yield output_dict
