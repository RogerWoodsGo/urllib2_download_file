#!/usr/bin/python2.6
import os
import urllib2
import re
LOGIN = "www.linuxidc.com"
PASSWD = "www.linuxidc.com"
URL0 = "http://linux.linuxidc.com"
URL ="http://linux.linuxidc.com/2013%E5%B9%B4%E8%B5%84%E6%96%99/"
FILE_PATH = "/media/Documents/Linux/linuxidc/"
#pattern_file = re.compile(r'.*\.[txt|rar|zip|gz|tar]',re.DOTALL)
from ntlm import HTTPNtlmAuthHandler
from BeautifulSoup import BeautifulSoup

def open_url(url):
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, url, LOGIN, PASSWD)
    # create the NTLM authentication handler
    auth_NTLM = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)

    # create and install the opener
    opener = urllib2.build_opener(auth_NTLM)
    urllib2.install_opener(opener)
    return url;
def download_flie(url0):
    # retrieve the result
    url = open_url(url0)
    response = urllib2.urlopen(url)
    html_doc = response.read()
    soup0 = BeautifulSoup(html_doc)
    link_list = []
    html_pre = soup0.find('pre')
    print(type(html_pre))
    #print(html_pre.findAll('a'))
    #soup = BeautifulSoup(html_pre)
    for link in html_pre.findAll('a'):
       link_list.append(link['href'])
    print(link_list)
    link_list = link_list[1:]
    response.close()
    return link_list
def recurive(url):
    tmp_url = open_url(url)
    tmp_list = download_flie(tmp_url)
    print(tmp_list)
    count = 0
    print(tmp_list)
    for f_name in tmp_list:
        if(f_name.endswith("/")):
            #with open(f_name,"wb") as local_file:
                #local_file.write(url)
            recurive(URL0 + f_name)
            count += 1
        else:
            print(os.path.basename(f_name))
            tree_name = FILE_PATH + os.path.basename(f_name)
            with open(tree_name,"wb+") as local_file:
                local_file.write(urllib2.urlopen(URL0 + f_name).read())

if __name__ == '__main__':
    recurive(URL)
