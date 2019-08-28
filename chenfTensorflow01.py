
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

def sort_trash(imgpath):
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
            print("self.GUI_a",GUI_a)
            print("等待回應")
    		# wait for camera to detect motion, then sleep for a bit to
    		# let the object settle down
            print ("waiting for motion...")
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
                        m.motor_2()
                        time.sleep(2)
                        m.my_DC()
                        time.sleep(1)
                        m.motor_1()
                        time.sleep(1)
                    elif str(selectedLabel).find('paper') != -1 or str(selectedLabel).find('cardboard') != -1:
                        print("It's paper.")
                        m.motor_3()
                        time.sleep(2)
                        m.my_DC()
                        time.sleep(1)
                        m.motor_1()
                        time.sleep(1)
                    elif str(selectedLabel).find('metal') != -1:
                        print("It's metal.")
                        time.sleep(1)
                        m.my_DC()
                        time.sleep(1)
            else:
                time.sleep(5)
def main():
	sort_trash('ImageProcessing/img/classificationImage.jpg')

if __name__ == '__main__':
    i=0
    GUI_a=0
    GUI_IN=8#馬達IN1
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GUI_IN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    main()