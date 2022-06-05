# main.py -- put your code here!
from pyb import USB_VCP, Timer, UART, ADC, Pin, ExtInt
import pyb
import time

# Virtual UART Port
ser = pyb.USB_VCP(0)
ser2 = UART(6, 38400)
dc_state1 = [0]
test_state = 0
servo_state = [0]


                #PWM        #Timer   #CH    #State
PPPins = { 0: { 4: 'X1',    5: 5,    6: 1,  7: 0}, 
           1: { 4: 'X2',    5: 2,    6: 2,  7: 0},
           2: { 4: 'X3',    5: 9,    6: 1,  7: 0},
           3: { 4: 'X4',    5: 2,    6: 4,  7: 0}
}

#   0: Top
#   1: Bot
#   2: Pincherxxxxxxxxxxxzzzzzzzz
#   3: Spect
#   4: Elephant

                        #PWM      #DIR      #Timer  #CH  
mainStepperPins = { 0: {4: 'Y8',  5: 'Y7',  6: 12,  7: 2, },
                    1: {4: 'X10', 5: 'X9',  6: 4,   7: 2, },
                    2: {4: 'Y4',  5: 'Y3',  6: 4,   7: 4, },
                    3: {4: 'Y6',  5: 'Y5',  6: 1,   7: 1, },
                    4: {4: 'Y9',  5: 'Y10', 6: 2,   7: 3, },
}

servoPins = { 0: { 4: pyb.Servo(4) }
}

solenoidPin = { 0: { 4: 'X7', 5: 1 } }


def toggleServo(servo_dict, state):
    pyb.LED(2).on()
    time.sleep(.4)
    if(state[0] == 0):
        servo_dict[4].angle(45)
        state[0] = 1
    else:
        servo_dict[4].angle(-45)
        state[0] = 0

def togglePump(pump_dict):
    pyb.LED(4).on()
    Timer(pump_dict[5], freq=1250).channel(pump_dict[6], Timer.PWM, pin=Pin(pump_dict[4])).pulse_width_percent(100)
    time.sleep(5/1000)
    pyb.LED(4).off()
    Timer(pump_dict[5], freq=1250).channel(pump_dict[6], Timer.PWM, pin=Pin(pump_dict[4])).pulse_width_percent(0)

def stepperMove(stepper_dict, state):
    
    if state == 1:
        pyb.LED(3).on()
        Pin(stepper_dict[5], Pin.OUT_PP).high()
        Timer(stepper_dict[6], freq=1250).channel(stepper_dict[7], Timer.PWM, pin=Pin(stepper_dict[4])).pulse_width_percent(25)
        time.sleep(5/1000)
        Timer(stepper_dict[6], freq=1250).channel(stepper_dict[7], Timer.PWM, pin=Pin(stepper_dict[4])).pulse_width_percent(0)
        pyb.LED(3).off()
    else:
        pyb.LED(2).on()
        Pin(stepper_dict[5], Pin.OUT_PP).low()
        Timer(stepper_dict[6], freq=1250).channel(stepper_dict[7], Timer.PWM, pin=Pin(stepper_dict[4])).pulse_width_percent(25)
        time.sleep(5/1000)
        Timer(stepper_dict[6], freq=1250).channel(stepper_dict[7], Timer.PWM, pin=Pin(stepper_dict[4])).pulse_width_percent(0)
        pyb.LED(2).off()

def toggleSolenoid(sol_dict):
    time.sleep(.4)
    if sol_dict[5] == 0:
        Pin(sol_dict[4], Pin.OUT_PP).high()
        sol_dict[5] = 1
        print("Solenoid High")
    else:
        Pin(sol_dict[4], Pin.OUT_PP).low()
        sol_dict[5] = 0
        print("Solenoid Low")

def togglePump2(sol_dict):
    time.sleep(.4)
    if sol_dict[7] == 0:
        Pin(sol_dict[4], Pin.OUT_PP).high()
        sol_dict[7] = 1
        #print("Solenoid High")
    else:
        Pin(sol_dict[4], Pin.OUT_PP).low()
        sol_dict[7] = 0
        #print("Solenoid Low")


	     
                 

   
