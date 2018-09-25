import requests
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
* Function Name : get51jobDataZufang
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
*
************************************************************************
'''
def get51jobDataZufang(pageNumber, saveFileRootPath):
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
    savePage = 0
    # The loop control per page, then get per districts datas.
    for index in range(1, pageNumber + 1):
        url = "https://jobs.51job.com/xian/p" + str(index)
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
        if num == 3000:
            savePage = savePage + 1
            num = 0
        writeFile(saveFileRootPath + "/51job_original_" + str(savePage) + ".txt", result)
        print("savePage:", savePage, "num:", num)
        num = num + len(job)
        job.clear()
        company.clear()
        location.clear()
        money.clear()
        time.clear()
        order.clear()
        clearMoney.clear()
        result = ""
