def NULL_not_found(object: any) -> int:
    """ Find the type of the object """
    if object is None:
        print("Nothing: None", type(object))
        return 0
    if isinstance(object, float) and object != object:
        print("Cheese: nan", type(object))
        return 0
    if isinstance(object, bool) and object is False:
        print("Fake: False", type(object))
        return 0
    if isinstance(object, int) and object == 0:
        print("Zero: 0", type(object))
        return 0
    if isinstance(object, str) and len(object) == 0:
        print("Empty:", type(object))
        return 0
    print("Type not Found")
    return 1
