'''
Created on Mar 29, 2014

@author: Majid Hameed
'''

import pymongo
import time, datetime

connection = pymongo.Connection('mongodb://localhost', safe=True)
db = connection.web_analytics

def is_valid_login(login, password):
    user = {'login':login, 'password':password}
    db_user = db.users.find_one(user)
    return db_user is not None

def is_session_exists(remote_ip, login='admin'):
    login = {'login':login, 'remote_ip':remote_ip}
    login_session = db.sessions.find_one(login)
    return login_session is not None

def add_session(login, remote_ip):
    login = {'login':login, 'remote_ip':remote_ip}
    db.sessions.insert(login)

def remove_session(login, remote_ip):
    login = {'login':login, 'remote_ip':remote_ip}
    db.sessions.remove(login)

def accounts_total():
    query_total_hits = [{'$group':{'_id':'$HTTP_REFERER_WEBSITE','total':{'$sum':1}}}]
    db_result = db.request_detail.aggregate(query_total_hits)
    accounts = {}
    for account in db_result['result']:
        accounts[account['_id']]=account['total']
    return accounts

def accounts_urls(accounts_total):
    acc_urls = {}
    for url in accounts_total:
        if url is not None:
            acc_urls[url] = url.encode('base64', 'strict')
        else:
            acc_urls[url] = 'None'.encode('base64', 'strict')
    return acc_urls

def account_by_date_range(account, from_date, to_date=None):
    query = []
    if to_date is None:
        query.append({'$match': {'HTTP_REFERER_WEBSITE':account,'request_date':{'$gte':from_date}}})
    else:
        query.append({'$match': {'HTTP_REFERER_WEBSITE':account, 'request_date':{'$gte':from_date, '$lte':to_date}}})
    query.append({'$group' : {'_id':'$HTTP_REFERER_WEBSITE','total':{'$sum':1}}})
    db_result = db.request_detail.aggregate(query)
    accounts = {}
    for account in db_result['result']:
        accounts[account['_id']]=account['total']
    return accounts

def accounts_by_date(date_filter=''):
    date_filters = {
'today': {'$gte':datetime.datetime.fromtimestamp(time.time()-24*60*60), '$lte':datetime.datetime.fromtimestamp(time.time(), None)},
'yesterday' : {'$gte':datetime.datetime.fromtimestamp(time.time()-48*60*60),'$lte':datetime.datetime.fromtimestamp(time.time()-24*60*60)},
'month' : {'$gte':datetime.datetime.fromtimestamp(time.time()-30*24*60*60),'$lte':datetime.datetime.fromtimestamp(time.time(), None)}
    }
    query = []
    if date_filter is not None and date_filter in date_filters.keys():
        print date_filter, 'filter applied'
        query.append({'$match' : {'request_date':date_filters[date_filter]}})
    query.append({'$group' : {'_id':'$HTTP_REFERER_WEBSITE','total':{'$sum':1}}})
    db_result = db.request_detail.aggregate(query)
    accounts = {}
    for account in db_result['result']:
        accounts[account['_id']]=account['total']
    return accounts

