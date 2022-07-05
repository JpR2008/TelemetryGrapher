
import irsdk
import time


class State:

    ir_connected = False
    last_car_setup_tick = -1

def check_iracing_connected():

    if(state.ir_connected and not (ir.is_initialized and ir.is_connected)):
        state.ir_connected = False
        # reset state variables
        state.last_car_setup_tick
        # shutdown Iracing library
        ir.shutdown()
        print('irsdk disconnected')

    elif(not state.ir_connected and ir.startup() and ir.is_initialized and ir.is_connected):
        state.ir_connected = True
        print('irsdk connected')


timeLog = open("TelFiles\stime.txt", 'w+')
throttleLog = open("TelFiles\sthrottle.txt", 'w+')
brakeLog = open("TelFiles\sbrake.txt", 'w+')
clutchLog = open("TelFiles\clutch.txt", 'w+')
rpmLog = open("TelFiles\eRpm.txt", 'w+')
steeringLog = open("TelFiles\steering.txt", 'w+')
fuelLevelLog = open("TelFiles\Fuellevel.txt", 'w+')
fuelUsePerHourLog = open("TelFiles\FuelUsePerHour", 'w+')

# tires

flTempLog = open("TelFiles\FrontLeftT.txt", 'w+')
flWearLog = open("TelFiles\FrontLeftW.txt", 'w+')

frTempLog = open("TelFiles\FrontRightT.txt", 'w+')
frWearLog = open("TelFiles\FrontRightW.txt", 'w+')

rlTempLog = open("TelFiles\LeftRearT.txt", 'w+')
rlWearLog = open("TelFiles\LeftRearW.txt", 'w+')

rrTempLog = open("TelFiles\RightRearT.txt", 'w+')
rrWearLog = open("TelFiles\RightRearW.txt", 'w+')


def log_data():


    t = round(ir['SessionTime'], 4)
    th = round(ir['Throttle'], 4)
    thRaw = round(ir['ThrottleRaw'], 4)
    b = round(ir['Brake'], 4)
    c = round(ir['Clutch'], 4)
    f = round(ir['FuelLevel'], 4)
    fU = round(ir['FuelUsePerHour'], 4)
    s = round(ir['SteeringWheelAngle'], 4)
    rpm = round(ir['RPM'], 4)



    lfT = round(ir['LFtempCM'], 4)
    lfW = round(ir['LFwearM'], 4)

    rfT = round(ir['RFtempCM'], 4)
    rfW = round(ir['RFwearM'], 4)

    rlT = round(ir['LRtempCM'], 4)
    rlW = round(ir['LRwearM'], 4)

    rrT = round(ir['RRtempCM'], 4)
    rrW = round(ir['RRwearM'], 4)


    timeLog.write('\n' + "Session Time:" + str(t))
    throttleLog.write('\n' + "Throttle:" + str(th))
    brakeLog.write('\n' + "Brake:" + str(b))
    clutchLog.write('\n' + "Clutch:" + str(c))
    rpmLog.write('\n' + "RPM:" + str(rpm))
    fuelLevelLog.write('\n' + "Fuel Level:" + str(f))
    fuelUsePerHourLog.write('\n' + "Fuel Use Per Hour:" + str(fU))
    steeringLog.write('\n' + "Steering:" + str(s))


    flTempLog.write('\n' + "Front Left Temperature:" + str(lfT))
    flWearLog.write('\n' + "Front Left Wear:" + str(lfW))
    
    frTempLog.write('\n' + "Front Right Temperature:" + str(rfT))
    frWearLog.write('\n' + "Front Right Wear:" + str(rfW))

    rlTempLog.write('\n' + "Left Rear Temperature:" + str(rlT))
    rlWearLog.write('\n' + "Left Rear Wear:" + str(rlW))

    rrTempLog.write('\n' + "Right Rear Temperature:" + str(rrT))
    rrWearLog.write('\n' + "Right Rear Wear:" + str(rrW))

def loop():

    ir.freeze_var_buffer_latest()

    log_data()

    print("Looping")

    

if __name__ == '__main__':
    
    ir = irsdk.IRSDK()
    state = State()

    try:

        while True:

            check_iracing_connected()

            if state.ir_connected:
                loop()

            time.sleep(.1)
    except KeyboardInterrupt:

        pass

else:

    print('Failed')
