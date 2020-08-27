import numpy as np
import random
import time
import requests
from gtts import gTTS
import os

def getStudents():
  r = requests.get('https://olivmarcos.github.io/agente/students.json')
  data = r.json()
  students = data['students']
  return students

def getSchedule ( numberOfStudents, numberOfCalls, classDuration ):
  schedule = classDuration / numberOfStudents
  schedule = schedule / numberOfCalls
  return schedule

def getStudent():
  students = getStudents()
  init = 0
  end = len( students ) - 1
  index = random.randint(init, end)
  student = students[index]
  return student

students = getStudents()

numberOfStudents = len( students )
numberOfCalls = 3
classDuration = 100

schedule = getSchedule( numberOfStudents, numberOfCalls, classDuration )

studentsCalled = []

while classDuration > 0:
  student = getStudent()
  if not student in studentsCalled:
    classDuration = classDuration - schedule
    time.sleep( schedule )
    studentsCalled.append( student )
    print( student )
    output = gTTS(text=student, lang='pt-BR', slow=False)
    output.save('output.mp3')

    os.system('start output.mp3')
