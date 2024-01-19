import subprocess

def start_process(file_path_or_url):
    try:
        subprocess.run(["start", "", file_path_or_url], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Example usage:
# Replace "your_file.txt" or "https://www.example.com" with the actual file path or URL

# start_process("your_file.txt")

# Or
start_process("https://www.facebook.com")
