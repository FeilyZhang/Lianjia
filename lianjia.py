import requests
import datetime
from bs4 import BeautifulSoup

'''
************************Basic Informations******************************
*
* File Name            : lianjia.py
* Copyright            : 2018 Feily Zhang, All Rights Reserved.
* Create Date          : 2018-09-22
* Author               : Feily Zhang
* Author's Blog        : https://feily.tech/
* Author's Email       : feily_email@sina.cn
* Abstract Discription : Crawling website data and related statistical analysis.
*
************************Revision History********************************
*
* No   Version   Date        Revised by     Discription
* 0     V1.0     2018-09-22  Feily Zhang    Create this file.
*
************************************************************************
'''

'''
**********************Function Information******************************
*
* Function Name : writeFile
* Create Date   : 2018-09-22
* Discription   : Write data to file.
* Parameter     : filePath : File name.
                  content  : the data that need to write.
* Return Value  : None
*
************************Revision History********************************
*
* No   Version   Date        Revised by     Discription
* 0    V1.0.0    2018-09-22  Feily Zhang    Create this function.
*
************************************************************************
'''
def writeFile(filePath, content):
    with open(filePath, 'a') as file:
        file.write(content)


'''
**********************Function Information******************************
*
* Function Name : getLianjiaData
* Create Date   : 2018-09-22
* Discription   : Preliminary access to housing price data.
* Parameter     : keys : Key to extract in JSON data, that is list.
                  districts : All districts and counties of Xi'an, Shaanxi.
                  pageNumber : There are several pages of JSON data in each district.
                  saveFileRootPath : Save the root of the file.
* Return Value  : None
*
************************Revision History********************************
*
* No   Version   Date        Revised by     Discription
* 0    V1.0.0    2018-09-22  Feily Zhang    Create this function.
*
************************************************************************
'''
def getLianjiaData(keys, districts, pageNumber, saveFileRootPath):
    result = ""
    eleIndex = 0
    districtsIndex = 0
    response_map = {}
    response_list = []
    # The cycle traverses all districts and counties.
    for dis in range(0, len(districts)):
        # The loop control per page.
        for index in range(1, pageNumber[dis] + 1):
            url = "https://xa.fang.lianjia.com/loupan/" + districts[dis] + "/pg" + str(index) +  '/?_t=1'
            r = requests.get(url)
            response_map = r.json()
            response_list = response_map["data"]["list"]
            # This loop extracts every object in every page list.
            for ele in response_list:
                recordIndex = str((index - 1) * len(response_list) + eleIndex)
                # Traversing keys to get object values.
                for indexKeys in range(0, len(keys)):
                    # If you want to add ID, if it's the first element, add ID.
                    if indexKeys == 0:
                        result = recordIndex +  ",,," + ele[keys[indexKeys]] + ",,,"
                    # Because the value of the "tag" key may be a list。
                    # It may be wrong without any judgement.
                    elif indexKeys != len(keys) - 1:
                        result = result + ele[keys[indexKeys]] + ",,,"
                    else:
                        result = result + str(ele[keys[indexKeys]]) + "\n"
                writeFile(saveFileRootPath + '/lianjia_original_' + districts[districtsIndex] + ".txt", result)
                print(result)
                result = ""
                eleIndex = eleIndex + 1
            eleIndex = 0;
        districtsIndex = districtsIndex + 1;


