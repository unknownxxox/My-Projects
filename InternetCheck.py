import subprocess

print("Checking internet connection...")

try:
    
    result = subprocess.run(
        ['ping', '-c', '2', '-W', '1', '8.8.8.8'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    if result.returncode == 0:
        print("✅ Internet is up.")
    else:
        print("❌ Internet is down.")
except Exception as e:
    print(f"❌ Error occurred: {e}")
