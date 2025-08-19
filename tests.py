from functions.get_files_info import get_files_info


result = get_files_info("calculator", ".")
print("Results for current directory:")
print(result)

result = get_files_info("calculator", "pkg")
print("Results for 'pkg' directory:")
print(result)

result = get_files_info("calculator", "/bin")
print("Results for '/bin' directory:")
print(result)

result = get_files_info("calculator", "../")
print("Results for '../' directory:")
print(result)
