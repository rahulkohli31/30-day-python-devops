service_running = True
maintenance_mode = False
backup_in_progess = False

system_available = service_running and not maintenance_mode
print(f"System Available: {system_available}")