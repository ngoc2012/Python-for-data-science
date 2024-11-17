def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None", type(object))
        return 0
    elif isinstance(object, float) and object != object:
        print("Cheese: nan", type(object))
        return 0
    elif isinstance(object, bool) and object is False:
        print("Fake: False", type(object))
        return 0
    elif isinstance(object, int) and object == 0:
        print("Zero: 0", type(object))
        return 0
    elif isinstance(object, str) and len(object) == 0:
        print("Empty:", type(object))
        return 0
    print("Type not Found")
    return 1
