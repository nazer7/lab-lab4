from datetime import datetime
def date_diff(date1: str, date2: str, date_format: str = "%Y-%m-%d %H:%M:%S") -> int:
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    difference = abs((d2 - d1).total_seconds())
    return int(difference)
date1 = "2025-02-20 12:00:00"
date2 = "2025-02-22 14:30:00"
diff_seconds = date_diff(date1, date2)
print(f"Difference in seconds: {diff_seconds}")