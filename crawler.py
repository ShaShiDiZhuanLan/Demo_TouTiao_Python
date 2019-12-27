# coding: utf-8
"""
Author: 沙振宇
Update Time: 2019-12-25
Info: 爬虫——有bug尚未修复（未加as和cp参数）
"""
import xlrd
import urllib.request
from lxml import etree
import os

arr_all=[]
# 爬取
def run(myUrl, xp):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    headers = {'User-Agent': user_agent,'tt_webid': '6773835217905321479'}
    req = urllib.request.Request(myUrl, headers=headers)

    # 访问页面
    myResponse = urllib.request.urlopen(req)
    myPage = myResponse.read()
    print("myPage:",myPage)
    myPage = myPage.decode("UTF-8")
    print("myPage:",myPage)

    if myPage != "":
        html = etree.HTML(myPage)
        print("xp",xp)
        result = html.xpath(xp)
        print("result",result)
        tmpList = ""
        for item in result:  # 文章名称
            if item.strip() != "":
                tmpList = tmpList + item.strip()
        return tmpList
    else:
        return ""


# 读excel
def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook('data/2019-toutiao.xlsx')
    # 根据sheet索引或者名称获取sheet内容
    sheet = workbook.sheet_by_index(0) # sheet索引从0开始
    # sheet的名称，行数，列数
    print (sheet.name,sheet.nrows,sheet.ncols)


    for row in range(sheet.nrows):
        dir_tmp={}
        if sheet.cell_value(row,0) != '标题':
            dir_tmp['title'] = sheet.cell_value(row,0)
            dir_tmp['web'] = sheet.cell_value(row,1)
            dir_tmp['num'] = str(row)
            arr_all.append(dir_tmp)

# 写文件
def write_txt(name,content):
    with open(name, "w", encoding="utf-8") as fp:
        fp.write(content)

def main():
    # read_excel()
    # print(arr_all)
    # # for dir in arr_all:
    # #     web = dir["web"]
    # web = "https://www.toutiao.com/a6626929361519903240/"
    # print(web)
    # result = run(web, '//div[@class="articleInfo"]/content/text()')
    # if result == "":
    #     result = run(web, '//div[@class="article-content"]/p/text()')
    #     # write_txt("data/result/"+dir["num"]+".txt", result)

    for i in range(96):
        if i > 20:
            write_txt("data/"+str(i)+".txt", "")

if __name__ == '__main__':
    main()
    write_txt("data/result/all.txt", "all")

