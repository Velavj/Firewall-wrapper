#!/usr/bin/env python3
import os
import subprocess
import json
import argparse

CONFIG_FILE = "rules.json"

def apply_rule(rule):
    try:
        cmd = ["netsh", "advfirewall", "firewall", "add", "rule"]
        for key, value in rule.items():
            cmd.append(f"{key}={value}")
        subprocess.run(cmd, check=True)
        print(f"Applied rule: {' '.join(cmd)}")
    except Exception as e:
        print(f"Failed to apply rule {rule}: {e}")

def apply_rules_from_config(config_path=CONFIG_FILE):
    if not os.path.exists(config_path):
        print("Configuration file not found.")
        return
    with open(config_path, 'r') as file:
        rules = json.load(file)
        for rule in rules.get("rules", []):
            apply_rule(rule)

def list_rules():
    subprocess.run(["netsh", "advfirewall", "firewall", "show", "rule", "name=all"])

def clear_rules():
    subprocess.run(["netsh", "advfirewall", "firewall", "delete", "rule", "name=all"])
    print("All firewall rules deleted.")

def main():
    parser = argparse.ArgumentParser(description="Simple Windows Firewall wrapper using netsh")
    parser.add_argument("--apply", action="store_true", help="Apply rules from configuration file")
    parser.add_argument("--list", action="store_true", help="List current firewall rules")
    parser.add_argument("--clear", action="store_true", help="Delete all user-added firewall rules")
    parser.add_argument("--config", type=str, help="Specify a custom config file")
    args = parser.parse_args()

    if args.clear:
        clear_rules()
    if args.list:
        list_rules()
    if args.apply:
        apply_rules_from_config(args.config if args.config else CONFIG_FILE)

if __name__ == "__main__":
    main()
