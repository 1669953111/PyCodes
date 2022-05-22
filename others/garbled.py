import random.sample
import string

def get_garbled():
	return ''.join(random.sample(string.ascii_letters + string.digits + string.punctuation, 32))

print(get_garbled())
