def NULL_not_found(object: any) -> int:

    try:
        match object:
            case str() if object == '':
                print('Empty:', object, type(object))
            case float() if object != object:
                print('Cheese:', object, type(object))
            case bool() if object is False:
                print('Fake:', object, type(object))
            case int() if object == 0:
                print('Zero:', object, type(object))
            case None:
                print('Nothing:', object, type(object))
            case _:
                print('Type not Found')
                return 1
        return 0

    except Exception:
        return 1
