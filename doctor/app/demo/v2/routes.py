# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.getall import Getall
from .api.getadoctor import Getadoctor


routes = [
    dict(resource=Getall, urls=['/getall'], endpoint='getall'),
    dict(resource=Getadoctor, urls=['/getadoctor'], endpoint='getadoctor'),
]