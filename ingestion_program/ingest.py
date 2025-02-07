import os
import subprocess
import sys

def main():
    input_data_dir = sys.argv[1]   # /input_data（from competition.yaml - input_data.zip）
    output_dir = sys.argv[2]       # /output（user output result ）
    submission_dir = sys.argv[3]   # /app/input（Decompression path of user-submitted code）

    
    command = ["python", os.path.join(submission_dir, "solve.py"), input_data_dir, output_dir]
    try:
        subprocess.check_call(command)
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)

if __name__ == "__main__":
    main()