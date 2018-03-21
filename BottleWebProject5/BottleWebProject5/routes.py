"""
Routes and views for the bottle application.
"""

from app import *
from bottle import route, view, request, template
from datetime import datetime, timedelta
import pymongo
from pymongo import MongoClient


@route('/')
@route('/home')
@view('LoginForm')
def LoginCheck():
    """Renders the Login page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/submitform', method = 'GET')
@route('/submitform', method = 'POST')
def submitform():
    username = request.forms.get('username')
    password = request.forms.get('password')
    # print(client)
    # print(db)
    # print(col)
    foundobj = col.find_one({"username":username})
    if foundobj != None :
        if foundobj['usertype'] != 'admin':
            temp1 = datetime.now()
            temp2 = datetime.strptime(foundobj['logindetails'][-1]['logindate']+' '+foundobj['logindetails'][-1]['logintime'], '%d/%m/%Y %H:%M:%S')
            if temp1 > temp2 and (temp1 - temp2).seconds > 5*60 :
                col.find_one_and_update({'username':username}, {'$push' : {'logindetails' : {'logintime': datetime.strftime(datetime.today(), "%H:%M:%S") , 'logindate': datetime.strftime(datetime.today(), "%d/%m/%Y"), 'loginip': '10.142.12.118'} }} )
        infoparam = dict(
        title='About',
        message='Your LoginInfo page.',
        year=datetime.now().year,
        username = foundobj['username'],
        object = foundobj,
        collection = col,
        IP = request.environ['REMOTE_ADDR']
    )
    
        if foundobj['usertype'] == 'admin':
            return template('redirect_admin.tpl',infoparam)
        else :
            return template('redirect_teacher.tpl',infoparam)
    else : 
        infoparam = dict(
            title='About',
            message='Your application description page.',
            year=datetime.now().year
        )
        return template('redirect_wrong', infoparam)

@route('/redirect_to_create')
@view('UserCreation')
def redirect_to_create():
    infoparam = dict(
            title='About',
            message='Your application description page.',
            year=datetime.now().year
        )
    return template('UserCreation', infoparam)

@route('/createuser', method = "POST")
@view('redirect_admin')
def createuser():
    col.insert_one({"username":request.forms.get('username'), "usertype":"teacher" , "password":request.forms.get('password'), 'logindetails' : [] })
    infoparam = dict(
        title='About',
        message='Your LoginInfo page.',
        year=datetime.now().year,
        collection = col
    ) 
    return template('redirect_admin', infoparam)