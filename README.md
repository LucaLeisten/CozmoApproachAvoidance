# Cozmo approach or avoidance behaviors 
This program will randomly choose to display a shuffled list of predefined cozmo animations. The conditions are approach vs. avoidance. The data is saved in a CSV file, including the participant ID, the condition and the displayed animations.

## First setup
1. Run conditions.py
This file creates a balanced randomization of conditions, through creating a conditions_list.pkl file, that contains 200x 0s and 200x 1s. The main file draws a conditions from this file and deletes it after. If you know your number of participants before hand, you can adjust the number of 0s and 1s in the conditions.py file.

2. Run create_csv.py
This file creates an initial csv file with headers to store your data in

## Run experiment
1. Run animations.py --participantID=[enterparticipantID]
2. participant ID is required
