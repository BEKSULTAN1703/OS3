import os
import platform
import socket
import subprocess
import re


def get_os_info():
    """
    Retrieves the operating system type and its release version.

    Returns:
        str: A formatted string with OS name and version.
    """
    return f"OS Name: {platform.system()}, Version: {platform.release()}"


def get_cpu_info():
    """
    Retrieves information about the system's CPU, such as the processor type.

    Returns:
        str: A formatted string with processor information.
    """
    return f"Processor: {platform.processor()}"


def get_memory_info():
    """
    Uses WMIC command to fetch the total physical memory installed in the system.

    Returns:
        str: A formatted string displaying the total memory in gigabytes.
    """
    command = "wmic ComputerSystem get TotalPhysicalMemory"
    total_memory = subprocess.check_output(command, shell=True).decode().split("\n")[1].strip()
    total_memory = round(int(total_memory) / (1024 ** 3), 2)
    return f"Total Memory: {total_memory} GB"


def get_disk_info():
    """
    Uses WMIC command to get information about disk size and free space from logical disks.

    Returns:
        str: A formatted string showing the size and available space of the disk in gigabytes.
    """
    command = "wmic LogicalDisk where DriveType=3 get Size, FreeSpace"
    disk_info = subprocess.check_output(command, shell=True).decode().split("\n")[1].strip().split()
    free_space_gb = round(int(disk_info[1]) / (1024 ** 3), 2)
    disk_size_gb = round(int(disk_info[0]) / (1024 ** 3), 2)
    return f"Disk Size: {disk_size_gb} GB, Available Disk Space: {free_space_gb} GB"


def get_current_user():
    """
    Retrieves the username of the current user logged into the operating system.

    Returns:
        str: The current user's login name.
    """
    return f"Current User: {os.getlogin()}"


def get_ip_address():
    """
    Retrieves the IP address of the system based on the hostname.

    Returns:
        str: The IP address of the system.
    """
    hostname = socket.gethostname()
    return f"IP Address: {socket.gethostbyname(hostname)}"


def get_system_uptime():
    """
    Retrieves the system uptime by using the 'systeminfo' command in Windows. It handles different
    encoding scenarios and possible exceptions during execution.

    Returns:
        str: Formatted string representing system uptime or an error message.
    """
    if platform.system() == "Windows":
        try:
            encoding = subprocess.check_output('chcp', shell=True).decode().split(':')[-1].strip()
            uptime_info = subprocess.check_output('systeminfo', shell=True).decode(encoding)
            uptime = re.search(r'System Boot Time: (.*)', uptime_info).group(1).strip()
            return f"System Uptime: {uptime}"
        except subprocess.CalledProcessError as e:
            return f"An error occurred while trying to get system uptime: {e}"
        except UnicodeDecodeError as e:
            return "Error decoding system information. Please check system encoding."
    else:
        return "System Uptime: Not available on non-Windows systems without additional modules"


def display_system_info():
    """
    Displays all collected system information by calling other functions and printing their outputs.
    """
    print(get_os_info())
    print(get_cpu_info())
    print(get_memory_info())
    print(get_disk_info())
    print(get_current_user())
    print(get_ip_address())
    print(get_system_uptime())


if __name__ == "__main__":
    display_system_info()
