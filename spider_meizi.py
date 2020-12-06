# encoding: utf-8
# _author:Miachel Zhang
# date: 2020/6/27

"""爬取彼岸网美女类型图片"""
import requests
from lxml import etree
from fake_useragent import UserAgent
import time



def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }
    res=requests.get(url,headers=headers)
    res.encoding = "gbk"
    if res.status_code == 200:
        return res.text
    else:
        print("响应错误，请检查")

def get_img(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    }
    res=requests.get(url,headers=headers)
    res.encoding = "gbk"
    if res.status_code == 200:
        return res.content
    else:
        print("响应错误，请检查")

def parse_index(html):
    e = etree.HTML(html)
    imgs_urls = e.xpath("//div[@class='list']//li/a/img/@src")
    img_names = e.xpath("//div[@class='list']//li/a/img/@alt")

    return imgs_urls,img_names


def parse_pic(html):
    e = etree.HTML(html)
    names = e.xpath("//div[@class='post-content']//a/@alt")
    imgs = e.xpath("//div[@class='post-content']//a/@href")


# 保存图片方法
def sava_info(filename, response):
    with open(filename, "wb") as f:
        f.write(response)

def main():
    pages=int(input("请输入要下载的页数（>2）:"))
    start = time.clock()
    for i in range(2,pages):
        Picurl = "http://www.netbian.com/meinv/index_"+str(i)+".htm"
        html=get_html(Picurl)
        info=parse_index(html)
        print("开始下载第：" + str(i) + "页数据")
        imgs_urls=info[0]
        img_names=info[1]
        for name, img in zip(img_names, imgs_urls):
            #return name, img
            img_name=str(name).split(" ")[0]
            res = get_img(img)
            sava_info(filename="E://python_project//project//img//" + img_name+".jpeg",response=res)
        print("下载完成第："+str(i)+"页数据")
    end = time.clock()
    print('下载耗时: %s 秒' % (end - start))
if __name__ == '__main__':
    main()
