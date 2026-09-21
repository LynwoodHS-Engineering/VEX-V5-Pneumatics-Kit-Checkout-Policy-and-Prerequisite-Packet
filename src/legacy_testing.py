import vex
import time

#create a brain object
brain = Brain()

#create two pnuematic cylinder objects
cylinderC = DigitalOut(brain.three_wire_port.c)
cylinderD = DigitalOut(brain.three_wire_port.d)

# set the cylinders to be off - They will both retract when the program starts
cylinderC.set(False)
cylinderD.set(False)
brain.screen.clear_screen()
brain.screen.print("Cylinders are in starting position")
wait(2, SECONDS)


while True:
    #set the cylinders to be on
    cylinderC.set(True)
    cylinderD.set(True)
    brain.screen.clear_screen()
    brain.screen.print("Cylinders are on")
    wait(1, SECONDS)

    #set the cylinders to be off
    cylinderC.set(False)
    cylinderD.set(False)
    brain.screen.clear_screen()
    brain.screen.print("Cylinders are off")
    wait(1, SECONDS)