#!/usr/bin/env python
# coding: utf-8

# # 代理IP

# In[10]:


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from bs4 import BeautifulSoup

import numpy as np
import random
import win32com.client as win32
import xlrd
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from proxyscrape import create_collector
from proxyscrape import get_proxyscrape_resource
from proxyscrape import create_collector
import proxyscrape


# In[2]:


# #來源一
# df = pd.read_excel('proxy1.xlsx',sheet_name='Sheet1')
# ActIps_1 = []

# for i in range(len(df)):
#     ip   = str(df['IP地址'][i]).replace(' ','')
#     port = str(df['端口'][i]).replace(' ','')
    
#     proxy_dict = {}
#     key   = 'https'
#     proxy_dict[key] ='https://'+ip+":"+  port

#     try:
#       # 隨機找的一篇新聞即可
#         url = 'https://seekingalpha.com/earnings/earnings-call-transcripts'
#         resp = requests.get(url, proxies=proxy_dict, timeout=2)

#         if str(resp.status_code) == '200':
#             ActIps_1.append(proxy_dict[key])
#             print('Succed: {}'.format(proxy_dict[key]))
#             resp_check = requests.get(url="https://blog.sodsec.com/ip.php",proxies=proxy_dict, timeout=2)
#             print(resp_check.text)
#         else:
#             print('Failed: {}'.format(proxy_dict[key]))

#     except:
#             print('Failed: {}'.format(proxy_dict[key]))


# In[3]:


# #來源一
# df = pd.read_excel('proxy1.xlsx',sheet_name='Sheet2')

# for i in range(len(df)):
#     proxy   = str(df['Proxy'][i]).replace(' ','')

    
#     proxy_dict = {}
#     key   = 'https'
#     proxy_dict[key] ='https://'+proxy

#     try:
#       # 隨機找的一篇新聞即可
#         url = 'https://seekingalpha.com/earnings/earnings-call-transcripts'
#         resp = requests.get(url, proxies=proxy_dict, timeout=2)

#         if str(resp.status_code) == '200':
#             ActIps_1.append(proxy_dict[key])
#             print('Succed: {}'.format(proxy_dict[key]))
#             resp_check = requests.get(url="https://blog.sodsec.com/ip.php",proxies=proxy_dict, timeout=2)
#             print(resp_check.text)
#         else:
#             print('Failed: {}'.format(proxy_dict[key]))

#     except:
#             print('Failed: {}'.format(proxy_dict[key]))
            


# In[4]:


# #來源一
# df = pd.read_excel('proxy1.xlsx',sheet_name='Sheet3')

# for i in range(len(df)):
#     proxy   = str(df['Proxy'][i]).replace(' ','')

    
#     proxy_dict = {}
#     key   = 'https'
#     proxy_dict[key] ='socks4://'+proxy

#     try:
#       # 隨機找的一篇新聞即可
#         url = 'https://seekingalpha.com/earnings/earnings-call-transcripts'
#         resp = requests.get(url, proxies=proxy_dict, timeout=2)

#         if str(resp.status_code) == '200':
#             ActIps_1.append(proxy_dict[key])
#             print('Succed: {}'.format(proxy_dict[key]))
#             resp_check = requests.get(url="https://blog.sodsec.com/ip.php",proxies=proxy_dict, timeout=2)
#             print(resp_check.text)
#         else:
#             print('Failed: {}'.format(proxy_dict[key]))

#     except:
#             print('Failed: {}'.format(proxy_dict[key]))


# In[ ]:


#來源二
# df = pd.read_excel('MyProxyList.xlsx')
# df = df.dropna()
# df.columns = [ x.replace(' ','') for x in df.columns ]
# df = df[[ 'high-anonymous' in x for x in df['Anonymitylevel']]].reset_index(drop=True)

# ActIps_2 = []

# for i in range(len(df)):
#     proxy = df['IPaddress'][i].replace(' ','')
#     proxy_dict = {} 
#     key   = 'http'
#     proxy_dict[key] ='http://'+proxy

#     try:
#       # 隨機找的一篇新聞即可
#         url = 'https://seekingalpha.com/earnings/earnings-call-transcripts'
#         resp = requests.get(url, proxies=proxy_dict, timeout=2)

