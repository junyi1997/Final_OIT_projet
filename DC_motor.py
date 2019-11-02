import RPi.GPIO as GPIO
import time
class motor:
   def __init__(self):
      self.ou1_pin=31#馬達IN1
      self.ou2_pin=33#馬達IN2
      self.ou3_pin=35#馬達IN3
      self.ou4_pin=37#馬達IN4
      self.in1_pin=36#一般桶
      self.in2_pin=38#塑膠桶
      self.in3_pin=40#紙類桶

      self.ouZ1_pin=32#DC馬達 pin1
      self.ouZ2_pin=29#DC馬達 pin2

      self.a=0
      self.b=0
      self.c=0
      self.w=0

      GPIO.setwarnings(False)
      GPIO.setmode(GPIO.BOARD)
      GPIO.setup(self.in1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
      GPIO.setup(self.in2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
      GPIO.setup(self.in3_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

      GPIO.setup(self.ou1_pin, GPIO.OUT)
      GPIO.setup(self.ou2_pin, GPIO.OUT)
      GPIO.setup(self.ou3_pin, GPIO.OUT)
      GPIO.setup(self.ou4_pin, GPIO.OUT)
      GPIO.setup(self.ouZ1_pin, GPIO.OUT)
      GPIO.setup(self.ouZ2_pin, GPIO.OUT)

   def my_DC(self):
      print("蓋子開啟")
      GPIO.output(self.ouZ2_pin,GPIO.HIGH)
      GPIO.output(self.ouZ1_pin,GPIO.LOW)
      time.sleep(1)
      GPIO.output(self.ouZ1_pin,GPIO.LOW)
      GPIO.output(self.ouZ2_pin,GPIO.LOW)
      print("蓋子到定點1")
      time.sleep(2)
      print("蓋子關閉")
      GPIO.output(self.ouZ2_pin,GPIO.LOW)
      GPIO.output(self.ouZ1_pin,GPIO.HIGH)
      time.sleep(1)
      GPIO.output(self.ouZ1_pin,GPIO.LOW)
      GPIO.output(self.ouZ2_pin,GPIO.LOW)
      print("蓋子到定點1")
      #self.motor_1()

   def motor_1(self):
      print("進入桶1")
      while True:
         self.a=GPIO.input(self.in1_pin)
         if self.a ==1:
               print("SW1啟動")
               GPIO.output(self.ou1_pin,GPIO.HIGH)
               GPIO.output(self.ou2_pin,GPIO.HIGH)
               GPIO.output(self.ou3_pin,GPIO.LOW)
               GPIO.output(self.ou4_pin,GPIO.LOW)
               time.sleep(1)
               #self.my_main()
               return
         elif self.a==0:
               GPIO.output(self.ou1_pin,GPIO.HIGH)
               GPIO.output(self.ou2_pin,GPIO.LOW)
               GPIO.output(self.ou3_pin,GPIO.LOW)
               GPIO.output(self.ou4_pin,GPIO.HIGH)
               

   def motor_2(self):
      print("進入桶2")
      while True:
         self.b=GPIO.input(self.in2_pin)
         if self.b ==1:
               print("SW2啟動")
               GPIO.output(self.ou1_pin,GPIO.LOW)
               GPIO.output(self.ou2_pin,GPIO.LOW)
               GPIO.output(self.ou3_pin,GPIO.HIGH)
               GPIO.output(self.ou4_pin,GPIO.HIGH)
               time.sleep(1)
               #self.my_DC()
               return
         elif self.b==0:
               GPIO.output(self.ou1_pin,GPIO.LOW)
               GPIO.output(self.ou2_pin,GPIO.HIGH)
               GPIO.output(self.ou3_pin,GPIO.HIGH)
               GPIO.output(self.ou4_pin,GPIO.LOW)
      
   def motor_3(self):
      print("進入桶3")
      while True:
         self.c=GPIO.input(self.in3_pin)
         if self.c ==1:
               print("SW3啟動")
               GPIO.output(self.ou1_pin,GPIO.LOW)
               GPIO.output(self.ou2_pin,GPIO.LOW)
               GPIO.output(self.ou3_pin,GPIO.HIGH)
               GPIO.output(self.ou4_pin,GPIO.HIGH)
               time.sleep(1)
               #self.my_DC()
               return
         elif self.c ==0:
               GPIO.output(self.ou1_pin,GPIO.LOW)
               GPIO.output(self.ou2_pin,GPIO.HIGH)
               GPIO.output(self.ou3_pin,GPIO.HIGH)
               GPIO.output(self.ou4_pin,GPIO.LOW)
               
      
   def my_main(self):
      self.w=eval(input("第幾個分類桶"))
      print("w=",self.w)
      if self.w == 1:
         print("選擇桶1")
         self.my_DC()
      elif self.w == 2:
         print("選擇桶2")
         self.motor_2()
      elif self.w == 3:
         print("選擇桶3")
         self.motor_3()
      elif self.w == 4:
         print("CCC")
         self.my_DC()
         
   def test(self):
      while True:
         self.a=GPIO.input(self.in1_pin)
         print("a=",self.a)
         self.b=GPIO.input(self.in2_pin)
         print("b=",self.b)
         self.c=GPIO.input(self.in3_pin)
         print("c=",self.c)
         time.sleep(1)

if __name__=='__main__':
    print("程式開始")
    M=motor()
    M.my_main()
    #M.my_DC()
