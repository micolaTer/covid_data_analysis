from covid_data_analysis import  all_get_html
import json

class ProvinceAnalysis():
    def __init__(self):
        self.covidData=all_get_html.CovidData()
        self.covidDataDict=self.covidData.get_json_dict()

    def province_total_data(self):
        areaTree=self.covidDataDict['areaTree'][0]['children']
        province_name=list()
        province_total_confirm=list()
        province_total_suspect = list()
        province_total_dead = list()
        province_total_heal = list()
        for province in areaTree:
            province_name.append(province['name'])
            province_total_confirm.append(province['total']['confirm'])
            province_total_suspect.append(province['total']['suspect'])
            province_total_dead.append(province['total']['dead'])
            province_total_heal.append(province['total']['heal'])
        province_total_confirm_dict = {'name': province_name, 'value': province_total_confirm}
        province_total_suspect_dict={'name':province_name,'value':province_total_suspect}
        province_total_dead_dict={'name':province_name,'value':province_total_dead}
        province_total_heal_dict={'name':province_name,'value':province_total_heal}
        province_total_dict = {'name': province_name, 'value0':province_total_confirm,'value1':province_total_suspect,'value2':province_total_dead,'value3':province_total_heal}
        # print(province_total_dict)
        with open('province_total_confirm.json','w',encoding='utf-8') as f:
            json.dump(province_total_dict,f,ensure_ascii=False)
        # return province_name,province_total_confirm

    def province_everyday_data(self):
        areaTree=self.covidDataDict['areaTree'][0]['children']
        province_name = list()
        province_today_confirm = list()
        province_today_suspect = list()
        province_today_dead = list()
        province_today_heal = list()
        for province in areaTree:
            province_name.append(province['name'])
            province_today_confirm.append(province['today']['confirm'])
            # province_today_suspect.append(province['today']['suspect'])
            province_today_dead.append(province['today']['dead'])
            province_today_heal.append(province['today']['heal'])
        # print(province_today_confirm)
        return province_name, province_today_confirm

    def main(self):
        self.province_total_data()
        self.province_everyday_data()

if __name__=="__main__":
    province_analysis=ProvinceAnalysis()
    a,b=province_analysis.province_everyday_data()
    print(a,b)