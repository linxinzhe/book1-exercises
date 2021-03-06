# 10.3 review exercises


# Initial setup
import os
import csv
# This path may need to be changed depending on your setup
path = "C:/Real Python/Course Materials/Chapter 10/Practice files"


# Read in a CSV and display each row except the header row
# Append a third column and write out the resulting CSV with a new header
in_file_path = os.path.join(path, "pastimes.csv")
out_file_path = os.path.join(path, "Output/categorized pastimes.csv")
with open(in_file_path, "rb") as inFile, open(out_file_path, "wb") as outFile:
    csv_reader = csv.reader(inFile)
    csv_writer = csv.writer(outFile)

    # skip header row and write a new output header row
    csv_reader.next()
    csv_writer.writerow(["Name", "Favorite Pastime", "Type of pastime"])

    for row in csv_reader:
        print row
        # Check if "Favorite Pastime" includes "fighting"
        if row[1].lower().find("fighting") != -1:
            row.append("Combat")
        else:
            row.append("Other")
        # Add the new row to the output
        csv_writer.writerow(row)
