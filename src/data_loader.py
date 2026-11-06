import random
import pandas as pd
from datetime import datetime, timedelta

def fetch_traffic_overview() -> pd.DataFrame:
    now = datetime.now()
    dates = [now - timedelta(days=i) for i in range(6, -1, -1)]
    normal = [random.randint(22000, 28000) for _ in range(7)]
    suspicious = [random.randint(11000, 15000) for _ in range(7)]
    malicious = [random.randint(3500, 6000) for _ in range(7)]
    return pd.DataFrame({
        'Date': [d.strftime('%Y-%m-%d') for d in dates],
        'Normal Traffic': normal,
        'Suspicious Traffic': suspicious,
        'Malicious Traffic': malicious
    })

def fetch_attack_distribution() -> pd.DataFrame:
    types = ['DDoS Attack', 'Port Scan', 'SQL Injection', 'XSS Attack', 'Brute Force', 'Others']
    counts = [
        random.randint(750, 850),
        random.randint(500, 600),
        random.randint(400, 500),
        random.randint(280, 350),
        random.randint(180, 220),
        random.randint(100, 150)
    ]
    return pd.DataFrame({'Type': types, 'Count': counts})

def fetch_recent_alerts(limit: int = 10) -> pd.DataFrame:
    now = datetime.now()
    types = ['DDoS Attack', 'SQL Injection', 'Port Scan', 'XSS Attack', 'Brute Force', 'DDoS Attack', 'SQL Injection', 'Port Scan', 'XSS Attack', 'Brute Force']
    sources = ['192.168.1.105', '192.168.1.110', '192.168.1.108', '192.168.1.115', '192.168.1.120', '192.168.1.130', '192.168.1.140', '192.168.1.150', '192.168.1.160', '192.168.1.170']
    dests = ['10.0.0.5', '10.0.0.8', '10.0.0.15', '10.0.0.12', '10.0.0.20', '10.0.0.25', '10.0.0.30', '10.0.0.35', '10.0.0.40', '10.0.0.45']
    severities = ['Critical', 'High', 'Medium', 'Medium', 'Low', 'Critical', 'High', 'Medium', 'Medium', 'Low']
    actions = ['Blocked', 'Blocked', 'Logged', 'Blocked', 'Logged', 'Blocked', 'Blocked', 'Logged', 'Blocked', 'Logged']

    times = [(now - timedelta(seconds=i*25 + random.randint(1, 10))).strftime('%b %d, %Y %H:%M:%S') for i in range(10)]

    df = pd.DataFrame({
        'Time': times,
        'Type': types,
        'Source IP': sources,
        'Destination IP': dests,
        'Severity': severities,
        'Action': actions
    })
    return df.head(limit)

def fetch_system_metrics() -> dict:
    return {
        'cpu': random.randint(28, 45),
        'memory': random.randint(60, 72),
        'disk': 78,
        'network': random.randint(40, 65)
    }

def fetch_top_metrics() -> list:
    total_alerts = random.randint(2400, 2550)
    critical_alerts = random.randint(140, 170)
    blocked_attacks = random.randint(1300, 1380)
    return [
        ("Total Alerts", f"{total_alerts:,}", f"+{round(random.uniform(10.0, 14.0), 1)}% vs last 7 days"),
        ("Critical Alerts", f"{critical_alerts}", f"+{round(random.uniform(7.0, 9.5), 1)}% vs last 7 days"),
        ("Blocked Attacks", f"{blocked_attacks:,}", f"+{round(random.uniform(14.0, 16.5), 1)}% vs last 7 days"),
        ("Traffic Analyzed", "2.45 TB", "+23.1% vs last 7 days"),
        ("Active Connections", f"{random.randint(8400, 8700):,}", f"+{round(random.uniform(4.0, 6.5), 1)}% vs last 7 days")
    ]
