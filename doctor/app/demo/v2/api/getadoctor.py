# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas
import csv

class Getadoctor(Resource):

    def get(self):
        print(g.args)
        upload = g.args
        name = upload['Doctorname']
        csvFile = open('data.csv')
        reader = csv.DictReader(csvFile)
        for item in reader:
            tuple_use = {'name':'a','location':'b','level':'c'}
            if(item['name'] == name):
                tuple_use['name'] = item['name']
                tuple_use['location'] = item['location']
                tuple_use['level'] = item['level']
                break

        return tuple_use, 200, None