#         if str(resp.status_code) == '200':
#             ActIps_2.append(proxy_dict[key])
#             print('Succed: {}'.format(proxy_dict[key]))
#             resp_check = requests.get(url="https://blog.sodsec.com/ip.php",proxies=proxy_dict, timeout=2)
#             print(resp_check.text)
#         else:
#             print('Failed: {}'.format(proxy_dict[key]))

#     except:
#             print('Failed: {}'.format(proxy_dict[key]))


# In[ ]:


# #來源三
# r =  requests.get('https://www.us-proxy.org/') 
# soup = BeautifulSoup(r.text, 'lxml')
# trs = soup.select("#proxylisttable tr")
# proxy_list = []
# for tr in trs:
#     tds = tr.select("td")
#     if len(tds) > 6:
#         ip = tds[0].text
#         port = tds[1].text
#         anonymity = tds[4].text
#         ifScheme = tds[6].text
#         if ifScheme == 'yes': 
#             scheme = 'https'
#             #if anonymity == 'anonymous':
#             proxy = "%s://%s:%s"%(scheme, ip, port)
#             print(proxy)
#             proxy_list.append(proxy)            
#         else: 
#             scheme = 'http'

# ActIps_3 = []
# for proxy in proxy_list:
#     proxy_dict = {}
#     key   = proxy.split('://')[0].replace('https','http')
#     proxy_dict[key] = proxy.replace('https','http')
    
#     key   = proxy.split('://')[0]
#     proxy_dict[key] = proxy

#     try:
#       # 隨機找的一篇新聞即可
#         url = 'https://www.chinatimes.com/realtimenews/20200205004069-260408'
#         resp = requests.get(url, proxies=proxy_dict, timeout=2)

#         if str(resp.status_code) == '200':
#             ActIps_3.append(proxy_dict[key])
#             print('Succed: {}'.format(proxy_dict[key]))
#             resp_check = requests.get(url="https://blog.sodsec.com/ip.php",proxies=proxy_dict, timeout=2)
#             print(resp_check.text)

#         else:
#             print('Failed: {}'.format(proxy_dict[key]))
#     except:
#             print('Failed: {}'.format(proxy_dict[key]))


# In[ ]:


ActIps_1 = []
#來源一
r=requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&anonymity=elite')
ips = [ x for x in r.text.split('\r\n') if  x !='']
df = pd.DataFrame(ips,columns=['Proxy'])
df = df.sample(frac=1, axis=0).reset_index(drop=True)
work_count = 0
for i in range(len(df)):
    if work_count == 20:
        break
    proxy   = str(df['Proxy'][i]).replace(' ','')

    
    proxy_dict = {}
    key   = 'https'
    proxy_dict[key] ='socks4://'+proxy

    try:
      # 隨機找的一篇新聞即可
        url = 'https://seekingalpha.com/earnings/earnings-call-transcripts'
        resp = requests.get(url, proxies=proxy_dict, timeout=2)

        if str(resp.status_code) == '200':


            resp_check = requests.get(url="https://blog.sodsec.com/ip.php",proxies=proxy_dict, timeout=2)
            print(resp_check.text)
            print('Succed: {}'.format(proxy_dict[key]))
            ActIps_1.append(proxy_dict[key])
            work_count += 1
            print('work_count: {}'.format(work_count))
        else:
            
            #print('Failed: {}'.format(proxy_dict[key]))
            pass

    except:
            #print('Failed: {}'.format(proxy_dict[key]))
            pass


 
# In[20]:



resource_name = get_proxyscrape_resource(proxytype='socks4', anonymity='anonymous')
collector = create_collector('socks4', 'socks4')


# In[21]:


proxies = collector.get_proxies({'anonymous': True})
ActIps_2 = []
df = pd.DataFrame(proxies)
df = df.sample(frac=1, axis=0).reset_index(drop=True)
work_count = 0
for i in range(len(df)):
    if work_count == 20:
        break
    proxy   = str(df['host'][i]+':'+df['port'][i]).replace(' ','')

    
    proxy_dict = {}
    key   = 'https'
    proxy_dict[key] ='socks4://'+proxy

    try:
      # 隨機找的一篇新聞即可
        url = 'https://seekingalpha.com/earnings/earnings-call-transcripts'
        resp = requests.get(url, proxies=proxy_dict, timeout=2)

        if str(resp.status_code) == '200':


            resp_check = requests.get(url="https://blog.sodsec.com/ip.php",proxies=proxy_dict, timeout=2)
            print(resp_check.text)
            print('Succed: {}'.format(proxy_dict[key]))
            ActIps_2.append(proxy_dict[key])
            work_count += 1
            print('work_count: {}'.format(work_count))
        else:
            
            #print('Failed: {}'.format(proxy_dict[key]))
            pass

    except:
            #print('Failed: {}'.format(proxy_dict[key]))
            pass


