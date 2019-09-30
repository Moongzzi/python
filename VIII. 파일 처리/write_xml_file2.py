import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement

root = Element("Drink")
name = SubElement(root, "name")
price = SubElement(root, "price")
ice = SubElement(root, "ice")
sugar = SubElement(root, "sugar")
pearl = SubElement(root, "pearl")

name.text = "딸기 요거트"
price.text = "3500"
ice.text = "1"
sugar.text = "2"
pearl.text = "1"

rootOpen = ("<Drink>")
rootClose = ("</Drink>")
name = ("<name>"+name+"</name>")
price = ("<price>"+price+"</price>")
print(rootOpen+name+price+rootClose)