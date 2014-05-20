# test 12 more xml xml creation

import xml.dom.minidom as mxml

stepOne = mxml.getDOMImplementation()

newXmlDoc = stepOne.createDocument(None, "some_tag", None)
top_element = newXmlDoc.documentElement
text = newXmlDoc.createTextNode('Some Content')
top_element.appendChild(text)

newXmlDocTwo = stepOne.createDocument(None, "Name", None)
top_element_two = newXmlDocTwo.documentElement
text_two = newXmlDoc.createTextNode('Bobby Bouche')
top_element_two.appendChild(text_two)


some_string = newXmlDoc.toprettyxml()
some_other_string = newXmlDocTwo.toprettyxml()
print some_string
print some_other_string
