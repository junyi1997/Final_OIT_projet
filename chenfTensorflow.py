
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
def wait(imgpath):
    print("Wait....")
    sort_trash(imgpath)
def sort_trash(imgpath):
    GUI_IN=8#馬達IN1
    GUI_紙類=26#馬達IN2
    GUI_塑膠=24#馬達IN3
    GUI_鐵=13#馬達IN4
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GUI_IN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(GUI_紙類, GPIO.OUT)
    GPIO.setup(GUI_塑膠, GPIO.OUT)
    GPIO.setup(GUI_鐵, GPIO.OUT)
    camera = Camera()
    m=motor()
	# database = Database()
    classifier = Classifier(os.path.abspath('Tf_classifier/trained_graph.pb'), os.path.abspath('Tf_classifier/output_labels.txt'))

	# statusThread = ui.start_status_shower_thread()

    while True:
        
        GUI_a=GPIO.input(GUI_IN)
        print("self.GUI_a",GUI_a)
        print("等待回應")
		# wait for camera to detect motion, then sleep for a bit to
		# let the object settle down
        if GUI_a ==1:
            print ("waiting for motion...")
            GPIO.output(GUI_塑膠,GPIO.LOW)
            GPIO.output(GUI_紙類,GPIO.LOW)
            GPIO.output(GUI_鐵,GPIO.LOW)
            print("self.GUI_塑膠1",GPIO.input(GUI_塑膠))
            print("self.GUI_紙類1",GPIO.input(GUI_紙類))
            print("self.GUI_鐵1",GPIO.input(GUI_鐵))
            C=motiondetector.waitForMotionDetection(camera.getPiCamera())
            time.sleep(0.5) # Lets object settle down, TODO maybe remove
            print("C=",C)
            
            if C != "close":   
                print ("detected motion")
                
        		# take a photo and classify it
                camera.takePhoto(imgpath)
                labels = classifier.get_image_labels(imgpath)
                print (labels)
                selectedLabel = brain.getRecyclingLabel(labels)
                is_trash = selectedLabel == None
        
                if is_trash:
                    print("It's trash.")
                    m.my_DC()
                    time.sleep(1)
                else:
                    print("It's recyclable.")
                    if str(selectedLabel).find('plastic') != -1 or str(selectedLabel).find('glass') != -1:
                        print("It's plastic or glass.")
                        GPIO.output(GUI_塑膠,GPIO.HIGH)
                        print("self.GUI_塑膠1",GPIO.input(GUI_塑膠))
                        print("self.GUI_紙類1",GPIO.input(GUI_紙類))
                        print("self.GUI_鐵1",GPIO.input(GUI_鐵))
                        time.sleep(1)
                        GPIO.output(GUI_塑膠,GPIO.LOW)
                        print("self.GUI_塑膠1",GPIO.input(GUI_塑膠))
                        print("self.GUI_紙類1",GPIO.input(GUI_紙類))
                        print("self.GUI_鐵1",GPIO.input(GUI_鐵))
                        m.motor_2()
                        time.sleep(2)
                        m.my_DC()
                        time.sleep(1)
                        m.motor_1()
                        time.sleep(1)
                    elif str(selectedLabel).find('paper') != -1 or str(selectedLabel).find('cardboard') != -1:
                        print("It's paper.")
                        GPIO.output(GUI_紙類,GPIO.HIGH)
                        print("self.GUI_塑膠1",GPIO.input(GUI_塑膠))
                        print("self.GUI_紙類1",GPIO.input(GUI_紙類))
                        print("self.GUI_鐵1",GPIO.input(GUI_鐵))
                        time.sleep(1)
                        GPIO.output(GUI_紙類,GPIO.LOW)
                        print("self.GUI_塑膠1",GPIO.input(GUI_塑膠))
                        print("self.GUI_紙類1",GPIO.input(GUI_紙類))
                        print("self.GUI_鐵1",GPIO.input(GUI_鐵))
                        m.motor_3()
                        time.sleep(2)
                        m.my_DC()
                        time.sleep(1)
                        m.motor_1()
                        time.sleep(1)
                    elif str(selectedLabel).find('metal') != -1:
                        print("It's metal.")
                        GPIO.output(GUI_鐵,GPIO.HIGH)
                        print("self.GUI_塑膠1",GPIO.input(GUI_塑膠))
                        print("self.GUI_紙類1",GPIO.input(GUI_紙類))
                        print("self.GUI_鐵1",GPIO.input(GUI_鐵))
                        time.sleep(1)
                        GPIO.output(GUI_鐵,GPIO.LOW)
                        print("self.GUI_塑膠1",GPIO.input(GUI_塑膠))
                        print("self.GUI_紙類1",GPIO.input(GUI_紙類))
                        print("self.GUI_鐵1",GPIO.input(GUI_鐵))
                        m.my_DC()
                        time.sleep(1)
            else:
                time.sleep(5)
def main():
	sort_trash('ImageProcessing/img/classificationImage.jpg')

if __name__ == '__main__':
    main()