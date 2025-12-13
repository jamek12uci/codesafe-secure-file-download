import os
import json
from datetime import datetime

BASE_DIRECTORY = "/challenge/files"

class FileLogger:
    def __init__(self, log_file="download.log"):
        self.log_file = log_file

    def log(self, message):
        timestamp = datetime.utcnow().isoformat()
        with open(self.log_file, "a") as f:
            f.write(f"[{timestamp}] {message}\n")


class FileDownloadService:
    def __init__(self, base_directory=BASE_DIRECTORY):
        self.base_directory = base_directory
        self.logger = FileLogger()

    def list_files(self):
        try:
            return os.listdir(self.base_directory)
        except FileNotFoundError:
            return []

    def read_file(self, filename):
        file_path = os.path.join(self.base_directory, filename)
        self.logger.log(f"Attempting to read file: {file_path}")

        if not os.path.exists(file_path):
            raise FileNotFoundError("File does not exist")

        with open(file_path, "r") as f:
            return f.read()

    def download_file(self, filename):
        contents = self.read_file(filename)
        response = {
            "filename": filename,
            "length": len(contents),
            "downloaded_at": datetime.utcnow().isoformat(),
            "contents": contents
        }
        self.logger.log(f"Successfully downloaded {filename}")
        return json.dumps(response, indent=2)


def main():
    service = FileDownloadService()

    print("Available files:")
    for f in service.list_files():
        print(f" - {f}")

    print("\nDownloading example.txt...\n")
    print(service.download_file("example.txt"))


if __name__ == "__main__":
    main()
