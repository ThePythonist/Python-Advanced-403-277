import xml.etree.ElementTree as ET

xml_data = open("payments.xml").read()
root = ET.fromstring(xml_data)
employees = root.findall("employee")

python_salaries = []

for i in employees:
    job = i.find("job_title")
    if "python" in job.text.lower():
        payment = i.find("monthly_payment")
        for j in payment:
            python_salaries.append(float(j.text))

print(sum(python_salaries) / len(python_salaries))
