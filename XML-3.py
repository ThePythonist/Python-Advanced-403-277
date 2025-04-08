import xml.etree.ElementTree as ET
import xmltodict

tree = ET.parse("flights.xml")
root = tree.getroot()

xml_string = ET.tostring(root, encoding='utf8', method='xml')

xml_dict = xmltodict.parse(xml_string)
print(xml_dict)
