import os
from constants import RULES_FILE

class RulesManager:
    def __init__(self, rules_file=RULES_FILE):
        self.rules_file = rules_file
        self.rules = []

    def load_rules(self):
        self.rules = []
        if not os.path.exists(self.rules_file):
            print(f"[INFO] '{self.rules_file}' not found. Starting with empty rules.")
            return
        with open(self.rules_file, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    self.rules.append(line)

    def save_rules(self):
        with open(self.rules_file, "w") as f:
            for rule in self.rules:
                f.write(rule + "\n")
        print("[✓] Rules saved successfully.")

    def add_rule(self, rule):
        rule = rule.strip().upper()
        if rule in self.rules:
            print("[WARN] Rule already exists.")
            return False
        self.rules.append(rule)
        return True

    def remove_rule(self, index):
        if 0 <= index < len(self.rules):
            removed = self.rules.pop(index)
            print(f"[✓] Removed rule: {removed}")
            return True
        return False
