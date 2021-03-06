from p146 import LRUCache, LRUCacheV2

test_cases = [
    ((["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"], [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]), [None, None, None, 1, None, -1, None, -1, 3, 4])
]

def runCase(cls, actions, params):
    instacne = None
    rst = []
    for act, param in zip(actions, params):
        if act == "LRUCache":
            instacne = cls(*param)
            rst.append(None)
            continue
        if not instacne:
            rst.append(None)
            continue
        if act == "put":
            instacne.put(*param)
            rst.append(None)
        else:
            rst.append(instacne.get(*param))

    return rst


def test_LRUCache():
    for case in test_cases:
        assert runCase(LRUCache, *case[0]) == case[1], case

def test_LRUCacheV2():
    for case in test_cases:
        assert runCase(LRUCacheV2, *case[0]) == case[1], case
