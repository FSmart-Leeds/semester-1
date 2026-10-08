# Week 1.2, Session 2: Task 6
temp = int(input("What is the machine's temperature in degrees Celsius?: "))
psi = int(input("What is the machine's PSI?: "))
status = int(input("What is the machine's operational status (1 for operating, 0 for stopped)?: "))
shutdown = 0
output = []

if temp > 80:
    output.append("[Warning]: Machine's temperature is too high. Shutdown recommended.")
    shutdown = 1
elif temp > 50:
    output.append("Machine's temperature is in safe limits.")
else:
    output.append("Machine's temperature is low and no action is needed.")

if psi > 100:
    output.append("[Warning]: High pressure detected. Maintenance recommended.")
    shutdown = 1
elif psi > 70:
    output.append("Pressure is stable.")
else:
    output.append("Pressure is low and the system is operating normally.")

if status == 1 and shutdown == 1:
    output.append("[Warning]: Machine is running in unsafe conditions and shutting down is recommended.")
elif status == 1:
    output.append("Everything is normal.")
else:
    output.append("Machine is stopped and no immediate action is needed.")


with open("machine_log.txt", "w") as file:
    file.write("")
for line in output:
    print(line)
    with open("machine_log.txt", "a") as file:
        file.write(line+"\n")
