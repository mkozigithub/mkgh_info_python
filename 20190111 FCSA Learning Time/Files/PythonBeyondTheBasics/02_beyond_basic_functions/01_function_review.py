import socket

def resolve(host):
    return socket.gethostbyname(host)

type(resolve)

if __name__ == "__main__":
    print(resolve('sixty-north.com'))