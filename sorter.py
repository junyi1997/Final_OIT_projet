# import servo
# import ui
from ImageProcessing.camera import Camera
from vision import Classifier
from ImageProcessing import motiondetector
import time 
import brain
# from databasehelper import Database
import os
from DC_motor import motor
import RPi.GPIO as GPIO

class Tensorflow:
	def __init__(self):
		self.i=0
		self.camera = Camera()
		self.m=motor()
		self.GUI_IN=8#馬達IN1
		self.GUI_紙類=26#馬達IN2
		self.GUI_塑膠=24#馬達IN3
		self.GUI_鐵=22#馬達IN4
		self.GUI_a=0
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.GUI_IN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		GPIO.setup(self.GUI_紙類, GPIO.OUT)
		GPIO.setup(self.GUI_塑膠, GPIO.OUT)
		GPIO.setup(self.GUI_鐵, GPIO.OUT)

	def sort_trash(self,imgpath):
		# database = Database()
		self.classifier = Classifier(os.path.abspath('Tf_classifier/trained_graph.pb'), os.path.abspath('Tf_classifier/output_labels.txt'))
		self.run(imgpath)
		# statusThread = ui.start_status_shower_thread()
	def run_now(self,imgpath):
		GPIO.output(self.GUI_紙類,GPIO.LOW)
		GPIO.output(self.GUI_塑膠,GPIO.LOW)
		GPIO.output(self.GUI_鐵, GPIO.LOW)
		# wait for camera to detect motion, then sleep for a bit to
		# let the object settle down
		print ("waiting for motion...")
		self.GUI_a=GPIO.input(self.GUI_IN)
		print("self.GUI_a",self.GUI_a)
		print("等待回應")
		if self.GUI_a ==1:
			motiondetector.waitForMotionDetection(self.camera.getPiCamera())
			time.sleep(0.5) # Lets object settle down, TODO maybe remove
			print ("detected motion")
			# take a photo and classify it
			'''
			if self.i<=3:
				self.i+=1
				c="test{:}.png".format(self.i)
				self.camera.takePhoto(imgpath)
				self.camera.takePhoto(c)
			'''
			labels = self.classifier.get_image_labels(imgpath)
			print (labels)
			selectedLabel = brain.getRecyclingLabel(labels)
			is_trash = selectedLabel == None

			if is_trash:
				print("It's trash.")
				self.m.my_DC()
				time.sleep(1)
			else:
				print("It's recyclable.")
				if str(selectedLabel).find('plastic') != -1 or str(selectedLabel).find('glass') != -1:
					print("It's plastic or glass.")
					GPIO.output(self.GUI_塑膠,GPIO.HIGH)
					print("self.GUI_塑膠",GPIO.input(self.GUI_塑膠))
					time.sleep(1)
					GPIO.output(self.GUI_塑膠,GPIO.LOW)
					self.m.motor_2()
					time.sleep(2)
					self.m.my_DC()
					time.sleep(1)
					self.m.motor_1()
					time.sleep(1)
				elif str(selectedLabel).find('paper') != -1 or str(selectedLabel).find('cardboard') != -1:
					print("It's paper.")
					GPIO.output(self.GUI_紙類,GPIO.HIGH)
					print("self.GUI_紙類",GPIO.input(self.GUI_紙類))
					time.sleep(1)
					GPIO.output(self.GUI_紙類,GPIO.LOW)
					self.m.motor_3()
					time.sleep(2)
					self.m.my_DC()
					time.sleep(1)
					self.m.motor_1()
					time.sleep(1)	
		else:
			self.run(imgpath)
	def run(self,imgpath):
		while True:
			self.GUI_a=GPIO.input(self.GUI_IN)
			print("self.GUI_a",self.GUI_a)
			print("等待回應")
			if self.GUI_a ==1:
				self.run_now(imgpath)
			else:
				print("Wait....")
					
	def main(self):
		self.sort_trash('ImageProcessing/img/classificationImage.jpg')

if __name__ == '__main__':
	T=Tensorflow()
	T.main()