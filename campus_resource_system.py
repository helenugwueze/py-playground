resources = [
    {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
    {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
    {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3},
]
fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_records = []

def find_resource(rid):
    return next((r for r in resources if r["id"].casefold() == rid.strip().casefold()), None)


def read_quantity(prompt):
    try:
        q = int(input(prompt))
        if q > 0:
            return q
    except ValueError:
        pass
    print("Error: quantity must be a positive integer.")
    return None


def borrow_resource(fid=None, rid=None, quantity=None):
    fid = (input("Fellow ID: ") if fid is None else fid).strip().upper()
    if fid not in fellows:
        print(f"Error: fellow ID {fid!r} was not found.")
        return False
    rid = (input("Resource ID: ") if rid is None else rid).strip().upper()
    r = find_resource(rid)
    if not r:
        print(f"Error: resource ID {rid!r} was not found.")
        return False
    if quantity is None:
        quantity = read_quantity("Quantity to borrow: ")
    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
        if quantity is not None: print("Error: quantity must be a positive integer.")
        return False
    if quantity > r["available"]:
        print(f"Rejected: only {r['available']} unit(s) of {r['name']} are available.")
        return False
    r["available"] -= quantity
    borrow_records.append({"fellow_id": fid, "resource_id": r["id"],
                           "quantity": quantity, "outstanding": quantity})
    print(f"Success: {fellows[fid]} borrowed {quantity} {r['name']}(s). Available now: {r['available']}.")
    return True


def return_resource(fid=None, rid=None, quantity=None):
    fid = (input("Fellow ID: ") if fid is None else fid).strip().upper()
    if fid not in fellows:
        print(f"Error: fellow ID {fid!r} was not found.")
        return False
    rid = (input("Resource ID: ") if rid is None else rid).strip().upper()
    r = find_resource(rid)
    if not r:
        print(f"Error: resource ID {rid!r} was not found.")
        return False
    if quantity is None:
        quantity = read_quantity("Quantity to return: ")
    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
        if quantity is not None:
            print("Error: quantity must be a positive integer.")
        return False
    records = [x for x in borrow_records if x["fellow_id"] == fid and x["resource_id"] == r["id"] and x["outstanding"] > 0]
    owed = sum(x["outstanding"] for x in records)
    if quantity > owed:
        print(f"Rejected: {fellows[fid]} has only {owed} {r['name']}(s) outstanding on loan.")
        return False
    left = quantity
    for record in records:
        amount = min(record["outstanding"], left)
        record["outstanding"] -= amount
        left -= amount
        if left == 0: break
    r["available"] += quantity
    print(f"Success: {fellows[fid]} returned {quantity} {r['name']}(s). Available now: {r['available']}.")
    return True


def list_resources():
    for r in resources:
        print(f"{r['id']} | {r['name']} | {r['category']} | total {r['total']} | available {r['available']}")


def add_resource():
    rid = input("Resource ID: ").strip().upper()
    if not rid or find_resource(rid):
        print("Error: ID is empty or already exists.")
        return
    name, category = input("Name: ").strip(), input("Category: ").strip()
    total = read_quantity("Total units: ")
    if not name or not category or total is None:
        print("Error: name, category and positive total are required.")
        return
    resources.append({"id": rid, "name": name, "category": category,
                      "total": total, "available": total})
    print(f"Added {name} ({rid}) with {total} unit(s).")


def search_resources(term=None):
    term = input("Enter resource name to search: ") if term is None else term
    matches = [r for r in resources if term.strip().casefold() in r["name"].casefold()]
    if not matches:
        print("No resources matched that name.")
    for r in matches:
        print(f"Found: {r['name']} ({r['id']})")


def filter_by_category():
    category = input("Enter category: ").strip().casefold()
    matches = [r for r in resources if r["category"].casefold() == category]
    if not matches:
        print("No resources found in that category.")
    for r in matches: print(f"{r['id']} | {r['name']} | {r['category']} | available {r['available']}/{r['total']}")


def generate_report():
    total = sum(r["total"] for r in resources)
    available = sum(r["available"] for r in resources)
    print("\nCAMPUS RESOURCE REPORT")
    print(f"Total units: {total}")
    print(f"Available units: {available}")
    print(f"Units currently borrowed: {total - available}")
    low = [r for r in resources if r["available"] < 3]
    print("Resources with fewer than 3 available units:")
    for r in low: print(f"  {r['name']} ({r['id']}): {r['available']} available")
    if not low: print("  None")
    borrowed = {r["id"]: r["total"] - r["available"] for r in resources}
    if resources:
        highest = max(borrowed.values())
        leaders = [r["name"] for r in resources if borrowed[r["id"]] == highest]
        print("Most borrowed resource(s): " + ", ".join(f"{name} ({highest})" for name in leaders)
              + " unit(s) currently borrowed")
    else:
        print("Most borrowed resource: None")


def demonstration():
    print("\n=== REQUIRED DEMONSTRATION ===")
    print("\n1. F001 borrows 2 laptops")
    borrow_resource("F001", "R001", 2)
    print(f"Available laptop units = {find_resource('R001')['available']}")
    print("\n2. F002 borrows 3 keyboards")
    borrow_resource("F002", "R002", 3)
    print(f"Available keyboard units = {find_resource('R002')['available']}")
    print("\n3. F001 returns 1 laptop")
    return_resource("F001", "R001", 1)
    print(f"Available laptop units = {find_resource('R001')['available']}")
    print("\n4. F003 requests 4 headsets")
    before = find_resource("R003")["available"]
    borrow_resource("F003", "R003", 4)
    print(f"Headset stock unchanged = {find_resource('R003')['available'] == before}")
    print("\n5. F002 tries to return 4 keyboards")
    before = find_resource("R002")["available"]
    return_resource("F002", "R002", 4)
    print(f"Keyboard stock unchanged = {find_resource('R002')['available'] == before}")
    print("\n6. Search for LAPtop (case-insensitive)")
    search_resources("LAPtop")
    print("\n7. Generate report")
    generate_report()
    print("\n=== END OF REQUIRED DEMONSTRATION ===")


def main():
    while True:
        print("\n=== LEARN2EARN CAMPUS RESOURCE MANAGEMENT ===")
        print("1. Add resource\n2. List resources\n3. Borrow resource\n4. Return resource")
        print("5. Search by name\n6. Filter by category\n7. Generate report")
        print("8. List fellows\n9. Run required demonstration\n0. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_resource()
        elif choice == "2":
            list_resources()
        elif choice == "3":
            borrow_resource()
        elif choice == "4":
            return_resource()
        elif choice == "5":
            search_resources()
        elif choice == "6":
            filter_by_category()
        elif choice == "7":
            generate_report()
        elif choice == "8":
            print("\nREGISTERED FELLOWS")
            for fid, name in fellows.items(): print(f"{fid}: {name}")
        elif choice == "9":
            demonstration()
        elif choice == "0":
            print("Goodbye. Thank you for using the system.")
            break
        else:
            print("Error: choose a menu option from 0 to 9.")


if __name__ == "__main__":
    main()
