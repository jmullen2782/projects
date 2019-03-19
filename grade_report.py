'''
Created on Mar 12, 2019
Grade Report
@author: Jennie Mullen
'''
def main():
    studentList = {}
    name = input("Would you like to add or delete a student's name?")
    name.lower()
    if name == 'add':
        student = input('Which student would you like to add?')
        grade = int(input("What grade would you like to add"))
        studentList[student] = grade
    else:
        del studentList[name]
    print(studentList)
main()