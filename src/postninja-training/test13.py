# test 11 more xml

import xml.dom.minidom as mxml

newdom = mxml.getDOMImplementation()

root = newdom.createDocument(None, "violation_record", None)
top_element = root.documentElement
firstNameNode = root.createElement("FName")
firstNameData = root.createTextNode("Christopher")
firstNameNodeNickNode = root.createElement("FNNick")
firstNameNodeNickData = root.createTextNode("Chris")

firstNameNodeNickNode.appendChild(firstNameNodeNickData)


firstNameNode.appendChild(firstNameData)
firstNameNode.appendChild(firstNameNodeNickNode)
top_element.appendChild(firstNameNode)

some_string = root.toprettyxml()

print some_string
