# prepare csv file with headers
with open('data.csv', 'a') as csvfile:
    csvfile.write("{},{},{}".format("ParticipantID", "Condition", "Animation"))
    csvfile.write("\n")
csvfile.close()
