def make_adder(addend):
	def adder(augend):
		return augend + addend
	return adder
	
add4 = make_adder(4)
add100 = make_adder(100)

print add4(6)
print add100(88)