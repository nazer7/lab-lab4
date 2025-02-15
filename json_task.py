import json
with open("data.json", "r") as file:
    data = json.load(file)
print("Interface Status")
print("="*80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<10} {'MTU':<10}")
print(f"{"-"*50:<50} {"-"*20:<20} {"-"*6:<10} {"-"*6:<10}")
for index, item in enumerate(data["imdata"]):
    if index >=3:  
        break  
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr")  
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(f"{dn:<50} {description:<20} {speed:<10} {mtu:<10}")
