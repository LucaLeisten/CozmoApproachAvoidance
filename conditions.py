import random
import pickle

conditions_list = [0]*200 + [1]*200
random.shuffle(conditions_list)

fh = open("conditions_list.pkl",'wb')
pickle.dump(conditions_list,fh)
fh.close