'''
**********************Function Information******************************
*
* Function Name : getLianjiaDataZufang
* Create Date   : 2018-09-24
* Discription   : Preliminary access to housing price data(renting a house).
* Parameter     : districts : All districts and counties of Xi'an, Shaanxi.
                  pageNumber : There are several pages of data.
                  saveFileRootPath : Save the root of the file.
* Return Value  : None
*
************************Revision History********************************
*
* No   Version   Date        Revised by     Discription
* 0    V1.0.1    2018-09-24  Feily Zhang    Create this function.
*
************************************************************************
'''
def getLianjiaDataZufang(districts, pageNumber, saveFileRootPath):
    num = 0
    result = ""
    region = []
    zone = []
    meters = []
    other = []
    tag = []
    price = []
    updateTime = []
    seeNum = []
    iniTag = []
    finalTag = []
    # The cycle traverses all districts and counties.
    for dis in range(0, len(districts)):
        # The loop control per page, then get per districts datas.
        for index in range(1, pageNumber[dis] + 1):
            url = "https://xa.lianjia.com/zufang/" + districts[dis] + "/pg" + str(index)
            print(url)
            htmlContent = requests.get(url).text
            soup = BeautifulSoup(htmlContent)
            region = soup.find_all("span", class_="region")
            zone = soup.find_all("span", class_="zone")
            meters = soup.find_all("span", class_="meters")
            other = soup.find_all("div", class_="con")
            tag = soup.find_all("div", class_="view-label left")
            price = soup.find_all("span", class_="num")
            updateTime = soup.find_all("div", class_="price-pre")
            seeNum = soup.find_all("div", class_="square")
            for per in range(0, len(region)):
                iniTag = tag[per].find_all("span")
                for perTag in range(0, len(iniTag)):
                    finalTag.insert(perTag, iniTag[perTag].string)
                result = result + str(per + num) + ",,," + region[per].string + ",,," + zone[per].string + ",,,"
                result = result + meters[per].string + ",,," + other[per].find("a").string + ",,," + str(finalTag) + ",,,"
                result = result + price[per].string + ",,," + updateTime[per].string + ",,," + seeNum[per].find("span").string + "\n"
                iniTag.clear()
                finalTag.clear()
            writeFile(saveFileRootPath + '/lianjia_original_zufang_' + districts[dis] + ".txt", result)
            print(result)
            num = num + len(region)
            region.clear()
            zone.clear()
            meters.clear()
            other.clear()
            tag.clear()
            price.clear()
            updateTime.clear()
            seeNum.clear()
            result = ""
        num = 0



'''
**********************Function Information******************************
*
* Function Name : get51jobData
* Create Date   : 2018-09-25
* Discription   : Preliminary access to job data.
* Parameter     : pageNumber : There are several pages of data.
                  saveFileRootPath : Save the root of the file.
* Return Value  : None
*
************************Revision History********************************
*
* No   Version   Date        Revised by     Discription
* 0    V1.0.2    2018-09-25  Feily Zhang    Create this function.
* 1    V1.0.3    2018-09-26  Feily Zhang    Increase the distrcits(The corresponding parameter is 'districts').
*
************************************************************************
'''
def get51jobData(districts, pageNumber, saveFileRootPath):
    num = 0
    result = ""
    job = []
    company = []
    location = []
    money = []
    time = []
    order = []
    clearMoney = []
    clearMoneyIndex = 0
    # The cycle traverses all districts and counties.
    for dis in range(0, len(districts)):
        print(datetime.datetime.now())
        # The loop control per page, then get per districts datas.
        for index in range(1, pageNumber[dis] + 1):
            url = "https://jobs.51job.com/xian/" + districts[dis] + "/p" + str(index)
            print(url)
            htmlContent = requests.get(url).text
            soup = BeautifulSoup(htmlContent)
            job = soup.find_all("span", class_="title")
            company = soup.find_all("p", class_="info")
            location = soup.find_all("span", class_="location name")
            money = soup.find_all("span", class_="location")
            time = soup.find_all("span", class_="time")
            for indexMoney in range(0, len(money)):
                if indexMoney % 2 != 0:
                    clearMoney.insert(clearMoneyIndex, money[indexMoney].string)
                clearMoneyIndex = clearMoneyIndex + 1
            for per in range(0, len(job)):
                result = result + str(per + num) + ",,," + str(job[per].find("a").get("title")) + ",,,"
                result = result + str(company[per].find("a", class_="name").get("title")) + ",,,"
                result = result + str(location[per].string) + ",,," + str(clearMoney[per]) + ",,,"
                result = result + str(time[per].string) + "\n"
            num = num + len(job)
            job.clear()
            company.clear()
            location.clear()
            money.clear()
            time.clear()
            order.clear()
            clearMoney.clear()
        num = 0
        writeFile(saveFileRootPath + "/51job_original_" + districts[dis] + ".txt", result)
        result = ""
        print(datetime.datetime.now())


