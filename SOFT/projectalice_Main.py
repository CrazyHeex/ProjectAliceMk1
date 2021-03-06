#########################################
#Project Alice
#########################################
#Author: Zhengxing Yang
#Description: V-REP simulation w/ 360 controller
#create date: 9/11/2015
#########################################

try:
    import vrep
except:
    print ('no python V-REP API support file found')

try:
    import ctypes
    import sys
    import time
    from operator import itemgetter, attrgetter
    from itertools import count, starmap
except:
    print ('something happend ;p check import')


try:
    import xinput

except:
    print ('no xinput found')


print ('Program started')
vrep.simxFinish(-1)
clientID=vrep.simxStart('127.0.0.1',19997,True,True,5000,5)
if clientID!=-1:
    print ('Connected!')



    # start the simulation:
    vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)
    vrep.simxAddStatusbarMessage(clientID,'Hello V-REP! This is a connection test!',vrep.simx_opmode_oneshot)
    #vrep.simxCreateDummy(clientID,0.3,None,vrep.simx_opmode_oneshot)
    # Now step a few times:
    print vrep.simxGetObjectGroupData(clientID,vrep.sim_object_dummy_type,0,vrep.simx_opmode_oneshot_wait)
    k = 0

    [res,objs]=vrep.simxGetObjects(clientID,vrep.sim_handle_all,vrep.simx_opmode_oneshot_wait)
    [errl,nHandlel] = vrep.simxGetObjectHandle(clientID, 'rik0', vrep.simx_opmode_oneshot_wait)
    [errr,nHandler] = vrep.simxGetObjectHandle(clientID, 'lik0', vrep.simx_opmode_oneshot_wait)


    joysticks = xinput.XInputJoystick.enumerate_devices()
    device_numbers = list(map(xinput.attrgetter('device_number'), joysticks))



    print('found %d devices: %s' % (len(joysticks), device_numbers))
    if not joysticks:
        sys.exit(0)
    j = joysticks[0]
    print('using %d' % j.device_number)
    @j.event
    def on_button(button, pressed):
        print button
        pos=[0,0,0]

        if button == 9:
            [nn,pp]=vrep.simxGetObjectPosition (clientID,nHandlel,-1,vrep.simx_opmode_streaming)
            pos[0]=pp[0]
            pos[1]=pp[1]
            pos[2]=pp[2]+0.002
            vrep.simxSetObjectPosition(clientID, nHandlel, -1, pos, vrep.simx_opmode_oneshot_wait)
        elif button == 10:
            [nn,pp]=vrep.simxGetObjectPosition (clientID,nHandler,-1,vrep.simx_opmode_streaming)
            pos[0]=pp[0]
            pos[1]=pp[1]
            pos[2]=pp[2]+0.002
            vrep.simxSetObjectPosition(clientID, nHandler, -1, pos, vrep.simx_opmode_oneshot_wait)
        else:
            vrep.simxStopSimulation(clientID,vrep.simx_opmode_oneshot_wait)
            vrep.simxFinish(clientID)


    @j.event
    def on_axis(axis, value):
        left_speed = 0
        right_speed = 0
        pos=[0,0,0]
        if axis == "l_thumb_x":

            [nn,pp]=vrep.simxGetObjectPosition (clientID,nHandlel,-1,vrep.simx_opmode_streaming)
            pos[0]=pp[0]+value/50
            pos[1]=pp[1]
            pos[2]=pp[2]
            vrep.simxSetObjectPosition(clientID, nHandlel, -1, pos, vrep.simx_opmode_oneshot_wait)
        if axis == "l_thumb_y":
            [nn,pp]=vrep.simxGetObjectPosition (clientID,nHandlel,-1,vrep.simx_opmode_streaming)
            pos[0]=pp[0]
            pos[1]=pp[1]+value/50
            pos[2]=pp[2]
            vrep.simxSetObjectPosition(clientID, nHandlel, -1, pos, vrep.simx_opmode_oneshot_wait)
        if axis == "left_trigger":
            [nn,pp]=vrep.simxGetObjectPosition (clientID,nHandlel,-1,vrep.simx_opmode_streaming)
            pos[0]=pp[0]
            pos[1]=pp[1]
            pos[2]=pp[2]-value/50
            vrep.simxSetObjectPosition(clientID, nHandlel, -1, pos, vrep.simx_opmode_oneshot_wait)
        if axis == "r_thumb_x":
            [nn,pp]=vrep.simxGetObjectPosition (clientID,nHandler,-1,vrep.simx_opmode_streaming)
            pos[0]=pp[0]+value/50
            pos[1]=pp[1]
            pos[2]=pp[2]
            vrep.simxSetObjectPosition(clientID, nHandler, -1, pos, vrep.simx_opmode_oneshot_wait)
        if axis == "r_thumb_y":
            [nn,pp]=vrep.simxGetObjectPosition (clientID,nHandler,-1,vrep.simx_opmode_streaming)
            pos[0]=pp[0]
            pos[1]=pp[1]+value/50
            pos[2]=pp[2]
            vrep.simxSetObjectPosition(clientID, nHandler, -1, pos, vrep.simx_opmode_oneshot_wait)
        if axis == "right_trigger":
            [nn,pp]=vrep.simxGetObjectPosition (clientID,nHandler,-1,vrep.simx_opmode_streaming)
            pos[0]=pp[0]
            pos[1]=pp[1]
            pos[2]=pp[2]-value/50
            vrep.simxSetObjectPosition(clientID, nHandler, -1, pos, vrep.simx_opmode_oneshot_wait)







    while True:
        j.dispatch_events()
        time.sleep(.01)



else:
    print ('Failed connecting to remote API server')
print ('Program ended')
