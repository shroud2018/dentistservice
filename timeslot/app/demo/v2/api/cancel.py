# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import csv

class Cancel(Resource):

    def post(self):
        result = []
        upload = g.json
        csvFile = open("data.csv")
        reader = csv.DictReader(csvFile)
        name = upload['name']
        time = upload['time']
        
        for item in reader:
            if(item['name'] == name and item['time']==time):
                item['avaliable'] = '0'
            result.append(item)
        csvFile.close()
        for item in result:
            print(item)
        fieldnames = ['name','time','avaliable']
        csvFile_w = open("data.csv",'w')
        writer = csv.DictWriter(csvFile_w,fieldnames=fieldnames)
        writer.writeheader()
        for item in result:
            writer.writerow(item)
        return None, 200, None
