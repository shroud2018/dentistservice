# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import csv

class DoctorAvaliable(Resource):

    def get(self):
        result = []
        csvFile = open("data.csv")
        reader = csv.DictReader(csvFile)
        upload = g.args
        name = upload['Doctorname']
        for item in reader:
            tuple_time = {'name': 'a','time':'0:00'}
            if (item['avaliable']=='0' and item['name']==name):
                tuple_time['name'] = item['name']
                tuple_time['time'] = item['time']
                result.append(tuple_time)
        print(name)
        return result, 200, None
