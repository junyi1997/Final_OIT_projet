#Ref：https://qiita.com/sai-san/items/24dbee74c5744033c330

# -*- coding: utf-8 -*-
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('./serviceAccount.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://seaturtle-105103308.firebaseio.com/',
    'databaseAuthVariableOverride': {
        'uid': 'seaturtle-105103308'
    }
})

##databaseに初期データを追加する
users_ref = db.reference('/users')

users_ref.set({
    'user001': {
        'date_of_birth': 'June 23, 1984',
        'full_name': 'Sazae Isono'
        }
    })

# databaseにデータを追加する
users_ref.child('user003').set({
    'date_of_birth': 'Aug 23, 1980',
    'full_name': 'Masuo Isono'
    })
users_ref = db.reference('/QR')

users_ref.set({
        '第一次': {
        'Scoin': '100',
        'name': '塑膠類',
        'sum1': '1',
        'time': '2019-06-14 10:29:16'
        },
        '第二次': {
        'Scoin': '1',
        'name': '紙類',
        'sum1': '2',
        'time': '2019-08-14 10:29:16'
        }
})
##データを取得する
users_ref = db.reference('/users')
print("users")
print(users_ref.get())
print(len(users_ref.get()))
users_ref = db.reference('/fb')
print("fb")
print(users_ref.get())
print(len(users_ref.get()))
##データを更新する
updates = {}
updates['/user001/full_name'] = 'AAA'
users_ref.update(updates)