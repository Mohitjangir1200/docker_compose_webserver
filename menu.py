import os
os.system("tput setaf 3")
print("\n\t\t\t  Welcome TO Web-server TUI\n")
print("\t\t------------------------------------------------")
os.system("tput setaf 7")

print("""choose 1 : To launch wordpress 
choose 2 : To launch Nginx
choose 3 : To launch Ghost""")
print("\n")
print("Enter your choice:")
ch = input()

if ch == '1':
    os.system("docker-compose -f wordpress.yml up")
elif ch == '2':
    os.system("docker-compose -f nginx.yml up")
elif ch == '3':
    os.system("docker-compose -f ghost.yml up")
else:
    print("command failed")
