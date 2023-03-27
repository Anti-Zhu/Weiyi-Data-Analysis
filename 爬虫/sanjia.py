import asyncio

from pyppeteer import launch
from pyquery import PyQuery as pq
import pandas as pd  # 用于保存csv文件

class HospitalSpider(object):

    def __init__(self):
        self._data = list()

    async def main(self,num):

        global browser
        try:

            browser = await launch(headless=True)
            page = await browser.newPage()

            print(f"正在爬取第 {num} 页面")
            await page.goto("https://y.dxy.cn/hospital/?&grade=2&page={}".format(num))
            content = await page.content()

            self.parse_html(content)
            print("正在存储数据....")

            data = pd.DataFrame(self._data)
            data.to_csv("三甲医院名单.csv", encoding='utf_8_sig')
        except Exception as e:
            print(e.args)
        finally:
            num+=1

            await browser.close()

            await self.main(num)
    def parse_html(self,content):

        doc = pq(content)

        items = doc(".hospital-title").items()
        for item in items:
            name = item.text() # 医院名称

            one_data = {
                "hospital_name": name
            }

            self._data.append(one_data)



    def run(self):
        loop = asyncio.get_event_loop()

        asyncio.get_event_loop().run_until_complete(self.main(1))



if __name__ == '__main__':

    Hospital = HospitalSpider()
    Hospital.run()