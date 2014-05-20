# test 11 more xml

import xml.dom.minidom as mxml

stepOne = mxml.getDOMImplementation()

newXmlDoc = stepOne.createDocument(None, "some_tag", None)
top_element = newXmlDoc.documentElement
text = newXmlDoc.createTextNode('Some Content')
top_element.appendChild(text)

some_string = newXmlDoc.toprettyxml()
print some_string
