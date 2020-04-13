from LRUCache import LRUCache

def main():
    test = LRUCache(3)
    test.put(1, "Hyderabad")
    test.put(2, "Delhi")
    test.put(3, "Mumbai")
    assert test.cache_dict == {1: "Hyderabad", 2: "Delhi", 3: "Mumbai"}
    print("Put test case passed")
    assert test.get(2) == "Delhi"
    print("Get test case passed")
    assert test.cache_dict == {1: "Hyderabad", 3: "Mumbai", 2: "Delhi"}
    print("After get dictionary is correct")
    test.put(4,"Bangalore")
    assert test.cache_dict == {3: "Mumbai", 2: "Delhi", 4: "Bangalore"}
    print("put after cache exceed passed")
    test.put(3, "Hyderabad")
    assert test.cache_dict == {3: "Hyderabad", 2: "Delhi", 4: "Bangalore"}
    print("LRU Success")

if __name__ == "__main__":
    main()