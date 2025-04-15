import csv

# ----------------------- Writing data to a CSV file -----------------------

# data = [
#     ['Name', 'Age', 'City'],  # row 1 : header
#     ['John', '25', 'New York'],
#     ['Alice', '30', 'London'],
#     ['Bob', '35', 'Paris']
# ]
#
# with open('data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
#     # with dar akhare kar file ra mibandad
#
# print('file has been created successfully.')

# ----------------------- Reading data from a CSV file -----------------------

# with open('data.csv', 'r') as file:
#     reader = csv.reader(file)
#     print(reader)
#     print(list(reader))
#     for row in reader:
#         print(row)

# ----------------------------------------------------------------------------

# with open('data.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row[0], row[2])

# ----------------------------------------------------------------------------

# with open('data.csv', 'r') as file:
#     reader = csv.reader(file)
#     header = next(reader)
#     # print(header)
#     for row in reader:
#         print(row)

# ----------------------------------------------------------------------------

# with open('data.csv', 'r') as file:
#     reader = csv.reader(file)
#     header = next(reader)
#     print(list(reader)[-2])
