# -*- coding: utf-8 -*-
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('./serviceAccount.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://seaturtle-105103308.firebaseio.com/'
})


#ref = db.reference('/')
#ref.set({
#        'boxes': 
#            {
#                'box001': {
#                    'color': 'red',
#                    'width': 1,
#                    'height': 3,
#                    'length': 2
#                },
#                'box002': {
#                    'color': 'green',
#                    'width': 1,
#                    'height': 2,
#                    'length': 3
#                },
#                'box003': {
#                    'color': 'yellow',
#                    'width': 3,
#                    'height': 2,
#                    'length': 1
#                }
#            }
#        })


"""
#更新數據
/*-----------ex1------------*/
ref = db.reference('boxes')
box_ref = ref.child('box001')
box_ref.update({
    'color': 'blue'
})
    
/*-----------ex2------------*/
ref = db.reference('boxes')
ref.update({
    'box001/color': 'red',
    'box002/color': 'blue'
})

#產生唯一鍵 "push"
ref = db.reference('boxes')
ref.push({
    'color': 'purple',
    'width': 7,
    'height': 8,
    'length': 6
})
"""
saveK1=[]#紀錄表格數據
saveK2=[]#紀錄表格數據
saveK3=[]#紀錄表格數據
saveK4=[]#紀錄表格數據
tit="Google"
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
#ref = db.reference('boxes/1')
    data = ref.get()
    if(data!=None): 
        over=1
        print(data)
        print("Google長度為：{:}".format(len(data)+1))
#        #val=str(data.keys())
#        for key in data:
#            print("key為：{:}，value為：{:}".format(key,data[key]))#key
        saveK1.append(data['sum1'])
        saveK2.append(data['time'])
        saveK3.append(data['name'])
        saveK4.append(data['SCoin'])
    else:
        over=0  
#        print("saveK1",saveK1)
#        print("saveK2",saveK2)
#        print("saveK3",saveK3)
#        print("saveK4",saveK4)
tit="fb"
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
#ref = db.reference('boxes/1')
    data = ref.get()
    if(data!=None): 
        over=1
        print(data)
        print("fb長度為：{:}".format(len(data)+1))
#        #val=str(data.keys())
#        for key in data:
#            print("key為：{:}，value為：{:}".format(key,data[key]))#key
        saveK1.append(data['sum1'])
        saveK2.append(data['time'])
        saveK3.append(data['name'])
        saveK4.append(data['SCoin'])
    else:
        over=0  
#        print("saveK1",saveK1)
#        print("saveK2",saveK2)
#        print("saveK3",saveK3)
#        print("saveK4",saveK4)
tit="QR"
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
#ref = db.reference('boxes/1')
    data = ref.get()
    if(data!=None): 
        over=1
        print(data)
        print("QR長度為：{:}".format(len(data)+1))
#        #val=str(data.keys())
#        for key in data:
#            print("key為：{:}，value為：{:}".format(key,data[key]))#key
        saveK1.append(data['sum1'])
        saveK2.append(data['time'])
        saveK3.append(data['name'])
        saveK4.append(data['SCoin'])
    else:
        over=0  
#        print("saveK1",saveK1)
#        print("saveK2",saveK2)
#        print("saveK3",saveK3)
#        print("saveK4",saveK4)
        
#        ref=""    
            
            
#print("value為：{:}".format(data[key]))#值
#print(data.keys())
#type(data.keys())
#temp=val.split("'")
#print(temp[1])
#print(data[temp[1]])
#print(val)
#print(ref.get())

#ref = db.reference('boxes')
## Generate a reference to a new location and add some data using push()
#new_box_ref = ref.push({
#    'color': 'purple',
#    'width': 7,
#    'height': 8,
#    'length': 6
#})
## Get the unique key generated by push()
#box_id = new_box_ref.key
#print(box_id)