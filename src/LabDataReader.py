from Types import DataType
from DataReader import DataReader
import xml.etree.ElementTree as ET


class LabDataReader(DataReader):

    def __init__(self) -> None:
        self.key: str = ""
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        mydoc = ET.parse(path)

        root = mydoc.getroot()

        for child in root:
            self.key = child.attrib["name"]
            self.students[self.key] = []
            for i in range(len(child)):
                self.students[self.key].append(
                    (child[i].tag, int(child[i].text))
                )
        return self.students