if __name__ == "__main__":

    

    but_pump_1 = Pin('Y11', Pin.IN, Pin.PULL_NONE) 
    but_pump_2 = Pin('X20', Pin.IN, Pin.PULL_NONE) #
    but_pump_3 = Pin('X19', Pin.IN, Pin.PULL_NONE) #
    but_pump_4 = Pin('X22', Pin.IN, Pin.PULL_NONE) #
    but_pump_5 = Pin('X11', Pin.IN, Pin.PULL_NONE) #
    but_pump_6 = Pin('X12', Pin.IN, Pin.PULL_NONE) #
    but_pump_7 = Pin('X18', Pin.IN, Pin.PULL_NONE) #
    but_pump_8 = Pin('X21', Pin.IN, Pin.PULL_NONE) #
    but_pump_9 = Pin('Y12', Pin.IN, Pin.PULL_NONE) #
    but_pump_10 = Pin('X4', Pin.IN, Pin.PULL_NONE) 
    but_pump_11 = Pin('X5', Pin.IN, Pin.PULL_NONE) 
    but_pump_12 = Pin('X6', Pin.IN, Pin.PULL_NONE) 

    #logicLevelOE = Pin('X17', Pin.OUT_PP).high()
    # Pump1B = Pin('X4', Pin.OUT_PP).low()
    # Pump2B = Pin('X5', Pin.OUT_PP).low()
    # Loop button checks
    
    while True:

        if but_pump_1.value(): #BUTTON RIGHT3
            test_state = 1
            stepperMove(mainStepperPins[0], test_state)
            print("Top Gear CW...")
        if but_pump_2.value(): #BUTTON LEFT3
            test_state = 0
            stepperMove(mainStepperPins[0], test_state)
            print("Top Gear CCW...")
        elif but_pump_3.value(): #BUTTON LEFT2
            test_state = 1
            stepperMove(mainStepperPins[1], test_state)
            print("Bot Gear CW..")
        if but_pump_4.value(): #BUTTON RIGHT4
            test_state = 0
            stepperMove(mainStepperPins[1], test_state)
            print("Bot Gear CCW..")
        elif but_pump_5.value(): #BUTTON LEFT4
            test_state = 0
            stepperMove(mainStepperPins[2], test_state)
            print("Pinching Assembly CW")
        if but_pump_6.value(): #BUTTON RIGHT1
            test_state = 1
            stepperMove(mainStepperPins[2], test_state)
            print("Pinching Assembly CCW")
        elif but_pump_7.value(): #BUTTON RIGHT2
            test_state = 1
            stepperMove(mainStepperPins[3], test_state)
            print("Spectroscopy moving CW...")
        elif but_pump_8.value(): #BUTTON RIGHT2
            test_state = 0
            stepperMove(mainStepperPins[3], test_state)
            print("Spectroscopy moving CCW...")
        if but_pump_9.value(): # BUTTON LEFT1
            togglePump(PPPins[0])
            print("Pump 1 going...")
        if but_pump_10.value(): # BUTTON RIGHT5
            togglePump(PPPins[1])
            print("Pump 2 going...")
        if but_pump_11.value(): # BUTTON RIGHT5
            togglePump(PPPins[2])
            print("Pump 3 going...") 
        if but_pump_12.value(): # BUTTON RIGHT5
            toggleSolenoid(solenoidPin[0])
            


        
        #toggleServo(servoPins[0], servo_state)
        #time.sleep(2)

        # t_end = time.time() + 1

        # while time.time() < t_end:
        #     test_state = 1
        #     stepperMove(mainStepperPins[3], test_state)
        
        # time.sleep(1)

        # t_end = time.time() + 1

        # while time.time() < t_end:
        #     test_state = 0
        #     stepperMove(mainStepperPins[3], test_state)
        
        # time.sleep(1)
        # t_end = time.time() + 2

        # while time.time() < t_end:
        #     test_state = 1
        #     stepperMove(mainStepperPins[3], test_state)
        
        # time.sleep(1)

        # t_end = time.time() + 2
        # while time.time() < t_end:
        #     test_state = 0
        #     stepperMove(mainStepperPins[3], test_state)

        # time.sleep(1)

        # t_end = time.time() + 5

        # while time.time() < t_end:
        #     test_state = 0
        #     stepperMove(mainStepperPins[2], test_state)
        
        # time.sleep(1)
        
        # t_end = time.time() + 5
        # while time.time() < t_end:
        #     test_state = 0
        #     stepperMove(mainStepperPins[2], test_state)
        
        # time.sleep(1)
        
        # t_end = time.time() + 2
        # while time.time() < t_end:
        #     test_state = 1
        #     stepperMove(mainStepperPins[1], test_state)

        # time.sleep(1)

        # t_end = time.time() + 2
        # while time.time() < t_end:
        #     test_state = 0
        #     stepperMove(mainStepperPins[1], test_state)
        
        # time.sleep(1)

        # t_end = time.time() + 2
        # while time.time() < t_end:
        #     test_state = 1
        #     stepperMove(mainStepperPins[0], test_state)
        
        # time.sleep(1)

        # t_end = time.time() + 2
        # while time.time() < t_end:
        #     test_state = 0
        #     stepperMove(mainStepperPins[0], test_state)
        
        # time.sleep(1)
