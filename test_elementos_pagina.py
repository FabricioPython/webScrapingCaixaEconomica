import typing
from dataclasses import dataclass



class Coordinate(typing.NamedTuple):
    lat: float
    lon: float

@dataclass
class DemoDataClass:
    a:int
    b: float = 1.1
    c = 'x'



trash = Coordinate('oi', None)
print(trash.__annotations__)

#trash.lat = 10

dc = DemoDataClass(20)
dc.z = 99
print(DemoDataClass.__annotations__)
print(dc.z)
 