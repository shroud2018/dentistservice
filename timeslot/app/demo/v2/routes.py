# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.reverse import Reverse
from .api.doctor_avaliable import DoctorAvaliable
from .api.cancel import Cancel


routes = [
    dict(resource=Reverse, urls=['/reverse'], endpoint='reverse'),
    dict(resource=DoctorAvaliable, urls=['/doctor_avaliable'], endpoint='doctor_avaliable'),
    dict(resource=Cancel, urls=['/cancel'], endpoint='cancel'),
]