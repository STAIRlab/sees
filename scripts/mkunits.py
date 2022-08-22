#!/usr/bin/env python
import csv
from sys import argv



def write(system, spreadsheet, file):
    print(f"\n{C}\n{C} ", spreadsheet[0][system].upper(), f"\n{C}\n", file=file)
    for i,row in enumerate(spreadsheet[1:]):
        if not row[system]:
            continue
        if row[0]:
            print(f"\n{C}\n{C} ", row[0].title(), f"\n{C}", file=file)

        if row[2]:
            primary, secondary = row[2:4]
        else:
            primary, secondary = row[3], None

        assignment = f"{primary:12} = {float(row[system])}"

        if secondary:
            assignment = f"{secondary:12} = {assignment}"
        else:
            assignment = f"{assignment}".replace("=", " "*(12+3) + "=")
        
        assignment +=  " "*(50 - len(assignment))

        if row[1]:
            assignment += f"{C} {row[1]}"

        print(assignment, file=file)


if __name__ == "__main__":
    systems = "MKS", "CGS", "FAS", "FPS", "FKS", "IPS", "IKS", "IAS"

    C = "#"

    with open(argv[1], 'r') as read_obj: 
        csv_reader = csv.reader(read_obj)
      
        spreadsheet = list(csv_reader)

    if len(argv) > 2:
        system = int(argv[2])
        write(system, spreadsheet, sys.stdout)
    else:
        for i, system in enumerate(systems):
            with open(f"{system}.py".lower(), "w+") as f:
                write(i+5, spreadsheet, f)

