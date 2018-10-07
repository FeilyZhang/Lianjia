import lianjia as lj
'''
keys = ["city_id", "city_name", "district", "district_id", 
        "district_name","resblock_name", "sale_status", 
        "total_price_start", "total_price_start_unit", "address",
        "average_price", "avg_price_start", "avg_price_start_unit" ,
        "bizcircle_name", "resblock_frame_area","house_type", "open_date", "tags"]
districts = ["weiyang", "baqiao", "changan4", "lianhu", "yanta",
        "beilin", "xinchengqu", "xixianxinquxian", "gaoling1", 
        "lintong", "yanliang", "lantian", "huxian", "zhouzhi"]
pageNumber = [27, 10, 9, 10, 35, 7, 5, 1, 2, 1, 1, 0, 1, 0]
saveFileRootPath = "/home/fei/Documents/lianjia"
lj.getLianjiaData(keys, districts, pageNumber, saveFileRootPath)
pageNumber = [53, 19, 18, 14, 95, 4, 11, 0, 1, 0, 0, 0, 0, 0]
'''
'''
types = ["xiaoshouxingzheng",
    "kefuzhichi", "caiwushenji", "jinrongzhengquan", "yinhang", "baoxian", "shengchanyingyun",
    "zhilianganquan", "gongchengjixie", "qichezhizao", "qichexiaoshou", "jigongpugong",
    "fuzhuangfangzhi", "caigou", "maoyi", "wuliucangchu", "shengwuzhiyao", "huagong", "yiliao",
    "guanggao", "gongguanmeijie", "shichangyingxiao", "yingshimeiti", "bianjichuban", "yishusheji",
    "yishusheji", "fangdichankaifa", "fangdichanxiaoshou", "wuyeguanli", "renliziyuan", "gaojiguanli",
    "xingzhenghouqin", "zixunguwen", "lvshifawu", "jiaoshi", "peixun", "keyan", "canyinfuwu", "jiudianlvyou",
    "meirongbaojian", "baihuolingshou", "jiaotongyunshu", "jiazhengbaojie", "gongwuyuan", "fanyi", "zaixiaoxuesheng",
    "peixunshixi", "jianzhi", "huanbao", "nonglinmuyu", "wangdiantaobao", "jixiejichuang", "yinshuabaozhuang",
    "yundongjianshen", "xiuxianyule", "others"]
pageNumber = [162, 483, 258, 223, 85, 295, 57, 55,
    131, 13, 71, 186, 10, 42, 46, 126, 144, 14, 63, 78, 38, 238, 37, 30, 115, 381, 86, 338, 148,
    430, 71, 466, 101, 38, 221, 100, 8, 333, 82, 66, 316, 49, 22, 2, 27, 31, 187, 31, 17, 7, 70,
    30, 4, 14, 41, 52]
saveFileRootPath = "/home/fei/Documents/lianjia/51job"
lj.get51jobDataZufang(districts, pageNumber, saveFileRootPath)
'''
less = []
larger = []
statistics = []
averagerKey = []
averagerValue = []
standardDeviation = []
zufangStatistics = {}
job51Statictics = {}
job51Statictics1 = {}
topZufang = 0
topJob51 = 0
topJob511 = 0
bottomZufang = 0
bottomJob51 = 0
bottomJob511 = 0
totalStatistics = {}
districts = ["weiyang", "baqiao", "changan4", "lianhu", "yanta",
        "beilin", "xinchengqu", "xixianxinquxian", "gaoling1", 
        "lintong", "yanliang", "lantian", "huxian", "zhouzhi"]
types = ["jisuanjiyingjian", "jisuanjiruanjian", "hulianwang", "it-guanli", "jishuzhichi",
    "tongxinjishukaifa", "dianzi", "xiaoshouguanli", "xiaoshourenyuan", "xiaoshouxingzheng",
    "kefuzhichi", "caiwushenji", "jinrongzhengquan", "yinhang", "baoxian", "shengchanyingyun",
    "zhilianganquan", "gongchengjixie", "qichezhizao", "qichexiaoshou", "jigongpugong",
    "fuzhuangfangzhi", "caigou", "maoyi", "wuliucangchu", "shengwuzhiyao", "huagong", "yiliao",
    "guanggao", "gongguanmeijie", "shichangyingxiao", "yingshimeiti", "bianjichuban", "yishusheji",
    "yishusheji", "fangdichankaifa", "fangdichanxiaoshou", "wuyeguanli", "renliziyuan", "gaojiguanli",
    "xingzhenghouqin", "zixunguwen", "lvshifawu", "jiaoshi", "peixun", "keyan", "canyinfuwu", "jiudianlvyou",
    "meirongbaojian", "baihuolingshou", "jiaotongyunshu", "jiazhengbaojie", "gongwuyuan", "fanyi", "zaixiaoxuesheng",
    "peixunshixi", "jianzhi", "huanbao", "nonglinmuyu", "wangdiantaobao", "jixiejichuang", "yinshuabaozhuang",
    "yundongjianshen", "xiuxianyule", "others"]
