# -*- coding: utf-8 -*-
from google.cloud import firebase

key="PCaUi0xj4e9v1tZ15YKuDalQa1OZOOauNlRqzDnA"

authentication = firebase.FirebaseAuthentication(key, 'q5896799@gmail.com')#這邊是要填入身分驗證，需要資料庫密鑰和google資料庫擁有者帳號

firebase.authentication = authentication #身分驗證

user = authentication.get_user() #獲取使用者資訊

firebase = firebase.FirebaseApplication('https://seaturtle-105103308.firebaseio.com/', authentication=authentication) #登入資料庫，網址在資料庫頁面能找到

firebase.post("/ABC","6677")