# In[ ]:


ActIps = ActIps_1+ActIps_2


# In[ ]:


ActIps


# In[ ]:


len(ActIps)


# # 一、進入seekingalpha 網頁 判斷con call 標題是否重複

# In[ ]:


with open('./transcript_title/transcript_title.txt','r',encoding='utf-8') as fp:
     existing_articles = fp.readlines()
fp.close()
existing_articles  = [ x.replace('\n','') for x in  existing_articles ]
existing_articles_titles = [ x.split('title href : ')[0] for x in existing_articles]
existing_articles_links =  [ x.split('title href : ')[1] for x in existing_articles]
print("原標題共有 {} 項".format(len(existing_articles_titles)))


# In[ ]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://seekingalpha.com/earnings/earnings-call-transcripts')
new_articles_titles = driver.find_elements_by_class_name("dashboard-article-link")
new_articles_titles = [ x.text for x in new_articles_titles ]
new_articles_links  = driver.find_elements_by_class_name("dashboard-article-link")
new_articles_links  = [ x.get_attribute('href') for x in new_articles_links ]
print("網頁上 Con call 標題共有 {} 項".format(len(new_articles_titles)))

update_articles_titles = [ x for x in new_articles_titles  if x not in existing_articles_titles ]
update_articles_links  = [ x for x in new_articles_links   if x not in existing_articles_links ]
print("須更新標題共有 {} 項".format(len(update_articles_titles)))

driver.close()


# # 版本一

# In[ ]:



def change_ip_info(url,ActIps,i):


    user_agent_list=[
            'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)',
            'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)',
            'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)',
            'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
            'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',  
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
        ]
    referer_list=[
            'https://www.sogou.com/',
            'http://blog.csdn.net/',
            'https://www.baidu.com/',
             'https://www.google.com/',
        ]

    header={
            'User-Agent':random.choice(user_agent_list), 
            'Referer':random.choice(referer_list)
        }
    ip=ActIps[i]
    proxy_dict = {}
    key   = ip.split('://')[0]
    proxy_dict[key] = ip     
    print(proxy_dict)
    
    try:
        html=requests.get(url,headers=header, proxies=proxy_dict,timeout=(3,7))  
        print('成功訪問')
    except:
        html=requests.get(url,headers=header,timeout=(3,7))  
        print('失敗 以自己IP在訪問一次')
    return html


# In[ ]:


sleep_min_list = [ 30 ]
j = 0
sleep_min = sleep_min_list[j]
print('開始測試休眠 {} 秒'.format(300))

