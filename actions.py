import os
import time
from monitor import get_top_process
from config import load_config
from logger import log_info, log_error

config = load_config()

# Cooldown tracker (prevents repeated killing)
last_kill_time = 0
COOLDOWN_SECONDS = 15


def normalize(name):
    if not isinstance(name, str):
        return ""
    return name.lower().strip()


def take_action(issue):
    global last_kill_time

    if issue != "HIGH_CPU":
        return

    # Cooldown check
    current_time = time.time()
    if current_time - last_kill_time < COOLDOWN_SECONDS:
        print("⏳ Cooldown active, skipping action")
        return

    process = get_top_process()

    if not process:
        print("❌ No process found")
        return

    name = normalize(process.get("name"))
    pid = process.get("pid")
    cpu = process.get("cpu_percent")

    print(f"🔥 Top process: {name} (PID: {pid}) using {cpu}% CPU")

    # Load config safely
    safe_processes = [normalize(p) for p in config.get("safe_processes", [])]
    killable_processes = [normalize(p) for p in config.get("killable_processes", [])]

    # Debug prints (important for now)
    print(f"DEBUG → safe: {safe_processes}")
    print(f"DEBUG → killable: {killable_processes}")

    # Safety check
    if name in safe_processes:
        print(f"🛑 Skipping safe process: {name}")
        return

    # Kill logic
    if name in killable_processes:
        message = f"Killing process: {name} (PID: {pid})"
        print(f"💀 {message}")
        log_info(message)

        try:
            os.kill(pid, 9)
        except Exception as e:
            error_msg = f"Failed to kill {name}: {e}"
            print(f"❌ {error_msg}")
            log_error(error_msg)
            last_kill_time = current_time
        except Exception as e:
            error_msg = f"Failed to kill process: {e}"
            print(f"❌ {error_msg}")
            log_error(error_msg)
    else:
        print(f"⚠️ Process not allowed to kill: {name}")
