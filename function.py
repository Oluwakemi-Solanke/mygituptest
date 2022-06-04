def sandwish_order(*sandwishes):
	""" Making a summary of sandwish orders. """
	print('\n The following items have been requested to be in their sandwishes:')
	for sandwish in sandwishes:
		print('-' + sandwish)
sandwish_order('shawama','eggroll',"wallnut")
sandwish_order('wallnut',"pizza")