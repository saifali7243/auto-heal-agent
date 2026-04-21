from monitor import get_metrics
from rules import check_rules
from actions import take_action
import time

while True:
    metrics = get_metrics()
    print(f"\n📊 Metrics: {metrics}")

    issues = check_rules(metrics)

    if issues:
        print(f"⚠️ Issues detected: {issues}")
        for issue in issues:
            take_action(issue)
    else:
        print("✅ System healthy")

    time.sleep(5)
