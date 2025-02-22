def NULL_not_found(object: any) -> int:

	type_map = {
		list: "List",
		tuple: "Tuple",
		set: "Set",
		dict: "Dict"
	}

	try :
		match object:
			case str():
				print
	
	except Exception as e:
		print (e)
	print (type(object))
	print (object)
	return 1