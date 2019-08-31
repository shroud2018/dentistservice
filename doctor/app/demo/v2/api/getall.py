# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import csv

class Getall(Resource):

    def get(self):
        result = []
        csvFile = open('data.csv')
        reader = csv.DictReader(csvFile)
        for item in reader:
            tuple_use = {'name':'a','location':'b','level':'c'}
            tuple_use['name'] = item['name']
            tuple_use['location'] = item['location']
            tuple_use['level'] = item['level']
            result.append(tuple_use)
        return result, 200, None
