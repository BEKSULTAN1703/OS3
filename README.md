Student: Beksultan Kulybekov; Group: SE-2223
Script Overview:
This Python script is designed to provide a comprehensive overview of various critical system parameters on a Windows machine. It harnesses native Windows management tools via command-line interfaces and integrates Python's powerful subprocess module to execute and fetch system information. This script is particularly useful for system administrators, developers, or tech enthusiasts who need a quick overview of system configurations without navigating through multiple system windows.

Function Details:
get_os_info(): This function uses the platform module to fetch the operating system type and its release version. This is useful for quickly determining the environment in which the script is running, which can be critical for deploying software that depends on specific OS characteristics.
get_cpu_info(): Retrieves details about the CPU, such as its identifier, which includes the brand and model of the processor. This information is crucial for performance analysis or when specifying system requirements for applications.
get_memory_info(): Executes a WMIC (Windows Management Instrumentation Command-line) command to obtain the total physical memory (RAM) installed in the system, expressed in gigabytes. This is vital for assessing the capability of the system to handle certain workloads or software applications, especially those that are memory-intensive.
get_disk_info(): Also utilizes WMIC to fetch detailed information about the logical disks on the system, specifically the disk size and available free space. This function provides a snapshot of storage utilization, which is essential for managing disk space, especially in environments where data is frequently processed or stored.
get_current_user(): Uses the os module to determine the username of the user currently logged into the system. This information might be used in scripts that need to tailor their operations or outputs to the current user, or for logging and monitoring user activities.
get_ip_address(): Determines the system’s IP address using the socket module by resolving the hostname to an IP address. This information can be crucial for network configuration, troubleshooting, and ensuring the system is accessible on the network.
get_system_uptime(): Tries to determine how long the system has been running since its last startup. This function can be particularly useful in monitoring environments or in applications where system reliability or uptime guarantees are crucial. It handles potential Unicode decoding errors and other exceptions to ensure robust uptime reporting.
Exception Handling:
The script includes error handling to address various issues that may occur during the execution of external commands or the processing of their outputs. For instance, it gracefully handles subprocess exceptions, such as CalledProcessError and UnicodeDecodeError, ensuring that the script can inform the user of the specific issue without crashing.

Usage:
To run the script, simply execute it from the command line or through an IDE that supports Python. The script outputs formatted strings for each piece of information, making it easy to read and understand at a glance.

Conclusion:
This script offers a straightforward way to fetch and display essential system information, which can aid in system diagnostics, monitoring, and maintenance tasks. Its modular design and clear error handling make it a reliable tool for anyone needing quick access to system details in a Windows environment.
