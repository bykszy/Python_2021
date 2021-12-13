import xml.dom.minidom


xml = xml.dom.minidom.parse("../files/xml.xml")
foods = xml.documentElement.getElementsByTagName('food')

name = foods[0].getElementsByTagName('name')[0].childNodes[0].data
price = foods[0].getElementsByTagName('price')[0].childNodes[0].data
description = foods[0].getElementsByTagName('description')[0].childNodes[0].data

print(f"{name}: {price} {description}")

# change name of person to something else
foods[0].getElementsByTagName('name')[0].childNodes[0].data = 'Crepes'
with open('xml_new.xml', 'w+') as new_file:
    new_file.write(xml.toxml())