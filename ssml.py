import xml.etree.ElementTree as ET

# create the root element for the SSML document
root = ET.Element('speak', version='1.0', xmlns='http://www.w3.org/2001/10/synthesis', xml_lang='en-US')

# add some SSML tags to the document
say_as = ET.SubElement(root, 'say-as', interpret_as='cardinal')
say_as.text = '1234'
p = ET.SubElement(root, 'p')
p.text = 'Here is a paragraph of text that will be spoken out loud.'

# serialize the SSML document to a string
ssml_string = ET.tostring(root, encoding='unicode')

# print the SSML markup
print(ssml_string)
