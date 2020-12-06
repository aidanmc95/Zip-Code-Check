import csv
import zipcodes

file_in = open('testin.csv', newline='')
file_out =  open('testout.csv', 'w', newline='')

reader = csv.DictReader(file_in)
headers = reader.fieldnames

writer = csv.DictWriter(file_out, fieldnames=headers)
writer.writeheader()

for row in reader:
    if(row['Zip Code'] and row['City'] and row['State']):
        zip_data = zipcodes.matching(row['Zip Code'])
        if(zip_data):
            if(zip_data[0]['active'] and zip_data[0]['city'].upper() == row['City'].upper() and zip_data[0]['state'].upper() == row['State'].upper()):
                row['\ufeffCheck'] = 'Good'
            else:
                row['\ufeffCheck'] = 'Bad'
        else:
            row['\ufeffCheck'] = 'Bad'
    else:
        row['\ufeffCheck'] = 'Bad'
    writer.writerow(row)

file_in.close()
file_out.close()