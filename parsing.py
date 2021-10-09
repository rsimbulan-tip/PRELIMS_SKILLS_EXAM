import json
import csv

jsonPath = './covid_cases.json'
with open(jsonPath,'r') as covid:
    data = json.loads(covid.read())

csvPath = './covid_cases.csv'
with open(csvPath,'w') as json_parsed:
    csv_file = csv.writer(json_parsed)
    csv_file.writerow(["dateRep","countriesAndTerritories","cases","deaths"])

for records in data ["records"]:
    csv_file.writerow([
    records["dateRep"],
    records["countriesAndTerritories"],
    records["cases"],
    records["deaths"]])

    