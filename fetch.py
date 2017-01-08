# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 11:04:34 2016

@author: Wiiill
"""
    
import urllib
import time

def fetch():
    start_time = time.time()
    count=0
    for index in indexlist:
        count+=1
        print("["+str(count)+"]"+" fetching: "+index)
       # if(index=="COM7"):
        #    urllib.urlretrieve("http://www.set.or.th/set/companyholder.do?symbol="+index+"&ssoPageId=6&language=en&country=US","C:\Users\Wiiill\Desktop\stockBhum\data\COMSEVEN.html")
         #   continue
        urllib.urlretrieve("http://www.set.or.th/set/companyholder.do?symbol="+index+"&ssoPageId=6&language=en&country=US","C:\Users\Wiiill\Desktop\stockBhum\data\\"+index+".html")
        """if(count%20==0):
            print("sleeping every 20 pages")
            time.sleep(3)
    """
    total_fetch_time = time.time()-start_time
    print "Fetching done used time: "+str(total_fetch_time)+" seconds"
    
def find():
    for index in indexlist:
        if 'นายธนวัฒน์ พันธุ์โกศล' in open('C:\Users\Wiiill\Desktop\stockBhum\data\\'+index+'.html').read():
            print index
    
indexlist = [line.rstrip('\n') for line in open('index')]
#fetch()
find()