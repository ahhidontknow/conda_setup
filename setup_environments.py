import subprocess
import re


command = ["nvidia-smi", "--query-gpu=cuda_version", "--format=csv,noheader"]

# first check whether cuda is available

try:
    result = subprocess.run("nvidia-smi", capture_output=True, text=True, check=True)
    
    # Use regular expressions to find the CUDA version in the output
    match = re.search(r"CUDA Version:\s*([\d\.]+)", result.stdout)
    
    if match:
        cuda_version = match.group(1)
        print(f"Successfully found CUDA version: {cuda_version}")
    else:
        print("Could not find CUDA version in nvidia-smi output.")

except (subprocess.CalledProcessError, FileNotFoundError) as e:
    print(f"An error occurred: {e}")

print(cuda_version)