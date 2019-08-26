def retry(func):
	def retried_function(*args, **kwargs):
		exc = None
		for _ in range(3):
			try:
				return func(*args, **kwargs)
			except Exception as exc:
				print("Exception raised while calling %s with args:%s, kwargs: %s. Retrying" % (func, args, kwargs).
		
		raise exc
	return retried_function

	@retry
	def do_something_risky():
		...

	retried_function = retry(do_something_risky)