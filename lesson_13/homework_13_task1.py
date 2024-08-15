import csv

with open('random.csv', mode='r', newline='') as f1:
    reader1 = csv.reader(f1)
    data1 = list(reader1)

with open('random-michaels.csv', mode='r', newline='') as f2:
    reader2 = csv.reader(f2)
    data2 = list(reader2)

combined_data = data1 + data2

unique_data = list(map(list, set(map(tuple, combined_data))))

output_file = 'result_Alokhin.csv'
with open(output_file, mode='w', newline='') as output_f:
    writer = csv.writer(output_f)
    writer.writerows(unique_data)