'''
**********************Function Information******************************
*
* Function Name : cleanAndAnalyze
* Create Date   : 2018-10-02
* Discription   : clean and analyze the data.
* Parameter     : readFileName : file's path
                  keyNumber : cleaning number
                  keyNumber2 : analyzing number
* Return Value  : None
*
************************Revision History********************************
*
* No   Version   Date        Revised by     Discription
* 0    V1.0.4    2018-10-02  Feily Zhang    Create this function.
* 1    V1.0.5    2018-10-05  Feily Zhang    add some function.
*
************************************************************************
'''
def cleanAndAnalyze(districts, keyNumber, keyNumber2):
    total_averager = 0
    number_averager = 0
    record = []
    result = {}
    averager = 0
    priceSort = []
    topAdd = 0
    path = "/home/fei/Documents/lianjia/lianjia_original_xinfang_" + districts + ".txt"
    if os.path.exists(path):
        # Calculate the average value of the data in the file.
        with open(path, 'r') as lines:
            for line in lines:
                # Separates each row from the data and gets the list.
                record = line.rstrip().split(",,,")
                # If the length of the list is not equal to the actual length.
                # the invalid data can be eliminated.
                # Otherwise, count the total and the number so as to calculate the mean.
                if (len(record) != keyNumber):
                    continue
                else:
                    value = float(record[keyNumber2])
                    # If the value is equal to 0, It means that the value is not credible,
                    # that is, it is useless for statistics.
                    if (value != 0):
                        total_averager = total_averager + value
                        number_averager = number_averager + 1
                        priceSort.append(value)
                    else:
                        continue
                record.clear()
        if number_averager != 0:
            averager = int(total_averager / number_averager)
            result[districts + "_AVERAGER"] = averager
        else:
            result[districts + "_AVERAGER"] = "All data is invalid."
    else:
        result[districts + "_AVERAGER"] = "file not found."
    priceSort.sort()
    if len(priceSort) != 0:
        result[districts + "_MAX"] = priceSort[len(priceSort) - 1]
        result[districts + "_MIN"] = priceSort[0]
        result[districts + "_RANGE"] = priceSort[len(priceSort) - 1] - priceSort[0]
    else:
        result[districts + "_MAX"] = "All data is invalid."
        result[districts + "_MIN"] = "All data is invalid."
        result[districts + "_RANGE"] = "All data is invalid."
    
    if os.path.exists(path):
        # Calculate the standard deviation of the data in the file.
        with open(path, 'r') as lines:
            for line in lines:
                # Separates each row from the data and gets the list.
                record = line.rstrip().split(",,,")
                # If the length of the list is not equal to the actual length.
                # the invalid data can be eliminated.
                if (len(record) != keyNumber):
                    continue
                else:
                    value = float(record[keyNumber2])
                    # If the value is equal to 0, It means that the value is not credible,
                    # that is, it is useless for statistics.
                    if (value != 0):
                        topAdd += pow(value - averager, 2)
                    else:
                        continue
                record.clear()
            if number_averager != 0:
                result[districts + "_STANDAR"] = int(pow(topAdd / number_averager, 0.5))
            else:
                result[districts + "_STANDAR"] = "All data is invalid."
    else:
        result[districts + "_STANDAR"] = "file not found."
    return result

def calculate(array):
    lists = []
    result = {}
    averagerAll = 0
    topAdd = 0
    for arr in array:
        if is_number(arr):
            averagerAll += arr
            lists.append(arr)
        else:
            continue
    result["averager"] = int(averagerAll / len(lists))
    result["averagerMax"] = int(sorted(lists)[len(lists) - 1])
    result["averagerMin"] = int(sorted(lists)[0])
    result["averagerRange"] = int(result["averagerMax"] - result["averagerMin"])
    for li in lists:
        topAdd += pow(li - result["averager"], 2)
    result["averagerStandar"] = int(pow(topAdd / len(lists), 0.5))
    return result

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
