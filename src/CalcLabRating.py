from Types import DataType
from CalcRating import CalcRating
import math

RatingType = dict[str, float]


class CalcLabRating:

    def __init__(self, data: DataType) -> None:
        self.data: RatingType = data
        self.rating: RatingType = {}

    def calc(self) -> RatingType:
        self.rating = CalcRating(self.data).calc()
        n = math.ceil(len(self.rating) / 4)

        self.rating = dict(sorted
                           (self.rating.items(),
                            reverse=True,
                            key=lambda x: x[1])[:n])
        return self.rating
