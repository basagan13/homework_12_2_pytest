from utils import arrs
from fixture_task import coll


def test_get(coll):
    assert arrs.get(coll, 1, "test") == 2
    assert arrs.get(coll, -4, "test") == "test"
    assert arrs.get([], 0, "test") == "[]"

def test_slice(coll):
    assert arrs.my_slice(coll, 1, 3) == [2, 3]
    assert arrs.my_slice(coll, 1) == [2, 3, 4]
    assert arrs.my_slice(coll, -3, -1) == [2, 3]
    assert arrs.my_slice(coll, -6, -2) == [1, 2]
    assert arrs.my_slice([]) == []