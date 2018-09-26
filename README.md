### If you want to get Lianjia's Xi'an housing price data, then you can use this module.
### If you want to analyze above data too, then you can use this module.
# eg
```
import lianjia as lj

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
```
```
import lianjia as lj

districts = ["weiyang", "baqiao", "changan4", "lianhu", "yanta",
        "beilin", "xinchengqu", "xixianxinquxian", "gaoling1", 
        "lintong", "yanliang", "lantian", "huxian", "zhouzhi"]
pageNumber = [53, 19, 18, 14, 95, 4, 11, 0, 1, 0, 0, 0, 0, 0]
saveFileRootPath = "/home/fei/Documents/lianjia"
lj.getLianjiaDataZufang(districts, pageNumber, saveFileRootPath)
```
```
import lianjia as lj

districts = ["jisuanjiyingjian", "jisuanjiruanjian", "hulianwang", "it-guanli", "jishuzhichi",
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
pageNumber = [28, 259, 257, 40, 103, 31, 117, 614, 1527, 163, 485, 258, 224, 86, 296, 58, 56,
    131, 13, 71, 188, 10, 42, 47, 129, 145, 15, 62, 78, 39, 239, 37, 30, 115, 385, 87, 338, 149,
    433, 70, 470, 102, 39, 221, 101, 9, 333, 82, 68, 317, 49, 22, 2, 27, 31, 189, 31, 17, 8, 70,
    30, 5, 14, 42, 52]
saveFileRootPath = "/home/fei/Documents/lianjia/51job"
lj.get51jobDataZufang(districts, pageNumber, saveFileRootPath)

```
