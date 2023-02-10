history = {
    "hero3" : {
        "ID" : 21861514,
        "name" : "Steve",
        "surname" : "Jobs"
    },
    "hero1" : {
        "ID" : 18346587,
        "name" : "Nelson",
        "surname" : "Mandela"
    },
    "hero2" : {
        "ID" : 20893456,
        "name" : "Richard",
        "surname" : "Feynman"
    }
    }

import collections
#x = sorted(history)
sorted_history = sorted(history.items(), key=lambda ID: ID[0] )

#print(x , sep = '\n')

od = collections.OrderedDict(sorted(history.items()))

print(history , sep ='\n')
