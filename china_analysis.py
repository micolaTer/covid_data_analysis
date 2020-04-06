from covid_data_analysis import all_get_html
class ChinaAnalysis():
    def __init__(self):
        #从all_get_html大类里面提取covidData()生成一个实例对象
        self.covidData=all_get_html.CovidData()
        #调用该实例对象里面的get——html——dict方法返回所需数据的字典类型，实例对象内全局可用
        # self.covidDataDict=self.covidData.get_html_dict()
        self.covidDataDict=self.covidData.get_json_dict()

    def china_total_data(self):
        #在covidData里面得到chinaTotal数据
        chinaTotal = self.covidDataDict['chinaTotal']
        # print(chinaTotal)
        #返回chinaTotal
        return chinaTotal

    def china_everyday_data(self):
        '''获取中国每日数据积累'''
        chinaDayList=self.covidDataDict['chinaDayList']
        date_list=list()
        everyday_confirm = list()
        everyday_suspect = list()
        everyday_dead = list()
        everyday_heal = list()
        for everyday in chinaDayList:
            date_list.append(everyday['date'])
            everyday_confirm.append(int(everyday['confirm']))
            everyday_suspect.append(int(everyday['suspect']))
            everyday_dead.append(int(everyday['dead']))
            everyday_heal.append(int(everyday['heal']))
        print(date_list)
        # print(everyday_confirm) # 中国累积确诊数据少于上面chinaTotal累积数据
        return date_list, everyday_confirm, everyday_suspect, everyday_dead, everyday_heal

    def main(self):
        self.china_total_data()
        self.china_everyday_data()

if __name__=="__main__":
    china_analysis=ChinaAnalysis()
    china_analysis.main()


