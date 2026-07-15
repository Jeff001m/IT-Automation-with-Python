import subprocess

website = "google.com"

print(f"Checking connectivity to {website}...")

result = subprocess.run(
    ["ping", "-c", "4", website],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("✅ Network connection is working.")
else:
    print("❌ Unable to reach the website.")

print("\nOutput:\n")
print(result.stdout)
