# 🔐 Nmap Network Scanning Script

This Python script utilizes the `nmap` library to perform a network scan on a specified target IP address. It provides detailed information about the target host, including the state of the host, protocols detected, and the status of individual ports.

## 🚀 Features

- **Host Discovery:** Identifies the target host and retrieves its hostname (if available).
- **Service and Version Detection:** Probes open ports to determine the services running and their versions using the `-sV` option.
- **Default Script Execution:** Executes default Nmap scripts using the `-sC` option to gather additional information about the target.
- **Port Scanning:** Lists all detected open ports and their states (e.g., open, closed).

## 📄 Requirements

- Python 3.x
- [python-nmap](https://pypi.org/project/python-nmap/) library

You can install the `python-nmap` library using pip:

```bash
pip install python-nmap
```

## 🛠️ Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/python-password-manager.git
    cd python-password-manager
    ```

2. Run the script:
    ```bash
    python nmap_scanner.py
    ```

3.The script will automatically scan the specified target IP address and print the results.

## 📝 Example Interaction

Host: 45.33.32.156 (example.com)
State: up
Protocol: tcp
Port: 22    State: open
Port: 80    State: open
Port: 443   State: open



## 🧩 How It Works

1. The script initializes an nmap.PortScanner() object.
2. The target IP address and scan options are defined.
3. The script runs the Nmap scan using the specified options (-sV -sC).
4. For each detected host, the script outputs the host's state, the protocols detected, and the status of each port.

⚠️ Disclaimer
This script is intended for educational purposes only. Unauthorized scanning of networks without explicit permission is illegal and unethical. Always ensure you have permission from the target before performing any scans.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

This `README.md` is designed to be both informative and visually appealing.


## 💡 Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/python-password-manager/issues) or submit a pull request.

---

Made with ❤️ by [George Raymond]([https://github.com/your-username](https://github.com/GeorgeRaymond98))
