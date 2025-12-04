# main.py

from rules_manager import RulesManager
from analyzer import Analyzer

TOOL_NAME = "Firewall Analyzer Tool v1"
AUTHOR = "LordAbdulla"

def main():
    print(f"\n=== {TOOL_NAME} ===")
    print(f"Author: {AUTHOR}\n")
    
    manager = RulesManager()
    manager.load_rules()

    while True:
        print("\n=== Firewall Analyzer Menu ===")
        print("1. List rules")
        print("2. Add rule")
        print("3. Remove rule")
        print("4. Analyze rules")
        print("5. Save and exit")
        print("6. Exit without saving")

        choice = input("> ").strip()

        if choice == "1":
            if not manager.rules:
                print("[INFO] No rules found.")
            else:
                print("\n--- Current Firewall Rules ---")
                for idx, rule in enumerate(manager.rules, 1):
                    print(f"{idx}. {rule}")
                print("------------------------------")
        elif choice == "2":
            rule = input("Enter rule (ALLOW/DENY TCP/UDP PORT): ").strip()
            if manager.add_rule(rule):
                print("[✓] Rule added.")
            else:
                print("[ERROR] Could not add rule.")
        elif choice == "3":
            for idx, rule in enumerate(manager.rules, 1):
                print(f"{idx}. {rule}")
            try:
                idx = int(input("Enter rule number to remove: "))
                if not manager.remove_rule(idx - 1):
                    print("[ERROR] Invalid rule number.")
            except ValueError:
                print("[ERROR] Please enter a valid number.")
        elif choice == "4":
            duplicates, conflicts, open_ports = Analyzer.analyze(manager.rules)
            print("\n--- Firewall Analysis ---")
            if duplicates:
                print("[!] Duplicates:")
                for d in duplicates:
                    print(f"  {d}")
            else:
                print("[✓] No duplicates.")

            if conflicts:
                print("[!] Conflicts:")
                for c1, c2 in conflicts:
                    print(f"  {c1} <--> {c2}")
            else:
                print("[✓] No conflicts.")

            print("\n[INFO] Open Ports:")
            for proto, ports in open_ports.items():
                print(f"  {proto}: {', '.join(map(str, ports))}")
            print("-------------------------")
        elif choice == "5":
            manager.save_rules()
            break
        elif choice == "6":
            print("[INFO] Exiting without saving.")
            break
        else:
            print("[ERROR] Invalid option. Choose 1-6.")

if __name__ == "__main__":
    main()
