import pandas as pd
from pyecharts.charts import Map,Timeline
from pyecharts import options as opts
import json
from covid_data_analysis import province_analysis

class ProvinceDailyMap():
    def __init__(self):
        self.province_analysis=province_analysis.ProvinceAnalysis()
        self.province_name,self.province_today_confirm=self.province_analysis.province_everyday_data()

    def listfliter(self):
        provinces=self.province_name
        numbers=self.province_today_confirm
        list_i=[[provinces[a],numbers[a]] for a in range(len(provinces))]
        return list_i

    def hotmapdaily(self):
        list_i=self.listfliter()
        map_1=(
            Map()
            .set_global_opts(
                title_opts=opts.TitleOpts(title="全国各省今日确诊疫情"),
                visualmap_opts=opts.VisualMapOpts()  # 最大数据范围
            )
            .add('今日',list_i,maptype="china")
        )
        map_1.render("province_daily.html")

if __name__=="__main__":
    plot=ProvinceDailyMap()
    list_1=plot.listfliter()
    print(list_1)
    plot.hotmapdaily()

