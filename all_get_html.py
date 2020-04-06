import requests
import json
import time

class CovidData():
    def __init__(self):
        #原始疫情数据网址
        self.start_url='https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_cn_day_counts&callback=&_=%d'%int(time.time()*1000)

    def get_html_dict(self):
        #爬取页面
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0'}
        response= requests.get(url=self.start_url,headers=headers)
        response.encoding='utf-8'
        #将json的string字符转换成字典
        resDict=json.loads(response.text)
        #由于需要用到resDict里面的['data'],依然是json的string，需要重复转换字典
        dataDict=json.loads(resDict['data'])
        # print(dataDict) #检查一下数据
        return dataDict

    def get_json_dict(self):
        filePath='C:/Users/tianyu.zhang/PycharmProjects/Test/covid_data_analysis/getOnsInfo.json'
        with open(filePath,encoding='utf-8') as f:
            response=f.readline()
            resDict=json.loads(response)
            dataDict=json.loads(resDict['data'])
            # print(dataDict)
        return dataDict

if __name__=="__main__":
    covidData=CovidData()
    cvoidDataDict=covidData.get_json_dict()
