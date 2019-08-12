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
        },
    'user002': {
        'date_of_birth': 'December 9, 1995',
        'full_name': 'Tama Isono'
        }
    })

# databaseにデータを追加する
users_ref.child('user003').set({
    'date_of_birth': 'Aug 23, 1980',
    'full_name': 'Masuo Isono'
    })

##データを取得する
print(users_ref.get())

##データを更新する
updates = {}
updates['/user001/full_name'] = 'AAA'
users_ref.update(updates)