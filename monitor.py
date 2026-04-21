import psutil


def get_metrics():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
    }


def get_top_process():
    processes = []

    for proc in psutil.process_iter(["pid", "name"]):
        try:
            cpu = proc.cpu_percent(interval=0.1)
            processes.append({"pid": proc.pid, "name": proc.name(), "cpu_percent": cpu})
        except:
            continue

    processes = sorted(processes, key=lambda x: x["cpu_percent"], reverse=True)

    return processes[0] if processes else None
