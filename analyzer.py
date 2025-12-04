from collections import defaultdict

class Analyzer:
    @staticmethod
    def parse_rule(rule):
        parts = rule.split()
        if len(parts) != 3:
            return None
        action, protocol, port = parts
        if action not in ("ALLOW", "DENY") or protocol not in ("TCP", "UDP") or not port.isdigit():
            return None
        return {"action": action, "protocol": protocol, "port": int(port)}

    @staticmethod
    def analyze(rules):
        duplicates = []
        conflicts = []
        open_ports = defaultdict(list)
        parsed_rules = []

        for r in rules:
            parsed = Analyzer.parse_rule(r)
            if parsed:
                parsed_rules.append(parsed)

        seen = set()
        for r in parsed_rules:
            key = (r["protocol"], r["port"])
            if key in seen:
                duplicates.append(r)
            else:
                seen.add(key)
            if r["action"] == "ALLOW":
                open_ports[r["protocol"]].append(r["port"])

        for i in range(len(parsed_rules)):
            for j in range(i + 1, len(parsed_rules)):
                r1, r2 = parsed_rules[i], parsed_rules[j]
                if (
                    r1["protocol"] == r2["protocol"]
                    and r1["port"] == r2["port"]
                    and r1["action"] != r2["action"]
                ):
                    conflicts.append((r1, r2))

        return duplicates, conflicts, open_ports
