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
