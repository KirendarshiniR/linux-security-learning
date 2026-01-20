# This is a simple learning script written to explore how Linux
# authentication logs work and how failed login attempts are recorded.
# The goal is to get comfortable reading system logs using Python,
# not to build a production security tool.

def monitor_auth_log(log_path):
    try:
        with open(log_path, "r", errors="ignore") as log_file:
            for line in log_file:
                if "Failed password" in line:
                    print(line.strip())
    except FileNotFoundError:
        print("Authentication log not found. This script is intended to run on Linux systems.")

if __name__ == "__main__":
    monitor_auth_log("/var/log/auth.log")
