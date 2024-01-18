import socket

def check_node_if_live(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, port))
        s.shutdown(2)
        return True
    except:
        return False
    
if __name__ == "__main__":
    ip = "8.8.8.8"
    port = 80
    print(check_node_if_live(ip, port))
