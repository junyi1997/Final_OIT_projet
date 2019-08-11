"""
使用於Python3
使用此程式前，必須先安裝好RPi.GPIO（記得在樹莓派灌），如果沒灌好一定會有錯。
想安裝RPi.GPIO，且如果你有pip的話，可打下方指令完成安裝
pip install RPi.GPIO
""" 

import time
import RPi.GPIO as GPIO

class StepMotor(object):
    """
    StepMotor 此類別為簡單操作兩相4線控之步進馬達用
    """

    forward_seq = ['1100', '0110', '0011', '1001']
    """
    forward_seq 為步進馬達正轉之輸出順序
    """

    reverse_seq = ['1001', '0011', '0110', '1100']
    """
    reverse_seq 為步進馬達正轉之輸出順序
    """

    a1_pin = 17 #A
    a2_pin = 27 #B
    b1_pin = 23 #/A
    b2_pin = 24 #/B
    """
    上述為樹莓派pin腳定義
    """
    all_pin = [a1_pin,
        a2_pin,
        b1_pin,
        b2_pin]
    """
    上述為樹莓派pin腳定義之陣列
    """

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(StepMotor.all_pin, GPIO.OUT)
        pass
    
    def initialize(self):
        self.set_step('0000')

    def forward(self, delay, steps):
        """正轉用 Function
        
        參數:
        ===
            delay(float) : 延遲時間(sec)
            （數值盡量在50/1000~4/1000，是不同步進馬達規格而定）
            steps(int)   : 期望走的步數
        舉例:
        ===
            forward(10/1000,100)
        """
        steps /= 4
        self._ward(delay,int(steps),StepMotor.forward_seq)
    def backward(self,delay, steps):
        """反轉用 Function
        
        參數:
        ===
            delay(float) : 延遲時間(sec)
            （數值盡量在50/1000~4/1000，是不同步進馬達規格而定）
            steps(int)   : 期望走的步數
        舉例:
        ===
            forward(10/1000,100)
        """
        steps /= 4
        self._ward(delay,int(steps),StepMotor.reverse_seq)
    
    def set_step(self, step):
        for i in range(4):
            GPIO.output(StepMotor.all_pin[i], int(step[i]))
            pass
        
    def _ward(self, delay, steps, seq):
        for _ in range(steps):
            for step in seq:
                self.set_step(step)
                time.sleep(delay)
    def clean(self):
        GPIO.cleanup()

"""
以下為測試程式，直接執行該程式即可進行測試。
"""

class Test_StepMotor(StepMotor):

    

    def __init__(self):
        self.test_count = [0,0,0,0]
        pass

    def set_step(self, step,seq):
        for i in range(4):
            if step == seq[i]:
                self.test_count[i] += 1

    def _ward(self, delay, steps, seq):
        for _ in range(steps):
            for step in seq:
                self.set_step(step,seq)
                time.sleep(delay)
        
    def test_step_info(self):
        sum = 0
        for i in range(len(self.test_count)):
            sum += self.test_count[i]

        # print(seq.__name__," " , seq , end="\n")
        # print(self.test_count, end="\n")
        # print("總共走 ", sum , " 步")
        return sum

import unittest
class TestStepMotorMethods(unittest.TestCase):

    def test_forward(self):
        test_StepMotor = Test_StepMotor()
        test_StepMotor.forward(1/1000,100)
        self.assertEqual(test_StepMotor.test_step_info(),100)

    def test_backward(self):
        test_StepMotor2 = Test_StepMotor()
        test_StepMotor2.backward(1/1000,200)
        self.assertEqual(test_StepMotor2.test_step_info(),200)
def main():
    unittest.main()
    pass

if __name__ == '__main__':
    main()