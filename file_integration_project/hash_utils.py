import hashlib

def calculate_hash(file_path):
    hash_algo = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(4096)
                if not chunk:
                    break
                hash_algo.update(chunk)

        return hash_algo.hexdigest()

    except FileNotFoundError:
        print("❌ File not found!")
        return None