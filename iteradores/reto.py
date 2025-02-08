def sum_seconds(days: int) -> int:
    return days * 10


def convert_seconds_to_hours(seconds: int) -> tuple:
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds


def time_elapsed_total(total_days: int) -> int:
    total_seconds_elapsed = sum_seconds(total_days * (total_days - 1) // 2)
    return total_seconds_elapsed


def parse_number(number):
    return f"{number:02}"


total_days = 39
total_seconds = time_elapsed_total(total_days)
hours, total_minutes, remaining_seconds = convert_seconds_to_hours(total_seconds)
print(convert_seconds_to_hours(sum_seconds(total_days)))
print(
    f"{parse_number(hours)}:{parse_number(total_minutes)}:{parse_number(remaining_seconds)}"
)
