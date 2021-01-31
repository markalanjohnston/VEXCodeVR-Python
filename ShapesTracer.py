# ------------------------------------------
#
# 	Project:      VEXcode Project
#	Author:       Mark Johnston
#	Created:      2021-01-30
#	Description:  code used at https://vr.vex.com for the Shape Tracer Playground
#   Copyright:    Copyright and related rights waived via CC0
#
# ------------------------------------------

# Library imports
from vexcode import *

def poly(num_sides, len):
    global myVariable
    for repeat_count in range(int(num_sides)):
        drivetrain.drive_for(FORWARD, len, MM)
        drivetrain.turn_for(RIGHT, (360 / num_sides), DEGREES)
        wait(5, MSEC)

def when_started():
    pen.move(DOWN)
    if location.position(X, MM) == -842 and location.position(Y, MM) == 340:
        drivetrain.drive_for(FORWARD, 500, MM)
        drivetrain.turn_for(RIGHT, (180 - (180 - 90) / 2), DEGREES)
        drivetrain.drive_for(FORWARD, math.sqrt(2 * (500**2)), MM)
        drivetrain.turn_for(RIGHT, (180 - (180 - 90) / 2), DEGREES)
        drivetrain.drive_for(FORWARD, 500, MM)
    if location.position(X, MM) == -180 and location.position(Y, MM) == 342:
        for repeat_count2 in range(3):
            drivetrain.drive_for(FORWARD, 500, MM)
            drivetrain.turn_for(RIGHT, (180 - 180 / 3), DEGREES)
            wait(5, MSEC)
    if location.position(X, MM) == 483 and location.position(Y, MM) == 540:
        drivetrain.drive_for(FORWARD, 380, MM)
        drivetrain.turn_for(RIGHT, 150, DEGREES)
        drivetrain.drive_for(FORWARD, 740, MM)
        drivetrain.turn_for(RIGHT, (180 - 24.815), DEGREES)
        drivetrain.drive_for(FORWARD, 452.71, MM)
    if location.position(X, MM) == -860 and location.position(Y, MM) == -179:
        poly(5, 345)
    if location.position(X, MM) == -260 and location.position(Y, MM) == -141:
        poly(6, 290)
    if location.position(X, MM) == 322 and location.position(Y, MM) == -122:
        poly(8, 235)
    if location.position(X, MM) == -903 and location.position(Y, MM) == -722:
        for repeat_count3 in range(4):
            drivetrain.drive_for(FORWARD, 189, MM)
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            drivetrain.drive_for(FORWARD, 189, MM)
            drivetrain.turn_for(LEFT, 90, DEGREES)
            drivetrain.drive_for(FORWARD, 189, MM)
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            wait(5, MSEC)
    if location.position(X, MM) == -301 and location.position(Y, MM) == -522:
        for repeat_count4 in range(2):
            drivetrain.drive_for(FORWARD, 200, MM)
            drivetrain.turn_for(RIGHT, 120, DEGREES)
            drivetrain.drive_for(FORWARD, 675, MM)
            drivetrain.turn_for(RIGHT, 60, DEGREES)
            wait(5, MSEC)
    if location.position(X, MM) == 343 and location.position(Y, MM) == -859:
        for repeat_count5 in range(2):
            drivetrain.drive_for(FORWARD, 525, MM)
            if repeat_count5 == 0:
                drivetrain.turn_for(RIGHT, 135, DEGREES)
            else:
                drivetrain.turn_for(LEFT, 135, DEGREES)
            drivetrain.drive_for(FORWARD, math.sqrt(2 * (525**2)), MM)
            if repeat_count5 == 0:
                drivetrain.turn_for(LEFT, 135, DEGREES)
            else:
                drivetrain.turn_for(RIGHT, 135, DEGREES)
            wait(5, MSEC)

vr_thread(when_started())
