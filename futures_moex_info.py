#!/usr/bin/env python
# coding: utf-8
import urllib.request
import json
def func_futures_moex_info(ticket):
    zip_headers = {}
    zip_data = {}
    zip_sec = {}
    # Заголовки для engines
    url = 'https://iss.moex.com/iss/engines/futures/markets/forts.json'
    html = json.loads(urllib.request.urlopen(url).read().decode("utf-8"))
    headers = html['securities']['data']
    for members in headers:
        zip_headers[members[1]] = members[3]
    headers = html['marketdata']['data']
    for members in headers:
        zip_headers[members[1]] = members[3]
    # Engines
    url = 'https://iss.moex.com/iss/engines/futures/markets/forts/boards/RFUD/securities/'+ticket+'.json'
    html = json.loads(urllib.request.urlopen(url).read().decode("utf-8"))
    headers_s = html['securities']['columns']
    data_s = html['securities']['data'][0]
    headers_m = html['marketdata']['columns']
    data_m = html['marketdata']['data'][0]
    for i in range(len(data_s)):
        zip_data[headers_s[i]] = {'ru_name':zip_headers.get(headers_s[i]), 'value':data_s[i]}
    for i in range(len(data_m)):
        zip_data[headers_m[i]] = {'ru_name':zip_headers.get(headers_m[i]), 'value':data_m[i]}
    # Securities
    url = 'https://iss.moex.com/iss/securities/'+ticket+'.json'
    html = json.loads(urllib.request.urlopen(url).read().decode("utf-8"))
    headers = html['description']['data']
    for members in headers:
        zip_sec[members[0]] = {'ru_name':members[1], 'value':members[2]}
    zip_data.update(zip_sec)
    return zip_data
