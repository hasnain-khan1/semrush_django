from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .forms import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from datetime import datetime
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import threading
import time
import urllib.request
from collections import OrderedDict
from urllib.parse import urlparse
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import pandas as pd
from bs4 import BeautifulSoup
import json
from .consumers import *
import time
from django.http import JsonResponse
# @login_required
import threading
# @asyncio.coroutine
def dashboard(request):
    # context={
    #     'user':request.user
    # }
    # for i in range(1,10):

    #     channel_layer = get_channel_layer()
    #     async_to_sync (channel_layer.group_send)(
    #     "messages_group", {
    #             "type": "next_notifi",
    #             "value": i,
    #             "body": i+1,
    #             "title": i+2,
    #             "description": i+2,
    #             "wordcount": i+2,
    #             "response_time": i,
    #             })
    #     time.sleep(1)
    # if request.method == 'POST':
    #     if 'sites' in request.POST:
    #         print(request.POST['sites'])
            
            # channel_layer = get_channel_layer()
            # async_to_sync(channel_layer.group_send)(
            # "messages_group", {
            #         "type": "next_notifi",
            #         "value": json.dumps('Success towards django'),
            #         })
            # try:
            #     print("starting....")
            #     site=request.POST['sites']
            #     #site = "https://www.python.org/"
            #     # site = "https://chasereiner.com"
            #     strt(site)
            #     print("Stopped.....")
            #     # print("Time Spent:", time.time() - t1)
            # except:
            #     pass

    return render(request, 'user/dashboard.html')

    # return render(request, 'user/manager_admin_dashboard.html')

def dashboard(request):
    # for i in range(1,10):
    #     channel_layer = get_channel_layer()
    #     async_to_sync (channel_layer.group_send)(
    #     "notifications_group", {
    #             "type": "next_notifi",
    #             "value": i,
    #             })
    #     time.sleep(1)
    #     print(i)
    # if request.method == 'POST':
    #     if 'sites' in request.POST:
    #         print(request.POST['sites'])
    #         try:
    #             print("starting....")
    #             site=request.POST['sites']
    #             #site = "https://www.python.org/"
    #             # site = "https://chasereiner.com"
    #             strt(site)
    #             print("Stopped.....")
    #             # print("Time Spent:", time.time() - t1)
    #         except:
    #             pass
    return render(request, 'user/dashboard.html')

@login_required
@csrf_exempt
def sitesdata(request):
    print('asim')
    print('raza')
    print('wow')
    print('bye')
    # return render(request, 'user/dashboard.html',context)




def link_extract(domain):
    parser = 'html.parser'
    resp = urllib.request.urlopen(domain)
    domain = urlparse(domain).netloc
    domain = "https://" + domain
    soup = BeautifulSoup(resp, parser)
    links2 = []
    links3 = []
    for link in soup.find_all('a', href=True):
        if (str(link['href'])[0]) == "/" and len(str(link["href"])) > 2:
            links2.append(domain + link["href"])
    for link in soup.find_all('a', href=True):
        if domain in (str(link["href"])):
            links2.append(domain + link["href"])
        else:
            links3.append(link["href"])
    links2 = list(OrderedDict.fromkeys(links2))
    return links2, links3


