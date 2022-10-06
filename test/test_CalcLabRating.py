# -*- coding: utf-8 -*-
from src.Types import DataType
from src.CalcLabRating import CalcLabRating
import pytest

RatingsType = dict[str, float]


class TestCalcRating:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingsType]:
        data: DataType = {
            "Иванов Иван Иванович":
            [
                ('математика', 100),
                ('литература', 100),
                ('программирование', 100)
            ],

            "Петров Петр Петрович":
            [
                ('математика', 78),
                ('химия', 87),
                ('социология', 61)
            ],
            "Меладзе Валерий Шотаевич":
            [
                ('математика', 62),
                ('химия', 54),
                ('социология', 34)
            ],
            "Андреев Андрей Андреевич":
            [
                ('математика', 61),
                ('химия', 26),
                ('социология', 86)
            ],
            "Леонидов Леонид Леонидович":
            [
                ('математика', 56),
                ('химия', 96),
                ('социология', 99)
            ],
            "Даниилов Даниил Даниилович":
            [
                ('математика', 100),
                ('химия', 100),
                ('социология', 100)
            ],
            "Дмитриев Дмитрий Дмитриевич":
            [
                ('математика', 54),
                ('химия', 88),
                ('социология', 43)
            ],
            "Артёмов Артём Артёмович":
            [
                ('математика', 96),
                ('химия', 87),
                ('социология', 62)
            ]
        }

        rating_scores: RatingsType = {
            "Даниилов Даниил Даниилович": 100.000,
            "Иванов Иван Иванович": 100.0000
        }

        return data, rating_scores

    def test_init_calc_rating(self, input_data: tuple[DataType,
                                                      RatingsType]) -> None:

        calc_rating = CalcLabRating(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(self, input_data: tuple[DataType, RatingsType]) -> None:

        rating = CalcLabRating(input_data[0]).calc()
        for student in rating.keys():
            rating_score = rating[student]
            assert pytest.approx(rating_score,
                                 abs=0.001) == input_data[1][student]
