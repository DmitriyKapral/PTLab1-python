# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.LabDataReader import LabDataReader


class TestLabDataReader:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = '''<?xml version="1.0" encoding="UTF-8" ?>\n''' + \
            '''<root>\n''' + \
            '''<fio name="Иванов Иван Иванович">\n''' + \
            '''<математика>67</математика>\n''' + \
            '''<музыка>100</музыка>''' + \
            '''<химия>91</химия>\n''' + \
            '''</fio>\n''' + \
            '''<fio name="Петров Петр Петрович">\n''' + \
            '''<математика>78</математика>\n''' + \
            '''<химия>87</химия>\n''' + \
            '''<социология>61</социология>\n''' + \
            '''</fio>\n''' + \
            '''</root>'''

        data = {
            "Иванов Иван Иванович": [
                ("математика", 67), ("музыка", 100), ("химия", 91)
            ],
            "Петров Петр Петрович": [
                ("математика", 78), ("химия", 87), ("социология", 61)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.txt")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = LabDataReader().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