print('開始測試 {} 秒'.format(sleep_min))
drouble_shooting = []
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver_tans = webdriver.Chrome(ChromeDriverManager().install())
driver_tans.get('https://translate.google.com.tw/')
for i in range(len(update_articles_links)):
    sleep =  np.random.randint(sleep_min)+np.random.random()
    print('-------休眠 {} 秒'.format(sleep))
    time.sleep(sleep)
    
    update_article_link  = update_articles_links[i]
    update_article_title = update_articles_titles[i]
    print("--------------------------------------處理連結{}----------------------------------".format(update_article_link))
    print("--------------------------------------處理連結標題{}----------------------------------".format(update_article_title))
    try:

        r =  change_ip_info(update_article_link,ActIps,i)
        soup = BeautifulSoup(r.text, 'html.parser')
        content = soup.find(id="page_content_wrapper").find_all('p')
        input_text = ''
        mail_output_text = ''
        mail_output_text_chi = ''
        for x in  content:
            #print(x.text)
            input_text += x.text
            if (len(input_text) > 3000)&(x != content[-1]):

                driver_tans.get('https://translate.google.com.tw/')
                time.sleep(1)
                inputElement    = driver_tans.find_element_by_id('source')
                inputElement.send_keys( input_text )
                time.sleep(1.5)
                out_put_text = driver_tans.find_element_by_xpath(
                    "//div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div").text


                #print(input_text)
                #print(out_put_text)
                mail_output_text_chi += out_put_text+'\n'
                mail_output_text += input_text+'\n'
                input_text = ''
                out_put_text = ''
            elif (len(input_text) > 3000)&(x == content[-1]):

                driver_tans.get('https://translate.google.com.tw/')
                time.sleep(1)
                inputElement    = driver_tans.find_element_by_id('source')
                inputElement.send_keys(input_text  )
                time.sleep(1.5)
                out_put_text = driver_tans.find_element_by_xpath(
                    "//div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div").text


                #print(input_text)
                #print(out_put_text) 
                mail_output_text_chi += out_put_text+'\n'  
                mail_output_text += input_text+'\n'
                input_text = ''    
                out_put_text = ''
            elif (len(input_text) <= 3000)&(x == content[-1]):

                driver_tans.get('https://translate.google.com.tw/')
                time.sleep(1)
                inputElement    = driver_tans.find_element_by_id('source')
                inputElement.send_keys(input_text )
                time.sleep(1.5)
                out_put_text = driver_tans.find_element_by_xpath(
                    "//div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div").text

                #print(input_text)
                #print(out_put_text) 
                mail_output_text_chi += out_put_text+'\n'
                mail_output_text += input_text+'\n'
                input_text = ''            
                out_put_text = ''

        # 開啟檔案
        fp = open(".//result_text//{}.txt".format(update_article_title), "w",encoding='utf-8')
        # 寫入到檔案
        fp.write(mail_output_text)
        # 關閉檔案
        fp.close()
        # 開啟檔案
        fp = open(".//result_text//{}.txt".format(update_article_title+'_chi'), "w",encoding='utf-8')
        # 寫入到檔案
        fp.write(mail_output_text_chi)
        # 關閉檔案
        fp.close()
        # Outlook版本------------------------------------------------------------------------------------------------------
    #     outlook = win32.Dispatch('outlook.application')
    #     mail = outlook.CreateItem(0)
    #     receivers = ['Solon@cathaysite.com.tw;matt.y@cathaysite.com.tw;Xavior@cathaysite.com.tw;xavior8100483@gmail.com']
    #     mail.To = receivers[0]
    #     mail.Subject ='Transcript_Seekingalpha'
    #     attachment1 = "C://Users//User//Desktop//seekingalpha//result_text//{}.txt".format(update_article_title)

    #     mail.Attachments.Add(Source=attachment1)
    #     mail.display()
    #     mail.Body = out_put_text
    #     mail.Send()
        # Gmail版本------------------------------------------------------------------------------------------------------
        # Account infomation load
        gmailUser ='linshenghua82@gmail.com'
        gmailPasswd = 'efxrbgprulmeciin'
        to = ["Solon@cathaysite.com.tw","matt.y@cathaysite.com.tw","Xavior@cathaysite.com.tw","xavior8100483@gmail.com"]

        # Create message
        message = MIMEMultipart()
        message['Subject'] = update_article_title
        message['From'] = gmailUser
        #message['To'] = to

        # Mail content
        message.attach(MIMEText('{}'.format( update_article_title), 'plain', 'utf-8'))

        # File
        file = MIMEText(open("C://Users//User//Desktop//seekingalpha//result_text//{}.txt".format(update_article_title), 'r', encoding='utf-8').read(), 'base64', 'utf-8')
        file['Content-Type'] = 'application/octet-stream'
        file['Content-Disposition'] = 'attachment; filename='+"{}.txt".format(update_article_title)
        message.attach(file)
        file = MIMEText(open("C://Users//User//Desktop//seekingalpha//result_text//{}.txt".format(update_article_title+'_chi'), 'r', encoding='utf-8').read(), 'base64', 'utf-8')
        file['Content-Type'] = 'application/octet-stream'
        file['Content-Disposition'] = 'attachment; filename='+"{}.txt".format(update_article_title+'_chi')
        message.attach(file)
        # Set smtp
        smtp = smtplib.SMTP("smtp.gmail.com:587")
        smtp.ehlo()
        smtp.starttls()
        smtp.login(gmailUser, gmailPasswd)

        # Send mail
        smtp.sendmail(message['From'], to, message.as_string())
        print('Send mails OK!')
        
        
        # 將所有新標題寫入到檔案
        with open('./transcript_title/transcript_title.txt','a',encoding='utf-8') as fp:
            lines = update_article_title+'title href : '+update_article_link+'\n' 
            fp.writelines(lines)
        fp.close()
        driver.close()
    except:
        drouble_shooting.append(update_article_link)


# In[ ]:




