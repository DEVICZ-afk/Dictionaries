robots = {
    "Antonín": "Úklid",
    "Boris": "Opravy",
    "Cyril": "Vaření",
    "David": "Údržba",
    "Eva": "Zahradničení",
}

while True:
    robot_name = input("Zadejte jméno robota (nebo 'konec' pro ukončení): ").strip()
    
    if robot_name.lower() == "konec":
        break
    
    if robot_name in robots:
        print(f"Robot {robot_name} má funkci: {robots[robot_name]}")
    else:
        add_function = input(f"Robot {robot_name} neexistuje. Zadejte jeho funkci: ").strip()
        robots[robot_name] = add_function
        print(f"Robot {robot_name} byl přidán s funkcí: {add_function}")
print("\nSeznam všech robotů a jejich funkcí:")
for name, function in robots.items():
    print(f"- {name}: {function}")