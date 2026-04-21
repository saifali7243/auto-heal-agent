def check_rules(metrics):
    issues = []

    if metrics["cpu"] > 30:
        issues.append("HIGH_CPU")

    if metrics["ram"] > 90:
        issues.append("HIGH_RAM")

    return issues