def description(lnks, external):
    for url in lnks:
        try:
            desciption = ' '
            description_selectors = [
                {"name": "description"},
                {"name": "og:description"},
                {"property": "description"}
            ]
            parser = 'html.parser'
            t11 = time.time()
            resp = urllib.request.urlopen(url)
            t2 = time.time()
            response = t2 - t11
            status_code = resp.getcode()
            print(status_code)
            if status_code == 200:
                status = "OK"
            else:
                status = "Error"

            soup = BeautifulSoup(resp, parser)
            title = soup.title.string
            text = (soup.get_text())
            count = len(text.split())
            # print(count)
            for selector in description_selectors:
                description_tag = soup.find(attrs=selector)
                if description_tag and description_tag.get('content'):
                    desciption = description_tag['content']
                    break
                else:
                    desciption = "None"
            print("---------------------------------------------------")
            print("link:", url.replace("\n", ""), "\nTitle:", title.replace("\n", ""), "\nDescription:",
                  desciption.replace("\n", ""),
                  "\nWord Count:", count, "\n", " Response_time", t2 - t11)
            print("---------------------------------------------------")
            print(";ayeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            # channel_layer = get_channel_layer()
            # async_to_sync (channel_layer.group_send)(
            # "notifications_group", {
            #         "type": "next_notifi",
            #         "value": json.dumps('Success towards django'),
            #         "body": url.replace("\n", ""),
            #         "title": title.replace("\n", ""),
            #         "description": desciption.replace("\n", ""),
            #         "wordcount": count,
            #         "response_time": t2 - t11,
            #         })
            print('thissssssssssssssssssssssssssssssssssssssssssssssssssssssssss')
            print(url)
            # print(short)
            print(title)
            print(desciption)
            print(count)
            print(response)
            channel_layer = get_channel_layer()
            async_to_sync (channel_layer.group_send)(
            "notifications_group", {
                    "type": "next_notifi",
                    "value": url,
                    # "body": short,
                    "title": title,
                    "description": desciption,
                    "wordcount": count,
                    "response_time": response,
                    })
            # time.sleep(3)
            if count < 150:
                short = True
            else:
                short = False
            data1 = [url, count, title, desciption, status_code, status, response, short]
            df = pd.DataFrame(data1,
                              index=["Url", "Words", "Title", "Description", "Response", "staus_code",
                                     "Load_time", "Short_content"])
            df = df.T
            df.to_csv("All_links.csv", encoding="utf-8", mode='a', index=False, header=False)
            if desciption == "None" or short:
                data2 = [url, count, title, "None", status, status_code, response, short]
                df2 = pd.DataFrame(data2, index=["Url", "Words", "Title", "Description", "Response", "staus_code",
                                                 "Load_time", "Short_content"])
                df2 = df2.T
                df2.to_csv("Missing_description.csv", encoding="utf-8", mode='a', index=False, header=False)
        except:
            pass
    data3 = [external]
    df = pd.DataFrame(data3, index=["External_links"])
    df = df.T
    df.to_csv("External_links.csv", encoding="utf-8", index=False, header=True)


def strt(dom):
    print("Started......")
    print("Wait! Link Scraping.....")
    external2 = []
    external3 = []

    if "https://" not in dom:
        dom = "https://" + dom
    lk, external = link_extract(dom)
    lk2 = []
    lk3 = []
    print("Depth1 links")
    lk = list(OrderedDict.fromkeys(lk))
    for k in lk:
        print(k)
        try:
            t, external2 = link_extract(k)
            for j in t:
                print(j)
                lk2.append(j)
        except:
            pass
    print("Depth2 Link")
    lk2 = list(OrderedDict.fromkeys(lk2))
    for k in lk2:
        try:
            t, external3 = link_extract(k)
            for j in t:
                print(j)
                lk3.append(j)
        except:
            pass
    mergedlist = (lk + lk2 + lk3)
    extrnl = (external2 + external3 + external)
    mergedlist = list(OrderedDict.fromkeys(mergedlist))
    extrnl = list(OrderedDict.fromkeys(extrnl))
    mergedlist.append(dom)
    # print(mergedlist)
    data2 = [" ", " ", " ", " ", " ", "", " ", ""]
    df2 = pd.DataFrame(data2,
                       index=["Url", "Words", "Title", "Description", "Response", "staus_code",
                              "Load_time", "Short_content"])
    df2 = df2.T
    df2.to_csv("Missing_description.csv", encoding="utf-8", index=False)
    df2.to_csv("All_links.csv", encoding="utf-8", index=False)

    if len(mergedlist) > 10:
        l1 = int(len(mergedlist) / 2)
        lst1 = mergedlist[0:l1]
        lst2 = mergedlist[l1:]
        t3 = threading.Thread(target=description, args=(lst1, extrnl,))
        t2 = threading.Thread(target=description, args=(lst2, extrnl,))
        t3.start()
        t2.start()
        t3.join()
        t2.join()
    else:
        description(mergedlist, extrnl)

def gen_data(request):
    s=request.POST['siting']
    print('s')
    print(s)
    try:
        print("starting....")
        # site=request.POST['sites']
        #site = "https://www.python.org/"
        # site = "https://chasereiner.com"
        # strt(s)
        # print("Stopped.....")
        print("over to threads")
        CreateStudentsThread(s).start()
        # print("Time Spent:", time.time() - t1)
    except:
        pass
    return JsonResponse({'status': 200})


class  CreateStudentsThread(threading.Thread):

    def __init__(self, site):
        self.site= site
        threading.Thread.__init__(self)

    def run(self):
        print("i m in runnnnnnnnnnnnnnnnn....")
        try:
            print("starting....")
            print(self.site)
            # site=request.POST['sites']
            #site = "https://www.python.org/"
            # site = "https://chasereiner.com"
            strt(self.site)
            print("Stopped.....")
            # CreateStudentsThread(site).start()
            # print("Time Spent:", time.time() - t1)
        except:
            pass








# if __name__ == '__main__':
#     while True:
#         try:
#             t1 = time.time()
#             site = str(input("please input the domain name:"))
#             print("starting....")
#             #site = "https://www.python.org/"
#             # site = "https://chasereiner.com"
#             strt(site)
#             print("Stopped.....")
#             print("Time Spent:", time.time() - t1)
#         except:
#             pass
