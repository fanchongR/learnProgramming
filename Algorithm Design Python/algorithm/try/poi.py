# -*- coding: utf-8 -*-
import urllib.request
import os
import json
import glob
import re
import traceback
import time

os.chdir(r"C:\Users\user\Desktop\tfpoi")



def positionpaser(lon, lat):
    url = "http://restapi.amap.com/v3/geocode/regeo?location=" + str(lon) + "," + str(lat) + "&extensions=base&output=json&key=51a107a394fe550d2c133d3e5300e80a&radius=1000&extensions=all"
    temp = urllib.request.Request(url)
    temp = urllib.request.urlopen(temp,timeout=1)
    temp = temp.read().decode('utf8')
    p = re.compile("\[\]")
    temp = p.sub("\"\"", temp)
    result = json.loads(temp)
    if result["status"] == '0': return ("", "", "", "", "", "", "", "","")
    addressComponent = result['regeocode']['addressComponent']
    if 'businessAreas' in addressComponent and len(addressComponent['businessAreas'][0]) > 0:
        compname = addressComponent['businessAreas'][0]['name']
    else:
        compname = ""
    return addressComponent['province'], addressComponent['city'], addressComponent['district'], \
           addressComponent['neighborhood']['name'], addressComponent['neighborhood']['type'], \
           addressComponent['building']['name'], addressComponent['building']['type'], compname,result['regeocode']['formatted_address']


# RESIDENCE.write("mob\tprovince\tcity\tdistrict\tneighborhood_name\tneighborhood_type\tbuilding_name\tbuilding_type\tbusinessarea_name\n")
ERROR_NUM = 0


OUT = open("beijingpoi_poi_parsed.txt", "w")
IN = open("beijingpoi.txt")
#HEADER = IN.readline()

LINE = 0
for line in IN:

    LINE += 1
    if LINE % 100 == 0:print(LINE)

    fields = line.strip().split('\t')
    
    is_finish = False
    repeat_count = 0
    while not is_finish and repeat_count < 10:
        try:
            position = positionpaser(fields[0], fields[1])
            OUT.write('\t'.join(fields) + '\t' + '\t'.join(position) + '\n')
            is_finish = True
        except Exception as e:
            ERROR_NUM += 1
            traceback.print_exc()
            is_finish = False
            repeat_count += 1
    
    
OUT.close()

print("ERROR NUM:", ERROR_NUM)