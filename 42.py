import xmltodict

xml_data = open("payments.xml").read()
data_dict = xmltodict.parse(xml_data)
root = data_dict['employees']
employees = root['employee']

selected = []

for i in employees:
    if int(i["age"]) >= 30:
        selected.append(i)

print(selected)

# =============================================

import dicttoxml

# Convert selected list into XML format
xml_output = dicttoxml.dicttoxml({'employees': selected})

# Save to a file
with open("selected_employees.xml", "wb") as f:
    f.write(xml_output)

print("XML file has been created successfully!")
