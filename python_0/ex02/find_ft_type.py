def all_thing_is_obj(object: any) -> int:

	type_map = {
		list: "List",
		tuple: "Tuple",
		set: "Set",
		dict: "Dict"
	}

	if isinstance(object, str) :
		print(object + " is in the kitchen : " + str(type(object)))
	elif type(object) in type_map:
		print(type_map.get(type(object)), ":", type(object))
	else :
		print("Type not found")
	return 42

