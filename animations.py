# playing approaching or avoiding animations of cozmo.
# participants are randomly assigned to one conditions, based on a list with 100x approach and 100x avoidance. Everytime one condition is assigned, this gets removed from the list, making the assignment balanced.
# 10 animations per conditions were chosen, these are balanced in arousal

import cozmo
import random
import argparse
import keyboard
import time
import pickle
from cozmo.util import degrees, distance_mm, speed_mmps
import csv

approach_list = ["anim_meetcozmo_celebration_02_head_angle_40","anim_hiking_rtnewarea_01","anim_hiking_rtnewarea_02","anim_petdetection_dog_01_head_angle_20","anim_freeplay_reacttoface_sayname_01_head_angle_40","anim_memorymatch_successhand_cozmo_03","anim_peekaboo_success_02","anim_fistbump_success_02","anim_memorymatch_successhand_cozmo_04","anim_peekaboo_success_03","anim_freeplay_reacttoface_wiggle_01"]
random.shuffle(approach_list)
avoidance_list = ["anim_cozmosays_badword_01_head_angle_20","anim_pounce_fail_02","anim_peekaboo_failgetout_01","anim_fistbump_fail_01","anim_speedtap_loseround_intensity01_01","anim_keepaway_losegame_01","anim_speedtap_loseround_intensity02_01","anim_keepaway_losehand_02","anim_rtpmemorymatch_no_01","anim_reacttocliff_stuckleftside_03","anim_gotosleep_off_01","anim_memorymatch_failgame_cozmo_03","anim_rtpmemorymatch_no_01","anim_rtpkeepaway_playerno_01"]
random.shuffle(avoidance_list)

# set fieldnames for csv file
fieldnames = ['ParticipantID','Condition','Animation']

def get_in_position(robot: cozmo.robot.Robot, baseline):
    # set volumne to 0 so that cozmo does not make noise while moving back to baseline position
    robot.set_robot_volume(0)
    # move back to baseline position
    robot.set_lift_height(0.0).wait_for_completed()
    robot.go_to_pose(baseline, relative_to_robot=False).wait_for_completed()
    # turn volumne back on
    robot.set_robot_volume(100)


# add writing file that saves participant id, and approach or avoidance
def cozmo_approach(robot: cozmo.robot.Robot):
    # get participant ID from terminal and save to object
    log_path = None
    parser = argparse.ArgumentParser()
    parser.add_argument("--participantID", type=str, required=True,
                         help="Participant ID is required to record logs correctly")

    args = parser.parse_args()
    participantID = args.participantID

    # choose randomly number 1 or 2 to assign to condition
    fh = open("conditions_list.pkl",'rb')
    conditions_list = pickle.load(fh)
    fh.close() 

    # set baseline position
    baseline = robot.pose   
    reset = 0

    # turn volume on in case the last reset happened when volume was turned off
    robot.set_robot_volume(100)

    # do one wake-up animation to see that program has started.
    robot.play_anim("anim_launch_wakeup_03").wait_for_completed()

    # set cozmo to sleep for 10 seconds before animations starts to give user time to start the game
    time.sleep(10)
    
    # if number of 0s in conditions_list is larger than numbers of 1s display approach behaviors
    if conditions_list.count(0) > conditions_list.count(1):
        condition = str("approach")
        # remove one 0 from the list to update number of conditions assigned
        conditions_list.remove(0)
        # update the list
        fh = open("conditions_list.pkl",'wb')
        pickle.dump(conditions_list, fh)
        fh.close()

        # save cozmos coordinates for baseline
        try:
            while True:
                for animation in approach_list:
                    robot.play_anim(animation).wait_for_completed()
                    get_in_position(robot, baseline)
                    time.sleep(1)

                    with open('data.csv', 'a') as csvfile:
                        csvfile.write("{},{},{}".format(participantID, condition, animation))
                        csvfile.write("\n")
                    csvfile.close()
                    
        except KeyboardInterrupt:
            pass
        # turn back to baseline
    # if numbers of 1s is larger than numbers of 0s display avoidance behaviors
    elif conditions_list.count(1) > conditions_list.count(0):
        condition = str("avoidance")
        # remove a 1 from conditions list to update number of conditions assigned
        conditions_list.remove(1)
        # update the list
        fh = open("conditions_list.pkl",'wb')
        pickle.dump(conditions_list, fh)
        fh.close()

        try:
            while True:
                for animation in avoidance_list:
                    robot.play_anim(animation).wait_for_completed()                   
                    get_in_position(robot, baseline)
                    time.sleep(1)

                    with open('data.csv', 'a') as csvfile:
                        csvfile.write("{},{},{}".format(participantID, condition, animation))
                        csvfile.write("\n")
                    csvfile.close()

        except KeyboardInterrupt:
            pass

    else:
        random_number = random.randrange(0,2)
        if random_number == 0:
            condition = str("approach")
            # remove one 0 from the list to update number of conditions assigned
            conditions_list.remove(0)
            # update the list
            fh = open("conditions_list.pkl",'wb')
            pickle.dump(conditions_list, fh)
            fh.close()


            try:
                while True:
                    for animation in approach_list:
                        robot.play_anim(animation).wait_for_completed()
                        get_in_position(robot, baseline)
                        time.sleep(1)

                        with open('data.csv', 'a') as csvfile:
                            csvfile.write("{},{},{}".format(participantID, condition, animation))
                            csvfile.write("\n")
                        csvfile.close()
            except KeyboardInterrupt:
                pass

        else:
            condition = str("avoidance")
            # remove a 1 from conditions list to update number of conditions assigned
            conditions_list.remove(1)
            # update the list
            fh = open("conditions_list.pkl",'wb')
            pickle.dump(conditions_list, fh)
            fh.close()

            try:
                while True:
                    for animation in avoidance_list:
                        robot.play_anim(animation).wait_for_completed()
                        get_in_position(robot, baseline)
                        time.sleep(1)

                        with open('data.csv', 'a') as csvfile:
                            csvfile.write("{},{},{}".format(participantID, condition, animation))
                            csvfile.write("\n")
                        csvfile.close()

            except KeyboardInterrupt:
                pass


cozmo.run_program(cozmo_approach)
