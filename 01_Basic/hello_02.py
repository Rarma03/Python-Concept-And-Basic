#  perfom auto updation if imported file changed
from importlib import reload

from hello import print_words

# reload('hello') -> in local env we dont need it, we used it in shell 

print_words("We are using the funtion defined in other location")