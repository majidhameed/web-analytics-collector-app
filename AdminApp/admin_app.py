'''
Created on Mar 31, 2014

@author: Majid Hameed
'''

import bottle, types, pymongo
from bottle import Bottle, request, response, static_file
from json import dumps
from paste import httpserver
import datetime
import admin_util

DEFAULT_PORT = 8181
APP_NAME = "AdminApp"
HOST = '0.0.0.0'
DEV = False

app = Bottle()


@app.get('/')
def index():
    return present_login()

@app.get('/login')
def present_login():
    remote_ip = request.environ['REMOTE_ADDR']
    if admin_util.is_session_exists(remote_ip):
        print 'admin home'
        return bottle.template("admin", dict())
    else:
        return bottle.template("login", dict(login="", password="", login_error=""))
    
@app.post(('/login'))
def do_login():
    login = bottle.request.forms.get("login")
    password = bottle.request.forms.get("password")
    remote_ip = request.environ['REMOTE_ADDR']
    print "login:", login, "password:", password
    if admin_util.is_session_exists(remote_ip, login):
        print 'already login in'
        bottle.redirect("/admin")
    elif admin_util.is_valid_login(login, password):
        print 'valid login'
        admin_util.add_session(login, remote_ip)
        bottle.redirect("/admin")
    else:
        print "invalid login"
        bottle.redirect("/login")
        
@app.get('/admin')
def admin_home():
    return present_login()

@app.get('/tracking_code')
def tracking_code():
    print "tracking code page"
    tracking_code = 'http://'  + request.environ['HTTP_HOST'].split(':')[0] + '/t'
    return bottle.template('tracking_code', dict(tracking_code=tracking_code))

@app.get('/account_view/<account>')
def account_view(account):
    print 'account:' + account
    website = account.decode('base64', 'strict')
    template_dict = {
'website':website,
    }
    return bottle.template('account_view', template_dict)

@app.post('/accounts_by_date_range')
def accounts_by_date_range():
    from_date_str = request.forms.get('from_date')
    to_date_str = request.forms.get('to_date')
    website = request.forms.get('website')
    print from_date_str, to_date_str
    date1 = from_date_str.split('/')
    from_date=datetime.datetime(int(date1[2]),int(date1[0]),int(date1[1]))
    
    to_date = None
    if len(to_date_str) is not 0:
        date2 = to_date_str.split('/')
        to_date=datetime.datetime(int(date2[2]),int(date2[0]),int(date2[1]))
    data = admin_util.account_by_date_range(website,from_date, to_date)
    print data
    response.content_type = 'application/json'
    return dumps(data)
    
@app.get('/accounts')
def accounts_index():
    account_total = admin_util.accounts_total()
    template_dict  = {
'accounts_total': account_total,
'accounts_today': admin_util.accounts_by_date('today'),
'accounts_yesterday': admin_util.accounts_by_date('yesterday'),
'accounts_month': admin_util.accounts_by_date('month'),
'accounts_url': admin_util.accounts_urls(account_total),
    }
    return bottle.template('accounts_index', template_dict)

@app.route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='')
    
bottle.debug(DEV)
app.run(server='paste', host=HOST, port=DEFAULT_PORT, reloader=DEV)