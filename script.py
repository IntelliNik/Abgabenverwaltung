# Befehlsaufbau: python script.py *einteilen/austeilen* *Übungsnummer* *Tutorname*
# die Abgaben sollten sich in einem Unterordner "abgaben" im gleichen Verzeichnis des Skrips befinden.

import os
import re
import sys

dir_exercises = "abgaben"
list_exercises = os.listdir(dir_exercises)

tutors = ["Alex","Bernd","Christoph","Detlef","Elmar"]

def remove_duplicates(x):
  return list(dict.fromkeys(x))

def einteilen():
    groups = []

    for list in list_exercises:
        groups.append(re.search("Abgabegruppe [0-9]+",list).group(0).split()[1]) # get the group numbers
    
    groups = remove_duplicates(groups)

    exercises_perTutor = len(groups) // len(tutors)
    remaining = len(groups) % len(tutors)

    print("There are " + str(len(groups)) + " groups.")

    count = 0
    for tutor in tutors:
        print("Tutor " + tutor + " gets groups " )
        for x in range(count*exercises_perTutor,exercises_perTutor*count+exercises_perTutor):
            print(groups[x]+" ", end='')
        print("")
        count = count + 1


def austeilen():
    print()


if (len(sys.argv) >= 4):
    mode = sys.argv[1]
    exercise = sys.argv[2]
    name = sys.argv[3]
else:
    print("Not enough arguments")
    sys.exit()


if (mode == "einteilen"):
    einteilen()
elif (mode == "austeilen"):
    austeilen()
else: 
    print("Mode not correct")
