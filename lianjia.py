import os
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

def countHouseNumber(districts):
    result = {}
    legalData = 0
    invalidData = 0
    path = "/home/fei/Documents/lianjia/lianjia_original_xinfang_" + districts + ".txt"
    if os.path.exists(path):
        with open(path, 'r') as lines:
            for line in lines:
                record = line.rstrip().split(",,,")
                if int(record[11]) != 0:
                    legalData += 1
                else:
                    invalidData += 1
        result[districts + "_legalData"] = legalData
        result[districts + "_invalidData"] = invalidData
        result[districts + "_totalData"] = legalData + invalidData
        if result[districts + "_totalData"] == 0:
            result[districts + "_legalRate"] = "None"
            result[districts + "_invalidRate"] = "None"
        else:
            result[districts + "_legalRate"] = str((legalData / result[districts + "_totalData"]) * 100) + '%'
            result[districts + "_invalidRate"] = str((invalidData / result[districts + "_totalData"]) * 100) + '%'
    else:
        result[districts + "_warning"] = "file not found"
    return result

def searchDistrictFromDistrict(averager, districts, statistics, flag):
    allAverager = []
    allDistricts = []
    for sta in range(0, len(statistics) - 1):
        if is_number(statistics[sta][districts[sta] + "_" + flag]):
            allAverager.append(statistics[sta][districts[sta] + "_" + flag])
            allDistricts.append(districts[sta])
    for index in range(0, len(allDistricts)):
        if averager == allAverager[index]:
            return str(averager) + "   " + allDistricts[index]

def countHouseNumberAboveOrBlow(districts, averagerAll):
    largerNumber = 0
    lessNumber = 0
    record = []
    result = {}
    temp = {}
    for dis in districts:
        path = "/home/fei/Documents/lianjia/lianjia_original_xinfang_" + dis + ".txt"
        if os.path.exists(path):
            with open(path, 'r') as lines:
                for line in lines:
                    record = line.rstrip().split(",,,")
                    if int(record[11]) != 0:
                        if int(record[11]) >= averagerAll:
                            largerNumber += 1
                        else:
                            lessNumber += 1
                record.clear()
            temp["largerNumber"] = largerNumber
            temp["lessNumber"] = lessNumber
            temp["totalNumber"] = lessNumber + largerNumber
            if temp["totalNumber"] != 0:
                temp["largerNumberRate"] = str(largerNumber / temp["totalNumber"] * 100) + '%'
                temp["lessNumberRate"] = str(lessNumber / temp["totalNumber"] * 100) + '%'
            else:
                temp["largerNumberRate"] = "temp[dis + \"_totalNumber\"] is 0"
                temp["lessNumberRate"] = "temp[dis + \"_totalNumber\"] is 0"
            result[dis] = temp
            largerNumber = 0
            lessNumber = 0
            temp = {}
        else:
            result[dis] = "file not found"
    return result

def countTag(districts):
    tag = []    
    nums = 1
    account = 1
    record = []
    result = {}
    valueList = []
    for dis in districts:
        path = "/home/fei/Documents/lianjia/lianjia_original_xinfang_" + dis + ".txt"
        if os.path.exists(path):
            with open(path, 'r') as lines:
                for line in lines:
                    record = line.rstrip().split(",,,")[18].split(',')
                    for re in record:
                        tag.append(re)
    for t in tag:
        if t[0] == '[':
            valueList.append(t[1:])
        elif t[len(t) - 1] == ']':
            valueList.append(t[:len(t) - 1 - 1])
    
    maxNum = len(valueList)
    # Data statistics
    while True:

        # When the list is not empty
        if maxNum != 0:

            # When a round of statistics does not reach the end of the list
            if nums != maxNum:
                if valueList[0] == valueList[nums]:
                    account += 1
                    valueList.pop(nums)
                    maxNum -= 1
                    result[valueList[0]] = account
                else:
                    nums += 1
                    
            # When a round of statistics reaches the end of the list
            else:

                # The last round of statistics may have only one list element left, 
                # so the element and its statistical results must be added to the dictionary before the element is popped.
                if maxNum == 1 and nums == 1:
                    result[valueList[0]] = account
                    valueList.pop(0)
                    break

                # When not the last round of statistics for a list element or the last round of statistics, as usual
                else:
                    valueList.pop(0)
                    maxNum -= 1
                    nums = 1
                    account = 1

        # When the list is empty
        else:
            break
    return result

def calculateZufangAverager(districts):
    top = 0
    bottom = 0
    result = {}
    for dis in districts:
        path = "/home/fei/Documents/lianjia/lianjia_original_zufang_" + dis + ".txt"
        if os.path.exists(path):
            with open(path, 'r') as lines:
                for line in lines:
                    record = line.rstrip().split(",,,")
                    if is_number(record[6]) and int(record[6]) != 0:
                        top += int(record[6])
                        bottom += 1
                    else:
                        continue
            if bottom != 0:
                result[dis] = int(top / bottom)
            top = 0
            bottom = 0
    return result

def calculate51jobAverager(types):
    top = 0
    bottom = 0
    result = {}
    # ~ print(record[:len(record) - 3].split('-')[0])
    # ~ print(record[len(record) - 3:])
    for ty in types:
        path = "/home/fei/Documents/lianjia/51job/51job_original_" + ty + ".txt"
        if os.path.exists(path):
            with open(path, 'r') as lines:
                for line in lines:
                    record = line.rstrip().split(",,,")
                    if record[4][len(record) - 3:] == "千/月":
                        top += int(record[4][:len(record) - 3].split('-')[0]) * 1000
                        bottom += 1
                    elif record[4][len(record) - 3:] == "万/月":
                        top += int(record[4][:len(record) - 3].split('-')[0]) * 10000
                        bottom += 1
                    else:
                        continue
            if bottom != 0:
                result[ty] = int(top / bottom)
            top = 0
            bottom = 0
    return result
