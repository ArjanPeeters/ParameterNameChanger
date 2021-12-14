import ifcopenshell
from ifcopenshell.util import element as ue
import sys
import os

def indent(text: str, indent: int):
    print(' |  ' * indent, text)

class IfcFile():
    def __init__(self, file):
        self.ifc = ifcopenshell.open(file)
        self.elements = self.ifc.by_type('IfcElement')

    def change_parameter_name(self, from_name: str, to_name: str):
        for element in self.elements:
            for definition in element.IsDefinedBy:
                if definition.is_a('IfcRelDefinesByProperties'):
                    pset = definition.RelatingPropertyDefinition
                    indent(pset.Name, 1)
                    for prop in pset.HasProperties:
                        if prop.Name == from_name:
                            prop.Name = to_name
                            print("=" * 100)
                            indent(from_name + " --> " + prop.Name, 2)
                            print("=" * 100)
                        else:
                            indent(prop.Name, 2)



if __name__ == '__main__':
    file = input('Path of the IFC file: ')
    new_file = input('New File name: ')
    assert os.path.exists(file), "i didn't find file: " + str(file)
    ifc = IfcFile(file)
    from_name = input('Parameter name you want to change: ')
    to_name = input('New name you want to change it to: ')
    ifc.change_parameter_name(from_name, to_name)
    ifc.ifc.write(new_file)



