from netR import netR

def handler(req, res):
    res.write('Hello World')
    res.end()

server = netR.http_server()
server.add(handler)
server.listen(port=5000)