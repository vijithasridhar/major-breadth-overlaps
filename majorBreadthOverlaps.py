import deptBreadths
import csv
import sys
from bs4 import BeautifulSoup
import requests
import collections

baseLinkReqts = "http://bulletin.berkeley.edu/undergraduate/degree-programs/"
majorMinorList = "http://admissions.berkeley.edu/majors"
allMajors = []
allMinors = []

# majors/minors and their respective links
yourMajors = []
yourMinors = []
# classes needed for majors/minors; organized by major/minor name
neededClasses = {}       # {"Spanish" : {"Spanish": [101, 104, ...     }  ... }

deptAbbrSite = "http://registrar.berkeley.edu/?PageID=deptabb.html"
deptAbbrs = {}           # {"SPAN" : "Spanish", ... }

neededDepts = []
removalWords = ['and', 'the', 'of']
commonalities = {}

# Go to the major/minor website on Berkeley bulletin
# Find the department of this major/minor (NOT college)
# Create a list of all of the required classes
# Look through the dept-breadths results for the specified department to find matching classes
# between the list of major-required classes and list of breadth-provided classes



# Gets and parses the list of department abbreviations from 
# the website given by deptAbbrSite
# adds the list to the deptAbbrs dictionary
def defineDeptAbbrs():
    with open('berkeley-dept-abbrs.csv', 'rU') as csvfile:
        deptReader = csv.reader(csvfile)
        for row in deptReader:
            deptName = row[0]
            deptAbbr = row[1]
            deptAbbr = deptAbbr.replace(" ", "")
            deptAbbr1 = deptAbbr.decode('ascii', 'ignore')
            deptAbbrs[deptAbbr1] = deptName

    # r  = requests.get(deptAbbrSite)
    # data = r.text
    # soup = BeautifulSoup(data)

    # deptAbbrTable = soup.find("table", { "id" : "deptAbb" }).find("tbody").find_all('tr')   #edit this
    # for row in deptAbbrTable:
    #     #row = BeautifulSoup(r)
    #     rowData = row.find_all('td')
    #     if len(rowData) == 2:
    #         # 2 td's which implies that there's a name and an abbreviation listed
    #         deptName = rowData[0].get_text()
    #         deptAbbr = rowData[1].get_text()
    #         deptAbbr = deptAbbr.strip()
    #         deptAbbr = deptAbbr.replace("&nbsp;", " ")
    #         deptAbbr = deptAbbr.replace("\'" + "xa0", " ")
    #         deptAbbr = deptAbbr.replace("\t", "")
    #         deptAbbr = deptAbbr.replace("\n", "")
    #         deptAbbr = deptAbbr.replace("\r", "")
    #         deptAbbr = deptAbbr.replace(" ", "")
    #         deptName = deptName.strip()
    #         deptName = deptName.replace("&nbsp;", " ")
    #         if deptAbbr not in deptAbbrs:
    #             deptAbbrs[unicode(deptAbbr)] = deptName

def defineMajorsMinors():
    with open('berkeley-majors.csv', 'rU') as csvfile:
        majorReader = csv.reader(csvfile)
        for row in majorReader:
            allMajors.append(row[0])
    with open('berkeley-minors.csv', 'rU') as csvfile:
        minorReader = csv.reader(csvfile)
        for row in minorReader:
            allMinors.append(row[0])
    # print(allMajors)
    # print(allMinors)

    # r  = requests.get(majorMinorList)
    # data = r.text
    # soup = BeautifulSoup(data)

    # majorMinorTables = soup.find_all("table")   #edit this
    # for x in range(0, 5):
    #     majorTags = majorMinorTables[x].find_all("a")
    #     for i in majorTags:
    #         allMajors.append(i.get_text())
    
    # for x in range(5, len(majorMinorTables) - 1):
    #     minorTags = majorMinorTables[x].find_all("a")
    #     for i in minorTags:
    #         allMinors.append(i.get_text())


