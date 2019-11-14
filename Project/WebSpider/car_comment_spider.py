import scrapy
import pandas as pd

class CarCommentSpider(scrapy.Spider):
    name = 'CarComment'  # 蜘蛛的名字
    # 指定要抓取的网页, 从第1页到第124页，程序会自动解析每个url
    start_urls = ['https://koubei.16888.com/117870/0-0-0-1/']


    # 网页解析函数
    def parse(self, response):
        for car in response.xpath('/html/body/div/div/div/div[@class="mouth_box"]/dl'):  # 遍历xpath
            advantage = car.xpath('dd/div[2]/p[1]/span[@class="show_dp f_r"]/text()').extract_first()
            disadvantage = car.xpath('dd/div[2]/p[2]/span[2]/text()').extract_first()
            # /html/body/div[9]/div[1]/div[2]/div[3]/dl[1]/dd/div[2]/p[2]/span[2]/text()
            sums = car.xpath('dd/div[2]/p[3]/span[2]/text()').extract_first()
            support_num = car.xpath('dd/div/div[@class="like f_r"]/a/text()').extract_first()
            #
            # print('优点：', advantage)
            # print('缺点：', disadvantage)
            # print('综述：', sums)
            # print('支持人数:', support_num)
            # columns = ['Advantage', 'disadvantage', 'sums', 'support_num']
            # data = [advantage, disadvantage, sums, support_num]
            # df_line = pd.DataFrame(columns=columns, data = data)
            # return_csv = pd.append(df_line)

            if advantage is not None and disadvantage is not None and sums is not None and support_num is not None:
                yield {'advantage': advantage, 'disadvantage': disadvantage, 'sums': sums, 'support_num': support_num}
        # return_csv.to_csv('data.csv')
'''
        n = len(response.xpath('/html/body/div/div/div/div/div[@class="page"]/a'))
        for i in range(1, n + 1):  # 遍历每个a元素，获取下一页的url
            text = response.xpath(
                '/html/body/div/div/div/div/div[@class="page"]/a[' + str(i) + ']/text()').extract_first()
            if text == '下一页':
                next_page = response.xpath(
                    '/html/body/div/div/div/div/div[@class="page"]/a[' + str(i) + ']/@href').extract_first()
                next_page = response.urljoin(next_page)  # 将相对地址转换为绝对地址

                yield scrapy.Request(next_page, callback=self.parse)  # next_page继续进行spider解析
'''
# //*[@id="reviews"]/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div[1]/div[1]/span/span[1]
# //*[@id="reviews"]/div/div/div[2]/div/div[1]/div[1]/div/div[1]/div[1]/div[2]/span[1]