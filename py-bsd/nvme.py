import os
import re
import subprocess

def get_nsid(path):
    name = os.path.basename(path)
    try:
        output = subprocess.check_output(["nvmecontrol", "nsid", path], stderr=subprocess.DEVNULL, text=True).strip()
        match = re.search(r"nvme\d+", output)
        controller = match.group(0) if match else name
        match = re.search(r"\d+", output)
        return controller, int(match.group(0)) if match else 1
    except (OSError, subprocess.CalledProcessError, ValueError):
        match = re.match(r"nvd(\d+)", name)
        return (f"nvme{match.group(1)}", 1) if match else (name, 1)
