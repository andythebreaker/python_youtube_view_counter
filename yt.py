#!/usr/bin/python
#--coding:UTF-8--
#無法顯示圖表中文
#三考資料http://charlieblovett.pixnet.net/blog/post/309808972-python-matplotlib-%E7%84%A1%E6%B3%95%E9%A1%AF%E7%A4%BA%E4%B8%AD%E6%96%87
#三考資料https://medium.com/marketingdatascience/%E8%A7%A3%E6%B1%BApython-3-matplotlib%E8%88%87seaborn%E8%A6%96%E8%A6%BA%E5%8C%96%E5%A5%97%E4%BB%B6%E4%B8%AD%E6%96%87%E9%A1%AF%E7%A4%BA%E5%95%8F%E9%A1%8C-f7b3773a889b
#路徑C:\Users\bear\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\matplotlib\mpl-data
#資料備份https://drive.google.com/file/d/1GxWLtaaGU2wSHyc6c20shxNPlkBnjTSj/view?usp=sharing
#資料備份https://drive.google.com/file/d/1bR7OEyG7Dv3rmkS4L0B7cXeKkWDCPHtv/view?usp=sharing
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.font_manager import FontProperties
import matplotlib.font_manager as font_manager
import requests
from bs4 import BeautifulSoup
import urllib

#url="https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/TraditionalChinese/SourceHanSansTC-Normal.otf"
#ttotf = requests.get(url)
#myfont = FontProperties(ttotf)

r = requests.get("https://www.youtube.com/channel/UCj_z-Zeqk8LfwVxx0MUdL-Q/videos") #將網頁資料GET下來
#r.encoding = 'utf-8'
#print(r.text)
soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
sel = soup.select('div[class="yt-lockup-meta"]') #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
sel2 = soup.select('a[dir="ltr"]')
strALL="ALL"
strALL2="ALL"
for i in range(len(sel)):
    strALL2 = strALL2+sel2[i].text+sel[i].text+"\n"#with title
for s in sel:
    strALL = strALL+s.text+"\n"#no title
strALL2=strALL2.replace(",","")

uai1="次數"
uai2="："
uai3="次"
cuai1=uai1.encode("utf-8","ignore")
cuai2=uai2.encode("utf-8","ignore")
cuai3=uai3.encode("utf-8","ignore")
tsl=strALL2.encode("utf-8","ignore")

wq=tsl.replace(cuai2,"@")
wq=wq.replace(cuai1,"")
wq=wq.replace(cuai3,"@")
print(wq)
ssp=wq.split("@")
ttltll=ssp[0]
del ssp[0]
plist=[0,99]
del plist[0]
del plist[0]
#for p in ssp:
#    if ssp.index(p)%2 == 1:
#        del ssp[ssp.index(p)]
rmd=[0,99]
del rmd[0]
del rmd[0]
for q in ssp:
    try:
        plist.append(int(q))
        print(q+"%%%%%\n")
    except ValueError:
        rmd.append(ssp.index(q))
        
for m in rmd:
    del ssp[m-rmd.index(m)]

aa=[0,99]
del aa[0]
del aa[0]
io=0
for i in plist:
    #print (i)
    aa.append(io)
    io+=1
    #print("\n")
    
print(strALL2)
strstl=""
cpsel2=sel2
del cpsel2[0]
for sel22 in cpsel2:
    strstl=strstl+"@SPLit@"+sel22.text
sel23=strstl.split("@SPLit@")
counterforsel123=0
for pp in sel23:
    print(pp)
    counterforsel123=counterforsel123+1
pppcounter=0
print("PPPPPPPPPPPPPPPPPPPPPPPPPPPP")
for ppq in plist:
    pppcounter=pppcounter+1
    print(ppq)
del sel23[0]
print("==========================")
print(counterforsel123-1)
print(pppcounter)

path='/usr/share/fonts/opentype/SourceHanSansTC-Normal.otf'
prop = font_manager.FontProperties(fname=path)
matplotlib.rc('font', family=prop.get_name())

plt.barh(sel23, plist,label =ttltll, align = "edge")
plt.xticks(rotation=45)

plt.legend() #要使用label要加這行
plt.title("YT film viewing number bar chart in the past month")
plt.xlabel("Title")
plt.ylabel("Number of views (times)")
plt.subplots_adjust(left=0.44, bottom=None, right=0.99, top=None, wspace=None, hspace=None)

plt.rcParams['savefig.dpi'] = 300 #圖片像素
plt.rcParams['figure.dpi'] = 300 #解析度

plt.savefig('op.png')

#print(strALL)
#normal_samples = np.random.normal(size = 100000) # 生成 100000 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數
#uniform_samples = np.random.uniform(size = 100000) # 生成 100000 組介於 0 與 1 之間均勻分配隨機變數
#plt.hist(normal_samples)
#plt.show()
#plt.hist(uniform_samples)
#plt.show()


