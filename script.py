# Befehlsaufbau: python script.py *einteilen/austeilen* *Übungsnummer* *Tutorname*
# die Abgaben sollten sich in einem Unterordner "abgaben" im gleichen Verzeichnis des Skrips befinden.

import os
import re
import sys
import random

dir_list = os.listdir("abgaben")

group_numbers = []
tutors = ["Alex","Bernd","Christoph","Detlef","Elmar"]
random.shuffle(tutors)

def remove_duplicates(x):
    return list(dict.fromkeys(x))

for dir in dir_list:
    group_numbers.append(re.search("Abgabegruppe [0-9]+",dir).group(0).split()[1]) # get the group numbers
group_numbers = remove_duplicates(group_numbers)

print("--- ABGABENVERWALTUNG ---")
print("Tutors: " + str(tutors))
print("Group numbers: " + str(group_numbers))

exercises_perTutor = len(group_numbers) // len(tutors)
remaining = len(group_numbers) % len(tutors)
print("There are " + str(len(group_numbers)) + " groups. ", end="")
print("Therefore every Tutor gets " + str(exercises_perTutor) + " exercises with " + str(remaining) + " exercises remaining")

unlucky = random.sample(tutors,remaining)
print("and fate decides " + str(unlucky) + " get +1 exercises")

def austeilen():
    print()
    print("--- AUSTEILEN ---")
    index_groups = 0
    index_groups_start = 0
    index_tutor = 0
    
    for tutor in tutors:
        ex_tutor = []
        if tutor in unlucky:
            while index_groups < index_groups_start+exercises_perTutor+1:
                ex_tutor.append(group_numbers[index_groups])
                index_groups += 1
        else:
            while index_groups < index_groups_start+exercises_perTutor:
                ex_tutor.append(group_numbers[index_groups])
                index_groups += 1

        index_groups_start = index_groups
        print("Tutor " + str(tutors[index_tutor]) + " gets groups " + str(ex_tutor)) 
        index_tutor += 1
        

def einteilen():
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
