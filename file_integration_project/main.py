import time
import os
from integrity_checker import check_integrity, check_folder

def main():
    print("=== FILE INTEGRITY CHECKER ===")

    print("1. Check single file")
    print("2. Check folder")
    print("3. Real-time monitoring")

    choice = input("Enter choice: ")

    if choice == "1":
        file_path = input("Enter file path: ")
        check_integrity(file_path)

    elif choice == "2":
        folder_path = input("Enter folder path: ")
        check_folder(folder_path)

    elif choice == "3":
        path = input("Enter file/folder path: ")

        print("🔄 Monitoring started (Ctrl+C to stop)")

        while True:
            try:
                if os.path.isfile(path):
                    check_integrity(path)
                else:
                    check_folder(path)

                time.sleep(5)

            except KeyboardInterrupt:
                print("\nStopped monitoring.")
                break

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()