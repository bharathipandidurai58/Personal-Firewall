import socket

# Read blocked websites
with open("rules.txt", "r") as file:
    blocked = [line.strip().lower() for line in file]

print("=" * 40)
print("Personal Firewall Simulation")
print("=" * 40)

while True:
    website = input("\nEnter website (or type exit): ").lower()

    if website == "exit":
        print("Firewall Closed.")
        break

    if website in blocked:
        print("❌ Access Blocked!")
    else:
        try:
            ip = socket.gethostbyname(website)
            print("✅ Access Allowed")
            print("IP Address:", ip)
        except:
            print("Website not found.")