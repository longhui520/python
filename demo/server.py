from wsgiref.simple_server  import make_server
from hellow import application
httpd = make_server('',8000,application)
print('Serving HTTTP on port 8000')
httpd.serve_forever()