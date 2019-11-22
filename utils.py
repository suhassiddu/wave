__all__ = ['kw2attr']

def kw2attr(obj, kwargs):
	for key, value in kwargs.items():
		setattr(obj, key, value)