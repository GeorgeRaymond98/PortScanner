# You will need permission to scann their port
import nmap  # Import the nmap module for network scanning

# Initialize the PortScanner object from the nmap module
nm = nmap.PortScanner()

# Define the target IP address to scan
target = "45.33.32.156"

# Define the scan options: 
# -sV: Probe open ports to determine service/version info
# -sC: Equivalent to --script=default (runs default scripts)
options = "-sV -sC"

# Run the scan on the target IP address with the specified options
nm.scan(target, arguments=options)

# Iterate through all detected hosts (there should only be one in this case)
for host in nm.all_hosts():
    # Print the host IP and its hostname (if available)
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    
    # Print the state of the host (e.g., 'up' or 'down')
    print("State: %s" % nm[host].state())
    
    # Iterate through all protocols detected on the host (e.g., 'tcp', 'udp')
    for protocol in nm[host].all_protocols():
        # Print the protocol being examined
        print("Protocol: %s" % protocol)
        
        # Get information about the ports associated with the protocol
        port_info = nm[host][protocol]
        
        # Iterate through each port and its corresponding state
        for port, state in port_info.items():
            # Print the port number and its state (e.g., 'open', 'closed')
            print("Port: %s\tState: %s" % (port, state))
