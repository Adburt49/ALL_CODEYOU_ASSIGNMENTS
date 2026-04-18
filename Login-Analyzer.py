Username = input("Enter username: ")
critical_user = input("Is this a privileged user? (yes/no): ")

failed_logins = int(input("Enter number of failed login attempts: "))

if failed_logins >= 5 and critical_user.lower() == "yes":
   print("[*]CRITICAL ALERT: Privileged account under attack!")
elif failed_logins > 0:
   print("[-] NOTICE: Some failed logins ob.")
else:
  print("[+] No failed logins recorded.")

print("\n=== Login Attempt Summary===")
print(f"Username: {Username}")
print(f"failed_attempts: {failed_logins}")
print(f"Privileged Account: {critical_user}")
print("Analyst Name: [April Burton]")

=== Login Attempt Summary===
Username: "Jordan"
failed_attempts: 9
Privileged Account: yes
Analyst Name: [April Burton]

