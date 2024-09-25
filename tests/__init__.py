import sys
import os

# Get the absolute path of the current script
current_script_path = os.path.abspath(__file__)

# Get the directory containing the script (root folder of the project)
root_folder = os.path.dirname(current_script_path)

# Append the root folder to sys.path
sys.path.append(root_folder)
