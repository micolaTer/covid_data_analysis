from covid_data_analysis import all_get_html
import json

class CityAnalysis():
    def __init__(self):
        self.covidData=all_get_html.CovidData()
        self.covidDataDict=self.covidData.get_json_dict()

    def city_total_data(self):
        '''获取湖北省各地级市累积数据'''
        # areaTree对应的第一个数据就是中国，下面的children对应的就是每个省份的数据，
        # 第一个省份就是湖北省，湖北省下面的children就是每个地级市的数据，也是一个列表，列表里面是字典
        areaTree=self.covidDataDict['areaTree'][0]['children'][0]['children']
        # print(areaTree)
        city_name=list()
        city_total_confirm=list()
        city_total_suspect=list()
        city_total_heal=list()
        city_total_dead=list()
        for city in areaTree:
            city_name.append(city['name'])
            city_total_confirm.append(city['total']['confirm'])
            city_total_suspect.append(city['total']['suspect'])
            city_total_dead.append(city['total']['dead'])
            city_total_heal.append(city['total']['heal'])
        city_total_dict={'name':city_name,
                         'value0':city_total_confirm,
                         'value1':city_total_suspect,
                         'value2':city_total_dead,
                         'value3':city_total_heal
                         }
        print(city_total_dict)
        with open('city_total_confirm.json','w',encoding='utf-8') as f:
            json.dump(city_total_dict,f,ensure_ascii=False)
        return city_name,city_total_confirm


    def city_daily_data(self):
        '''获取湖北省各地级市每日数据'''
        # areaTree对应的第一个数据就是中国，下面的children对应的就是每个省份的数据，
        # 第一个省份就是湖北省，湖北省下面的children就是每个地级市的数据，也是一个列表，列表里面是字典
        areaTree = self.covidDataDict['areaTree'][0]['children'][0]['children']
        # print(areaTree)
        city_name = list()
        city_today_confirm = list()
        city_today_suspect = list()
        city_today_heal = list()
        city_today_dead = list()
        for city in areaTree:
            city_name.append(city['name'])
            city_today_confirm.append(city['today']['confirm'])
            city_today_suspect.append(city['today']['suspect'])
            city_today_dead.append(city['today']['dead'])
            city_today_heal.append(city['today']['heal'])
        city_today_dict = {'name': city_name,
                           'value0': city_today_confirm,
                           'value1': city_today_suspect,
                           'value2': city_today_dead,
                           'value3': city_today_heal
                           }
        print(city_today_dict)
        with open('city_today_confirm.json', 'w', encoding='utf-8') as f:
            json.dump(city_today_dict, f, ensure_ascii=False)
        return city_name, city_today_confirm

    def main(self):
        self.city_total_data()
        self.city_daily_data()

if __name__=="__main__":
    city_analysis=CityAnalysis()
    city_analysis.main()

