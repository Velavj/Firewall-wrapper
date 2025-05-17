
## Usage

### Apply rules
```bash
sudo python3 firewall.py --apply
```

# Apply firewall rules from config
python firewall.py --apply

# List all firewall rules
python firewall.py --list

# Clear/delete all added rules
python firewall.py --clear

## Configuration Format (`rules.json`)
```json
{
  "rules": [
    {
      "name": "AllowSSH",
      "dir": "in",
      "action": "allow",
      "protocol": "TCP",
      "localport": "22",
      "profile": "any",
      "enable": "yes"
    },
    {
      "name": "BlockPing",
      "dir": "in",
      "action": "block",
      "protocol": "ICMPv4",
      "enable": "yes",
      "profile": "any"
    }
  ]
}

```

## License

MIT
