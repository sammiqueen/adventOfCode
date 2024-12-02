#! /usr/bin/python3

import sys

def safetyChecker(reports):

    unsafeReports = 0
    for report in reports:
        for i in range(len(report) - 1):
            if(
                (abs(report[i] - report[i + 1]) >= 1
                and
                abs(report[i] - report[i + 1]) <= 3)
            ):
                pass
            else:
                unsafeReports = unsafeReports + 1
                reports.remove(report)
                print(report," was unsafe due to diff")
                break

    risingCurrent = False
    risingPast = False
    for report in reports:
        for i in range(len(report) - 1):
            if(
                report[i] > report[i + 1]
            ):
                risingCurrent = False
            else:
                risingCurrent = True
            
            if(i > 0):
                if(risingPast != risingCurrent):
                    unsafeReports = unsafeReports + 1
                    print(report," was unsafe due to rise/decline")
                    break
            risingPast = risingCurrent
    

    
    return unsafeReports

reports = []
for line in sys.stdin:
    reports.append(line.split())

for report in reports:
    for i in range(len(report)):
        report[i] = int(report[i])

reportsAmnt = len(reports)

unsafeReports = safetyChecker(reports)

safeReports = (reportsAmnt) - unsafeReports
print(unsafeReports, " unsafe reports")
print(safeReports, " safe reports")
print(reportsAmnt, " total reports")