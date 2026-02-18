import subprocess

steps = [
    "scripts/01_data_collection.py",
    "scripts/02_data_cleaning.py",
    "scripts/03_data_harmonization.py",
    "scripts/04_sustainability_indicators.py"
]

for step in steps:
    print(f"Running {step}...")
    subprocess.run(["python", step])

print("Pipeline completed successfully.")
