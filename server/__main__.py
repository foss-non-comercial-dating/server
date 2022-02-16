import sys

from server import Server

if __name__ == "__main__":
    serverobj = Server(sys.argv)
    serverobj.run()