print("\n" + "--------------------The following indicators are printed for each district and county--------------------")
for dis in districts:
    print(lj.cleanAndAnalyze(dis, 19, 11))
    statistics.append(lj.cleanAndAnalyze(dis, 19, 11))
print("\n")

averagerKey = districts
for li in range(0, len(statistics) - 1):
    averagerValue.append(statistics[li][districts[li] + "_averager"])
for li in range(0, len(statistics) - 1):
    standardDeviation.append(statistics[li][districts[li] + "_standar"])

print("--------------------The following is to print the statistics of the county's overall average and its indicators--------------------")
totalStatistics = lj.calculateAll(averagerValue)
print(totalStatistics)
print("\n")

print("--------------------The following legal and invalid data are printed in all districts and counties--------------------")
for dis in districts:
    print(lj.countHouseNumber(dis))
print("\n")

print("--------------------The following print averages are compared and sorted--------------------")
print("The overall mean value is ", totalStatistics["averager"])
print("The average housing price in the following districts is larger than the average value.")
for averager in averagerValue:
    if lj.is_number(averager):
        if averager > totalStatistics["averager"]:
            larger.append(averager)
larger.sort()
for lar in larger:
    print(lj.searchDistrictFromDistrict(lar, districts, statistics, "averager"))
print("The average housing price in the following districts is less than the mean value.")
for averager in averagerValue:
    if lj.is_number(averager):
        if averager < totalStatistics["averager"]:
            less.append(averager)
less.sort()
for les in less:
    print(lj.searchDistrictFromDistrict(les, districts, statistics, "averager"))

larger.clear()
less.clear()
print("\n")

print("--------------------The following print standard deviation are compared and sorted--------------------")
print("The overall mean value is ", totalStatistics["averagerStandar"])
print("The standard deviation housing price in the following districts is larger than the standard deviation.")
for averager in standardDeviation:
    if lj.is_number(averager):
        if averager > totalStatistics["averagerStandar"]:
            larger.append(averager)
larger.sort()
for lar in larger:
    print(lj.searchDistrictFromDistrict(lar, districts, statistics, "standar"))
print("The standard deviation housing price in the following districts is less than the standard deviation.")
for averager in standardDeviation:
    if lj.is_number(averager):
        if averager < totalStatistics["averagerStandar"]:
            less.append(averager)
less.sort()
for les in less:
    print(lj.searchDistrictFromDistrict(les, districts, statistics, "standar"))
print("\n")

print("--------------------Excluding invalid data, the number of houses in the districts above and below the average is calculated and their proportion is calculated.--------------------")
print(lj.countHouseNumberAboveOrBlow(districts, totalStatistics["averager"]))

print(lj.countTag(districts))

print("--------------------The following is to print the rental data and overall average of counties and counties--------------------")
zufangStatistics = lj.calculateZufangAverager(districts)
print(zufangStatistics)
print()
for value in zufangStatistics.values():
    topZufang += int(value)
    bottomZufang += 1
print("xian's rent house averager price: " + str(int(topZufang / bottomZufang)) + "\n")

print("--------------------Print industry wage data and overall mean--------------------")
job51Statictics = lj.calculate51jobAverager(types)
print(job51Statictics)
print()
job51Statictics1 = lj.calculate51jobAverager1(types)
print(job51Statictics1)
print()
for value in job51Statictics.values():
    topJob51 += int(value)
    bottomJob51 += 1
for value1 in job51Statictics1.values():
    topJob511 += int(value1)
    bottomJob511 += 1
print("xian's industry wage data and overall mean: " + str(int(topJob51 / bottomJob51)) + "——" + str(int(topJob511 / bottomJob511)) + "\n")

print("--------------------The following prints the top ten and countdown ten prices in all districts and counties of Xi'an--------------------")
for dis in districts:
    print(dis, "   ", lj.topAndBottom(dis), "\n")
