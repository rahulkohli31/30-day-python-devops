server_name = input("Enter server name: ")
cpu_usage = input("Enter cpu usage: ")
memory_usage = input("Enter memory usage: ")
system_status = input("Enter system status: ")

print(f"Server Name: {server_name}")
print(f"CPU Usage: {cpu_usage}%")
print(f"Memory Usage: {memory_usage}%")
print(f"System Status: {system_status}")

info = [server_name, cpu_usage, memory_usage, system_status]
for data_type in info:
    print(type(data_type))