#!/usr/bin/env python3

# Copyright (c) 2016 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''Drive And Turn

Make Cozmo drive

'''

import cozmo
import time

from cozmo.util import degrees, distance_mm, speed_mmps

def cozmo_program(robot: cozmo.robot.Robot):
    keep_running = True
    current_speed = 50.0
    prior_action = 'stop'
    while keep_running:
        action = input('Direction forward, backward, left, faster, slower left, right, stop or exit?')
        if action == 'faster':
            robot.stop_all_motors()
            current_speed += 10
            if prior_action == 'forward':
               robot.drive_wheels(current_speed,current_speed)
               action = 'forward'
            elif prior_action == 'backward':
                robot.drive_wheels(-current_speed,-current_speed)
                action = 'backward'
        elif action == 'slower':
            robot.stop_all_motors()
            current_speed -= 10
            if prior_action == 'forward':
               robot.drive_wheels(current_speed,current_speed)
               action = 'forward'
            elif prior_action == 'backward':
                robot.drive_wheels(-current_speed,-current_speed)
                action = 'backward'
        elif action == 'left':
            response = robot.stop_all_motors()
            turn_action = robot.turn_in_place(degrees(45), num_retries=10)
        elif action == 'right':
            robot.stop_all_motors()
            robot.turn_in_place(degrees(-45))
        elif action == 'stop':
            robot.stop_all_motors()          
        elif action =='forward':
            robot.stop_all_motors()
            robot.drive_wheels(current_speed,current_speed)
        elif action == 'backward':
            robot.stop_all_motors()
            robot.drive_wheels(-current_speed,-current_speed)
        elif action == 'exit':
            robot.stop_all_motors()
            break
        
        prior_action = action

cozmo.run_program(cozmo_program)
