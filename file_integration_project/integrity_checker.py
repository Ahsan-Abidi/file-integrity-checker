import os
from hash_utils import calculate_hash
from file_ops import load_hashes, save_hash, update_hash, log_event
from alerts import send_email_alert, send_whatsapp_alert, send_to_cloud

# desktop notifications
try:
    from plyer import notification
except:
    notification = None


def alert_user(file_path):
    print(f"⚠️ MODIFIED: {file_path}")
    print("🔔 ALERT: File has been changed!")

    # sound alert
    try:
        import winsound
        winsound.Beep(1000, 500)
    except:
        pass

    # desktop notification
    if notification:
        notification.notify(
            title="File Alert 🚨",
            message=f"{file_path} modified!",
            timeout=5
        )


def check_integrity(file_path):
    current_hash = calculate_hash(file_path)
    if current_hash is None:
        return

    stored_hashes = load_hashes()

    if file_path in stored_hashes:
        if stored_hashes[file_path] == current_hash:
            print(f"✅ SAFE: {file_path}")
        else:
            alert_user(file_path)
            log_event(f"MODIFIED: {file_path}")

            # 🔥 ALERT SYSTEMS
            send_email_alert(file_path)
            send_whatsapp_alert(file_path)
            send_to_cloud(file_path)

            choice = input("Update hash? (y/n): ").lower()
            if choice in ['y', 'yes']:
                update_hash(file_path, current_hash)
                print("✅ Hash updated")
                log_event(f"HASH UPDATED: {file_path}")
    else:
        save_hash(file_path, current_hash)
        print(f"ℹ️ New file added: {file_path}")
        log_event(f"NEW FILE: {file_path}")


def check_folder(folder_path):
    if not os.path.exists(folder_path):
        print("❌ Folder not found!")
        return

    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            check_integrity(full_path)