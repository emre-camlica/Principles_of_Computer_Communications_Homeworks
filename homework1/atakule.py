import subprocess

# Define the target host (domain name or IP address)
target_host = "atakule.com.tr"

# Define the maximum number of hops (adjust as needed)
max_hops = 30

with open("atakule.txt", "a") as file:
    file.write("\n")

for i in range(100):
    # Create a subprocess to run tracert
    traceroute_process = subprocess.Popen(["tracert", "-h", str(max_hops), target_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Create a list to store the lines you want to write to the file
    lines_to_write = []

    # Monitor the output of tracert
    for line in traceroute_process.stdout:
        lines_to_write.append(line.strip())
        print(line.strip())

    # Wait for the traceroute process to complete
    traceroute_process.wait()

    # Check if we have at least 3 lines before "Traceroute completed."
    if len(lines_to_write) >= 3:
        # Write the third line before "Traceroute completed" to a file
        with open("atakule.txt", "a") as file:
            file.write(lines_to_write[-3])  # The third line before "Traceroute completed."
            file.write("\n")