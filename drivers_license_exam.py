'''
Created on Mar 4, 2019

@author: jmullen19
'''
answerkey = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
response = []
correct = 0
incorrect = 0
numanswers = 0
index = 0
file = open('drivers license student.txt', 'r')
response = file.readlines()
file.close()

while numanswers != 20:
    response.append()
    numanswers += 1

while index <=19:
    if answerkey[index] == response[index]:
        correct += 1
    else:
        incorrect += 1
    index += 1

if correct >= 15:
    print('You passed!')
else:
    print('You failed')

print('You got', correct,'correct and',incorrect,'incorrect.')
    
        
        