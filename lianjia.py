import requests

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
* Function Name : getLianjiaDat
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
