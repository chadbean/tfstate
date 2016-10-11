develop:
	@python vstrap.py

test:
	@. quickactivate && unit2 discover . "*_tests.py"
