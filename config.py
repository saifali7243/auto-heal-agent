import yaml
import time

last_loaded = 0
config_cache = {}


def load_config():
    global last_loaded, config_cache

    current_time = time.time()

    if current_time - last_loaded > 10:  # reload every 10s
        with open("config.yaml", "r") as f:
            config_cache = yaml.safe_load(f)
        last_loaded = current_time

    return config_cache
