# simple script to help me (or anyone really...) set up anaconda across devices

import subprocess
import re
import os

###############################################################################
# some prerequisites
###############################################################################

# general variables
env_dir = (os.getcwd()+"\\env")  # to get 

# Command to check whether the direct query works
# this currently isn't used but it should as it'd be better implemented...
# cant test it anyway...
command = ["nvidia-smi", "--query-gpu=cuda_version", "--format=csv,noheader"]
cuda_available = False


# some functions
# Let people decide what to install
def user_select(possible_envs):
    confirmation = False

    while user_selection != True:
        print(f"The following environments can be set up:\n{possible_envs}")
        # select what to install
        selected_envs = input("Please select the desired environments:\n")
        print(f"{selected_envs} have been selected.")
        # confirm before setup  //seems like a reasonable thing to do...
        confirmation = input("Do you want to set up these environments? (y | n)\n")
        # Inerpret input
        if confirmation == 'y':
            confirmation = True
            return selected_envs  # return selection
        else:
            # restart
            print("Selection aborted restart selection")


###############################################################################
# Start the actual setup
###############################################################################

# check if nvidia is installed properly and has CUDA-support
try:
    result = subprocess.run("nvidia-smi",
                            capture_output=True,
                            text=True,
                            check=True)

    # Use regular expressions to find the CUDA version in the output
    match = re.search(r"CUDA Version:\s*([\d\.]+)", result.stdout)

    if match:
        cuda_available = True
        cuda_version = match.group(1)
        print(f"Successfully found CUDA version: {cuda_version}")
    else:
        print("Could not find CUDA version in nvidia-smi output.")

except (subprocess.CalledProcessError, FileNotFoundError) as e:
    print(f"An error occurred when running nvidia-smi: {e}")
    print("Try updating your NVIDIA drivers or check if your GPU is installed correctly")
    print("If you aren't using a NVIDIA you can ignore this error.")


# Select install environments
user_selection = False

if cuda_available:
    all_env = (os.listdir(env_dir))
    print(user_select(all_env))




# this is down here since there might not be a need for this package
# to configure yaml-files to get the correct CUDA-ersion
# import yaml