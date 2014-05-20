# test 11 more xml

import xml.dom.minidom as mxml

newdom = mxml.getDOMImplementation()

root = newdom.createDocument(None, "violation_record", None)
top_element = root.documentElement

# Create First Name obj
firstNameNode = root.createElement("FName")
firstNameData = root.createTextNode("Christopher")
firstNameNode.appendChild(firstNameData)

minitNode = root.createElement("MI")
minitData = root.createTextNode("R")
minitNode.appendChild(minitData)

lastNameNode = root.createElement("LName")
lastNameData = root.createTextNode("Halbersma")
lastNameNode.appendChild(lastNameData)


top_element.appendChild(firstNameNode)
top_element.appendChild(minitNode)
top_element.appendChild(lastNameNode)

some_string = root.toprettyxml()

xmlfile = open("test14.xml", "w")
xmlfile.write(some_string)

print some_string
