from area import circle as c
from area import rect as r
from area.sec_pack import cuboid as cu
from area.sec_pack import sphere as s
print("area of circle:", c.area(2))
print("perimeter of circle:", c.peri(2))
print("area of rect:", r.area(2, 2))
print("perimeter of rect:", r.peri(2, 2))
print("area of cuboid:", cu.area(2, 2, 2))
print("perimeter of cuboid:", cu.peri(2, 2, 2))
print("area of sphere:", s.area(2))
print("perimeter of sphere:", s.peri(2))