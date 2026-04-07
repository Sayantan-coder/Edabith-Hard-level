import socket


def get_domain(Ip_Addr: str) -> str:
    try:
        domain_name = socket.gethostbyaddr(Ip_Addr)[0]
        return domain_name
    except socket.herror:
        return "No domain Found"


print(get_domain("127.1.1.1"))
print(get_domain("8.8.8.8"))
print(get_domain("8.8.4.4"))
