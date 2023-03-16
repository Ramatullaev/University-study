# name =  input("What's your name? ")
# logs = []

log = input()
log_file = open("log_file.txt", 'a')
log_file.write(f"{log}\n")
log_file.close()
print(log_file.closed)



# for _ in range(3):
#     log =  input("What's your name? ")
#     logs.append(log)

# for log in logs:
#     print(f"Hi, {logs}")



