#########################################
#Project Alice
#########################################
#Author: Zhengxing Yang
#Description: V-REP simulation w/ leapmotion
#create date: 10/1/2015
#########################################


import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
try:
    import Leap
except:
    print ('no Leap Motion support file found')

try:
    import ctypes
    from operator import itemgetter, attrgetter
    from itertools import count, starmap
except:
    print ('something happend ;p check import')




class SampleListener(Leap.Listener):

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        frame = controller.frame()

        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"
            print "  %s, id %d, position: %s" % (
                handType, hand.id, hand.palm_position)

            normal = hand.palm_normal
            direction = hand.direction



def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)



    vrep.simxFinish(-1)
    clientID=vrep.simxStart('127.0.0.1',19997,True,True,5000,5)


    if clientID!=-1:
        print ('Connected!')

        vrep.simxStartSimulation(clientID,vrep.simx_opmode_oneshot_wait)
        vrep.simxAddStatusbarMessage(clientID,'Hello V-REP! This is a connection test!',vrep.simx_opmode_oneshot)

        print vrep.simxGetObjectGroupData(clientID,vrep.sim_object_dummy_type,0,vrep.simx_opmode_oneshot_wait)

        pos=[0,0,0]
        [res,objs]=vrep.simxGetObjects(clientID,vrep.sim_handle_all,vrep.simx_opmode_oneshot_wait)
        [errl,nHandlel] = vrep.simxGetObjectHandle(clientID, 'rik0', vrep.simx_opmode_oneshot_wait)
        [errr,nHandler] = vrep.simxGetObjectHandle(clientID, 'lik0', vrep.simx_opmode_oneshot_wait)
        pos[0]=hand.palm_position.x
        pos[1]=hand.palm_position.y
        pos[2]=hand.palm_position.z
        if hand.is_left:
            vrep.simxSetObjectPosition(clientID, nHandlel, -1, pos, vrep.simx_opmode_oneshot_wait)
        elif hand.is_right:
            vrep.simxSetObjectPosition(clientID, nHandler, -1, pos, vrep.simx_opmode_oneshot_wait)
        else:
            print "need a hand"







    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()















































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

    controller = Leap.Controller()





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
