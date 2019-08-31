
from __future__ import absolute_import, print_function

from flask import request, g, jsonify

from . import Resource
from .. import schemas
from rivescript import RiveScript
import requests
import json

bot = RiveScript()
bot.load_directory('C:/9322ass3/chatbot/app/demo/v2/api/brain')
bot.sort_replies()
class Ask(Resource):

    def post(self):

        result = []
        ask_q = g.json
        
        msg = ask_q['message']
        feedback = bot.reply("localuser",msg)
        if (feedback == '0'):
            reply = "Sorry, I cannot understand. If you need to reverse, please input the name of the doctor and the time. if you want to see all the doctor information or timeslot, just input doctor information or timeslot"
        elif (feedback == '1'):
            #get doctor information
            url = 'http://192.168.99.100:8088/v2/getall'
            result = requests.get(url)
            result1 = result.json()
            reply = ''
            for item in result1:
                reply = reply + 'name: '+item['name']+' level: '+item['level']+' location: '+item['location']+' || ' 
            
        elif (feedback == 'cris wu' or feedback == 'xk cai' or feedback == 'bl qiao'):
            name = feedback.title()
            url = "http://192.168.99.100:8088/v2/getadoctor?Doctorname="
            url_name = url + name.replace(' ','%20')
            result = requests.get(url_name)
            reply = result.json()
        elif (feedback == '3'):
            url = "http://192.168.99.100:8080/v2/reverse"
            result = requests.get(url)
            result1 = result.json()
            reply = ''
            temp = ''
            for item in result1:
                if(temp!=item['name']):
                    reply = reply +item['name']+': '+item['time']+' | '
                    temp = item['name']
                else:
                    reply = reply+item['time']+' | '
                    
                    
           
        elif(feedback[0] == '4'):
            name_array = feedback.split(' ',1)
            name = name_array[1]
            url = "http://192.168.99.100:8080/v2/doctor_avaliable?Doctorname="
            name = name.title()
            url = url + name.replace(' ','%20')
            result = requests.get(url)
            result1 = result.json()
            reply = ''
            temp = ''
            for item in result1:
                if(temp!=item['name']):
                    reply = reply +item['name']+': '+item['time']+' | '
                    temp = item['name']
                else:
                    reply = reply+item['time']+' | '

            
        elif (feedback[0] == '5'):
            name_array = feedback.split(' ')
            name =str(name_array[1]).title()+' '+str(name_array[2]).title()
            time = name_array[4]
            if(len(time) == 4):
                str_time = time[0]+time[1]+':'+time[2]+time[3]
            else:
                str_time = time[0]+':'+time[1]+time[2]
            headers = {'Content-Type': 'application/json'}
            data = {"name": name,"time": str_time}
            a = json.dumps(data)
            url ="http://192.168.99.100:8080/v2/reverse"
            result = requests.post(url=url, headers = headers, json = data)
            reply = "Your appointment has succeed! Thank you!"
        elif (feedback[0] == '6'):
            name_array = feedback.split(' ')
            name =str(name_array[1]).title()+' '+str(name_array[2]).title()
            time = name_array[4]
            if(len(time) == 4):
                str_time = time[0]+time[1]+':'+time[2]+time[3]
            else:
                str_time = time[0]+':'+time[1]+time[2]
            url = "http://192.168.99.100:8080/v2/cancel"
            headers = {'Content-Type': 'application/json'}
            data = {"name":name,"time":str_time}
            result = requests.post(url=url,headers = headers, json = data)
            reply = 'Your ('+name + ' ' + str_time+') has been canceled!'
        elif(feedback[0] == '7'):
            url = "http://192.168.99.100:8088/v2/getadoctor?Doctorname="
            name_array = feedback.split(' ')
            name = name_array[1].title()+'%20'+name_array[2].title()
            url = url + name
            result = requests.get(url)
            result1 = result.json()
            reply = ''
            reply = reply + 'name: '+result1['name']+' level: '+result1['level']+' location: '+result1['location']+' || ' 
        else:
            reply = feedback
            
            
       # print(reply)
        return {'answer':reply}, 200, None
