
def all_thing_is_obj(object: any) -> int:
	#your code here
	t = type(object)
	obj = {
		list: "List",
		tuple: "Tuple",
		set: "Set",
		dict: "Dict",
	}

	if t in obj:
		print(f"{obj[t]} : {t}")
	elif t is str:
		print(f"{object} is in the kitchen : {t}")
	else:
		print("Type not found")

	return 42
