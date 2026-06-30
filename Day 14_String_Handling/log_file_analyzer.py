logs = [
    "INFO: Login Successful",
    "ERROR: Payment Failed",
    "INFO: Logout Successful",
    "ERROR: API Timeout"
]

# for log in logs:
#     if log.startswith("ERROR"):
#         print("Issue Found")
#         print(log)
    

error_count = 0
for log in logs:
    if log.startswith("ERROR"):
        print("Issue Found")
        print(log)
        error_count += 1

print("----------")
print("Total Errors:", error_count)