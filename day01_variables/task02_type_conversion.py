port_str = input("Enter port number: ")

try:
    port_int = int(port_str)
    print(f"Port as interger: {port_int}")

except ValueError:
    print("Invalid port number - Using default 8080")
    port_int = 8080