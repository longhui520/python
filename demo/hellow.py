def application(environ,start_response):
    start_response('200 ok',[('Content-type','text/html')])
    return [b'<h1>Hello,web!</h1>']
    