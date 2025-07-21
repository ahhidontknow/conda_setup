# simple script to help me (or anyone really...) set up my anaconda across devices

import subprocess
import re
import os

#general variables
env_dir = (os.getcwd()+"\\env")


# Command to check whether the direct query works // this isn't in-use currently but it should as it'd be better a implementation... cant test it anyway...
command = ["nvidia-smi", "--query-gpu=cuda_version", "--format=csv,noheader"]

# first check whether cuda is available or not

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

print(os.listdir(env_dir))