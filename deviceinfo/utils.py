import platform
import subprocess

def get_system_info():
    system = platform.system()
    info = {
        "os": system,
        "manufacturer": "Unknown",
        "model": "Unknown",
        "serial": "Unknown"
    }

    try:
        if system == "Windows":
            manufacturer = subprocess.check_output("wmic computersystem get manufacturer", shell=True).decode().split("\n")[1].strip()
            model = subprocess.check_output("wmic computersystem get model", shell=True).decode().split("\n")[1].strip()
            serial = subprocess.check_output("wmic bios get serialnumber", shell=True).decode().split("\n")[1].strip()

        elif system == "Darwin":  # macOS
            manufacturer = "Apple"
            model = subprocess.check_output(["sysctl", "-n", "hw.model"]).decode().strip()
            serial = subprocess.check_output(["system_profiler", "SPHardwareDataType"]).decode()
            serial = [line for line in serial.split("\n") if "Serial Number" in line][0].split(":")[-1].strip()

        elif system == "Linux":
            def run_dmidecode(key):
                output = subprocess.check_output(f"sudo dmidecode -t system | grep '{key}'", shell=True).decode()
                return output.split(":")[1].strip()

            manufacturer = run_dmidecode("Manufacturer")
            model = run_dmidecode("Product Name")
            serial = run_dmidecode("Serial Number")

        info.update({
            "manufacturer": manufacturer,
            "model": model,
            "serial": serial
        })
    except Exception as e:
        info["error"] = str(e)

    return info
