from deephaven_server import Server
s = Server(port=3000, jvm_args=["-Xmx4g"])
s.start()
