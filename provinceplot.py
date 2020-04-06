import pandas as pd
from pyecharts.charts import Map,Timeline
from pyecharts import options as opts
import json

data = [("广东", 10430.03,10000,3000,5000), ("山东", 9579.31,10000,3000,5000), ("河南", 9402.36,10000,3000,5000), ("四川", 8041.82,10000,3000,5000), ("江苏", 7865.99,10000,3000,5000), ("河北", 7185.42,10000,3000,5000),
        ("湖南", 6568.37,10000,3000,5000), ("安徽", 5950.1,10000,3000,5000), ("浙江", 5442,10000,3000,5000), ("湖北", 5723.77,10000,3000,5000), ("广西", 4602.66,10000,3000,5000), ("云南", 4596.6,10000,3000,5000),
        ("江西", 4456.74,10000,3000,5000), ("辽宁", 4374.63,10000,3000,5000), ("黑龙江", 3831.22,10000,3000,5000), ("陕西", 3732.74,10000,3000,5000), ("山西", 3571.21,10000,3000,5000), ("福建", 3552,10000,3000,5000),
        ("重庆", 2884,10000,3000,5000), ("贵州", 3476.65,10000,3000,5000), ("吉林", 2746.22,10000,3000,5000), ("甘肃", 2557.53,10000,3000,5000), ("内蒙古", 2470.63,10000,3000,5000), ("上海", 2301.391,10000,3000,5000),
        ("台湾", 2316.2,10000,3000,5000), ("新疆", 2181.33,10000,3000,5000), ("北京", 1961.2,10000,3000,5000), ("天津", 1293.82,10000,3000,5000), ("海南", 867.15,10000,3000,5000), ("香港", 709.76,10000,3000,5000),
        ("青海", 562.67,10000,3000,5000), ("宁夏", 630.14,10000,3000,5000), ("西藏", 3000.21,10000,3000,5000), ("澳门", 55.23,10000,3000,5000)]

def listfilter(i):
    data_pd = pd.DataFrame(data)
    # data_pd=data_pd.columns()
    cities = data_pd[0]
    numbers_i = data_pd[i]
    list_i = [[cities[a], numbers_i[a]] for a in range(len(cities))]
    return list_i

#data2 in case data not used
filepath = "province_total_confirm.json"
with open(filepath, encoding='utf-8') as f:
    data2 = f.readline()
    data2 = json.loads(data2)

def listfilter2(i):
    provinces=data2['name']
    numbers_i=data2['value'+str(i)]
    list_i = [[provinces[a], numbers_i[a]] for a in range(len(provinces))]
    return list_i


def hotmap(year):
    timeline_1 = Timeline()
    for i in range(0,4):
        if i==0:
            a='confirmed'
        elif i==1:
            a='suspected'
        elif i==2:
            a='dead'
        elif i==3:
            a='healed'
        list_i=listfilter2(i)
        map_1=(
            Map()
            .set_global_opts(
                title_opts=opts.TitleOpts(title="2020年全国各省疫情"),
                visualmap_opts=opts.VisualMapOpts()  # 最大数据范围
            )
            .add(a,list_i,maptype="china")
        )
        timeline_1.add(map_1,"{}".format(a))
    timeline_1.render("province_confirmed.html")

if __name__=="__main__":
    list_1 = listfilter(2)
    list_2=listfilter2(2)
    print(list_1)
    print(list_2)
    hotmap(2019)

