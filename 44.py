import xml.etree.ElementTree as ET

xml_data = open("flights.xml").read()
root = ET.fromstring(xml_data)

flights = root.findall("flight")  # List

for i in flights:
    if i.find("destination").text.lower() == "paris":
        print(i.find("flight_number").text)
        print(i.find("origin").text, "to", i.find("destination").text)
        print("=" * 100)
