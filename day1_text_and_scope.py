#Python study
#Day 1 : review code
#author : Suhyun An (Julie)
#python 기초문법 + 문자열 처리 + 정규식 표현법



#variable and data types
name = 'julie'
age =25
is_student = True

print(type(name)) #str
print(type(age)) #int
print(type(is_student)) #bool

# -------------------------------
# Lists, Tuples Dictionies, Sets
# -------------------------------

#List
symptoms = ['feaver', 'nausea', 'headache']
symptoms.append('cough')
print(symptoms)

#Tuples (immutable list)
patient_info = ('julie', 25)
print(patient_info)


#Dictionary (key-value structures)
patient = {
    'name':'julie',
    'age':'25',
    'symptoms':['fever','headache']
}
print(patient)
print(patient['symptoms'])


#Set(removes duplicates)
tags = {'fever', 'headache', 'cough', 'fever'}
print(tags)


# -------------------------------
# Conditionals and Loops
# -------------------------------

#if-else-elif condition
temp = 38.5
if temp > 37.5:
    print('fever detected')
elif temp == 37.5:
    print('boderline')
else:
    print('normal')


#for loop: iterate through list
for s in symptoms:
    print('symptoms:',s)



#while loop : run while condition is True
count = 0
while count<3:
    print('checking vitals...')
    count+=1


# -------------------------------
# Function Definition and Call
# -------------------------------

def say_hello():
    print('hello, julie!')

say_hello()


def add(a,b):
    return a+b

print(add(2,3))


def greet(name='julie'):
    print(f'hello, {name}!')

greet()
greet('suhyun')



# -------------------------------
# Basic string Methods
# -------------------------------

text = 'Patient has a FEVER of 102°F and also shows COUGH.'

#Convert to lowercase
lowered = text.lower()
print('Lowered',lowered)


#Split into words
tokens = lowered.split()
print('split into words', tokens)


# -------------------------------------
# Regex: re.sub, re.findall, re.split
# -------------------------------------

import re

#Remove non-alphabet charactoer using re.sub
cleaned = re.sub(r'[^a-z\s]',"",lowered)
cleaned


#Find specific symptoms using re.findall
note = 'Patient complains of headache, nausea, and dizziness.'
symptoms = re.findall(r'headache|nausea|dizzinies', note)
print('extracted symtoms', symptoms)


#Split sentences usring re.split
long_note = "Patient has fever. He also reports nausea. Check BP."
sentences = re.split(r'\. ?', long_note)
print('Split sentences', sentences)


#Remove empty strings(optinal)
sentences = [s for s in sentences if s.strip()]
print('filtered sentences', sentences)

