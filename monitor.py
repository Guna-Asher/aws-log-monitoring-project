import boto3
import os
from datetime import datetime

LOG_FILE = "app.log"
S3_BUCKET = "guna-log-archive-2026-devops"

def analyze_logs():
    # 1. Check if the log file even exists to avoid FileNotFoundError
    if not os.path.exists(LOG_FILE):
        print(f"{LOG_FILE} not found.")
        return

    errors = []
    with open(LOG_FILE, "r") as file:
        for line in file:
            if "ERROR" in line:
                errors.append(line)

    if errors:
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        filename = f"errors-{timestamp}.txt"

        # Write temporary error file
        with open(filename, "w") as f:
            f.writelines(errors)

        try:
            s3 = boto3.client("s3")
            s3.upload_file(filename, S3_BUCKET, filename)
            print(f"Uploaded {filename} to S3")
            
            # Optional: Remove the local temp error file after upload
            os.remove(filename) 
        except Exception as e:
            print(f"Failed to upload to S3: {e}")
            return # Exit so we don't wipe the log if upload fails

    else:
        print("No errors found")

    # 2. Clear the log file ONLY after processing is done
    open(LOG_FILE, "w").close()
    print("Main log file cleared.")

if __name__ == "__main__":
    analyze_logs()
