#! /usr/bin/python3

import sys

def safetyChecker(reports):

    passedFirstCheck = []
    unsafeReports = 0

    for report in reports:
        state = ""
        for i in range(len(report) - 1):

            if(state == ""):
                if (report[i] > report[i + 1]):
                    state = "falling"
                else:
                    state = "rising"
        
            
            elif (state == "falling"):
                if(report[i] > report[i + 1]):
                    pass
                else:
                    unsafeReports = unsafeReports + 1
                    print(report, " is unsafe")
                    break
            
            elif (state == "rising"):
                if(report[i] < report[i + 1]):
                    pass
                else:
                    unsafeReports = unsafeReports + 1
                    print(report, " is unsafe")
                    break
            
            if (i == (len(report) - 2)):
                passedFirstCheck.append(report)
    
    print(passedFirstCheck, " passed first check")

    passedSecondCheck = []
    for report in passedFirstCheck:
        for i in range(len(report) - 1):
            if (
                abs(report[i] - report[i + 1]) >= 1
                and
                abs(report[i] - report[i + 1]) <= 3
                ):
                pass

            else:
                unsafeReports = unsafeReports + 1
                print(report, " is unsafe")
                break

            if (i == (len(report) - 2)):
                passedSecondCheck.append(report)


    print(passedSecondCheck, " passed second check")
    return passedSecondCheck

reports = []
for line in sys.stdin:
    reports.append(line.split())

for report in reports:
    for i in range(len(report)):
        report[i] = int(report[i])

reportsAmnt = len(reports)

safeReportsAmnt = len(safetyChecker(reports))

unsafeReportsAmnt = reportsAmnt - safeReportsAmnt

print(unsafeReportsAmnt, " unsafe reports")
print(safeReportsAmnt, " safe reports")
print(reportsAmnt, " total reports")