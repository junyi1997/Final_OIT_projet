#Ref：https://qiita.com/sai-san/items/24dbee74c5744033c330

# -*- coding: utf-8 -*-
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
#import types
#
#def dict_get(dict, objkey, default):
#  tmp = dict
#  for k,v in tmp.items():
#    if k == objkey:
#      return v
#    else:
#      if type(v) is types.DictType:
#        ret = dict_get(v, objkey, default)
#        if ret is not default:
#          return ret
#  return default

cred = credentials.Certificate('./serviceAccount.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://seaturtle-105103308.firebaseio.com/',
    'databaseAuthVariableOverride': {
        'uid': 'seaturtle-105103308'
    }
})

##databaseに初期データを追加する


# databaseにデータを追加する

#users_ref = db.reference('/QR')
#
#users_ref.set({
#        '第01次': {
#        'SCoin': '100',
#        'name': '塑膠類',
#        'sum1': '1',
#        'time': '2019-06-14 10:29:16'
#        },
#        '第02次': {
#        'SCoin': '1',
#        'name': '紙類',
#        'sum1': '2',
#        'time': '2019-08-14 10:29:16'
#        }
#})
#users_ref.child('第03次').set({
#'Scoin': '6',
#'name': '鐵類',
#'sum1': '3',
#'time': '2019-08-16 10:29:16'
#})
#users_ref = db.reference('/fb')
#
#users_ref.set({
#        '第01次': {
#        'SCoin': '100',
#        'name': '塑膠類',
#        'sum1': '1',
#        'time': '2019-06-14 10:29:16'
#        },
#        '第02次': {
#        'SCoin': '1',
#        'name': '紙類',
#        'sum1': '2',
#        'time': '2019-08-14 10:29:16'
#        }
#})
#users_ref = db.reference('/Google')
#
#users_ref.set({
#        '第01次': {
#        'SCoin': '100',
#        'name': '塑膠類',
#        'sum1': '1',
#        'time': '2019-06-14 10:29:16'
#        },
#        '第02次': {
#        'SCoin': '1',
#        'name': '紙類',
#        'sum1': '2',
#        'time': '2019-08-14 10:29:16'
#        }
#})

##データを取得する
users_ref = db.reference('/Google')
print("Google")
c=users_ref.get()
print(c)
sumi_3_1=len(users_ref.get())
print(sumi_3_1)
users_ref = db.reference('/QR')
print("QR")
a=users_ref.get()
print(a)
print(len(users_ref.get()))
users_ref = db.reference('/fb')
print("fb")
b=users_ref.get()
print(b)
print(len(users_ref.get()))
money=0
tit='QR'
#Get Collection

saveK1 = []
saveK2 = []
saveK3 = []
saveK4 = []

money=0
tit='Google'
#Get Collection
sumi_1=0
#Get Collection
over=1 
i=0
while over:
    if i<10:
        A="{:}/第0{:}次".format(tit,i+1)
    else:
        A="{:}/第{:}次".format(tit,i+1) 
    i=i+1
    ref = db.reference(A)
    print(ref)
    data = ref.get()
    if(data!=None): 
        over=1
        sumi_1=len(data)+1
        print("sumi_1",sumi_1)
        saveK4.append(data['SCoin'])
    else:
        over=0
        for i in range(0,sumi_3_1):
            money+=int(saveK4[i])
            print(saveK4[i]) 
        print(money)      
##データを更新する
#updates = {}
#updates['/user001/full_name'] = 'AAA'
#users_ref.update(updates)

#{'user001': {'date_of_birth': 'June 23, 1984', 'full_name': 'Sazae Isono'}, 'user003': {'date_of_birth': 'Aug 23, 1980', 'full_name': 'Masuo Isono'}}