# Input: UC Berkeley departments (currently only supports one word departments)
# Output: list of classes and which L&S breadth categories they fulfill, for each department requested

import sys
from bs4 import BeautifulSoup
import requests
import collections

baseLinkBreadths = "http://ls-advise.berkeley.edu/requirement/breadth7/"
bCategories = {'al.html': 'Arts & Literature', 'bs.html': 'Biological Sciences', 'hs.html': 'Historical Studies', \
        'is.html': 'International Studies', 'pv.html': 'Philosophy & Values', 'ps.html': 'Physical Science', \
        'sbs.html': 'Social and Behavioral Sciences'}

# dictionary of dictionaries; 
# 1st level dictionary is each of the departments requested, 
# 2nd level dictionary is the class number
yourDepts = {}


# Searches through all 7 breadth listings for classes that
# match the requested deparments; adds them to the yourDepts
# dictionary
def findDeptClasses():
    for category in bCategories:
        r  = requests.get(baseLinkBreadths + category)
        data = r.text
        soup = BeautifulSoup(data)
        allDepts = soup.find("div", { "id" : "content_main" }).find("ul").find_all('li')

        for dept in allDepts:
            for yourDept in yourDepts:
                if yourDept in dept.string:
                    for word in dept.string.split():
                        if hasNum(word):                    # accounts for class numbers like C142, 100AC, etc.
                                                            # doesn't add the actual name of the department this way
                            addClasses(word, yourDept, bCategories[category])


# Parses the String containing the class number and adds it
# to the yourDepts dictionary in a readable way

# classNum: the class number to evaluate and add, e.g. 100AC
# yourDept: the current requested department, e.g. Spanish
# categoryName: which of the 7 breadths it is
def addClasses(classNum, yourDept, categoryName):
    if classNum[-1] == ',':
        classNum = classNum[:-1]
    if classNum in yourDepts[yourDept]:
        yourDepts[yourDept][classNum].append(categoryName)
    else:
        yourDepts[yourDept][classNum] = [categoryName]


# checks if the argument passed contains a number
# if it contains a number, it's a class and not a department

# s: potential class number
def hasNum(s):
    return any(i.isdigit() for i in s)


# prints out all the classes in yourDepts
def printClasses():
    for dept in yourDepts:
        print("==========================================================================")
        print(dept.upper())
        sortedClasses = collections.OrderedDict(sorted(yourDepts[dept].items()))
        for classNum, cats in sortedClasses.iteritems():
            print(str(classNum) + ": " + cats)
            

def main():
    deptArgs = ""
    deptArgs = raw_input("Enter the departments for which you want to list all L&S breadth classes, separated by semicolons: ")
    if len(deptArgs) < 1:
        deptArgs = raw_input("You must enter at least one department: ")
    deptArgs = deptArgs.split("; ")
    for arg in deptArgs:
        yourDepts[arg] = {}
    findDeptClasses()
    printClasses()

if __name__ == "__main__":
    main()
