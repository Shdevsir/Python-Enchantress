class AttributeInitType(type):
	def __call__(cls, *args, **kwargs):
		obj = type.__call__(cls, *args)
		for name, value in kwargs.items():
			setattr(obj, name, value)
			return obj


class StringGuitar(metaclass=AttributeInitType):
	pass


if __name__ == '__main__':
	strings = StringGuitar(number_of_strings=6)
	print(type(strings))
	print(strings.number_of_strings)
