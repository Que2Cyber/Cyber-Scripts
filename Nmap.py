import subprocess

def scan_range(start_ip, end_ip):
    """
    Scan a range of IP addresses using nmap.

    :param start_ip: The starting IP of the range.
    :param end_ip: The ending IP of the range.
    """
    # Check if nmap is installed
    try:
        subprocess.check_call(['nmap', '-V'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("Error: nmap is not installed. Please install nmap to proceed.")
        return

    # Create a target range for nmap
    target_range = f"{start_ip}-{end_ip.split('.')[-1]}"

    # Define the nmap command. Here we're using a simple ping scan (-sn) as an example.
    # You can modify this command with other nmap options as needed.
    command = ['nmap', '-sn', target_range]

    try:
        result = subprocess.check_output(command).decode('utf-8')
        print(result)
    except subprocess.CalledProcessError as e:
        print(f"Error during scan: {e}")
        return

if __name__ == "__main__":
    start_ip = input("Enter the start IP address (e.g., 192.168.1.1): ")
    end_ip = input("Enter the end IP address (e.g., 192.168.1.255): ")

    scan_range(start_ip, end_ip)