# adds all major/minor requirements to the neededClasses dictionary
def listMMReqts():
    def listReqts(mmName, type):
        neededClasses[mmName] = {}
        linkPart = processName(mmName)
        linkAddress = baseLinkReqts + linkPart + "/#" + type + "requirementstext"
        r  = requests.get(linkAddress)
        try:
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            print("There's been an error accessing the Berkeley Bulletin webpage for the " \
                    + mmName + " " + type + ":\n" + linkAddress + "\nError message: " + e.message)
        data = r.text
        soup = BeautifulSoup(data)
        allTables = soup.find_all("table", { "class" : "sc_courselist" })

        for table1 in allTables:
            allReqts =  table1.find_all('a', { "class" : "bubblelink" })
            for aTag in allReqts:
                # startIndex = aTag.find(">")
                # endIndex = aTag.find("<", 2)
                # print (startIndex + ": " + endIndex)
                classTitle = aTag.get_text()
                classTitle = classTitle.replace("&nbsp;", " ")
                classTitle = classTitle.replace(u'\xa0', ' ')

                classParts = classTitle.split(" ")
                deptAbbr = classParts[0]
                classNum = classParts[1]

                if len(classParts) > 2:             #cases like EL ENG
                    for x in range(1, len(classParts) - 1):
                        deptAbbr += classParts[x]
                if deptAbbr in deptAbbrs:
                    deptName = deptAbbrs[deptAbbr]
                else:
                    print("Could not find the department name for " + deptAbbr + " for class " + classTitle)
                if deptName not in neededClasses[mmName]:
                    neededClasses[mmName][deptName] = []

                neededClasses[mmName][deptName].append(classNum)
                neededDepts.append(deptName)

    for major in yourMajors:
        listReqts(major, "major")
    for minor in yourMinors:
        listReqts(minor, "minor")


# finds the classes that are common between breadth reqts
# and major/minor requirements
def findCommonClasses():
    for dept in neededDepts:
        deptBreadths.yourDepts[dept] = {}
    deptBreadths.findDeptClasses()

    for mmName in neededClasses:
        commonalities[mmName] = []
        for deptName in neededClasses[mmName]:     # list of needed classes for a specific major/minor
            for num in neededClasses[mmName][deptName]:
                if num in deptBreadths.yourDepts[deptName]:    # if the major/minor classNum is in the breadths list
                    commonalities[mmName].append([deptName, num, deptBreadths.yourDepts[deptName][num]])

def printResults():
    for mmName in commonalities:
        print("\n" + mmName + "\n------------------------------------------------")
        for classDescrip in commonalities[mmName]:
            breadthList = ""
            for breadthType in classDescrip[2]:
                breadthList += breadthType + ", "
            print(classDescrip[0] + " " + classDescrip[1] + ": " + breadthList[:-2])


# Processes the names of majors and minors, so that you
# get part of a link that you can feed into the beautiful soup
# mmName: name of input major/minor
def processName(mmName):
    words = mmName.split(' ')
    nameLink = ""
    for word in words:
        if word not in removalWords:
            if word[-1:] == ",":
                word = word[:-1]
            nameLink += word.lower() + '-'
    nameLink = nameLink[:-1]
    return nameLink


def main():
    defineMajorsMinors()
    majors = raw_input("Enter the following with semicolons (;) separating multiple majors/minors. \n" \
                            + "What majors are you considering? ")
    if majors != "":
        for major in majors.split(';'):
            major = major.strip()
            if major not in allMajors:
                raise SystemExit(major + " is an invalid major. Please ensure that you've entered" \
                    + " a major from the official UC Berkeley list, at " + majorMinorList \
                    + ", and rerun this script.")
            yourMajors.append(major)
    minors = raw_input("What minors are you considering? ")
    if minors != "":
        for minor in minors.split(';'):
            minor = minor.strip()
            if minor not in allMinors:
                raise SystemExit(minor + " is an invalid minor. Please ensure that you've entered \n" \
                    + "a minor from the official UC Berkeley list, at " + majorMinorList \
                    + "\n, and rerun this script.")
            yourMinors.append(minor)
    defineDeptAbbrs()
    listMMReqts()
    findCommonClasses()
    printResults()


if __name__ == "__main__":
    main()

