#!/usr/bin/env python3
# Jacob Rodal (https://www.jrodal.dev) (jr6ff@virginia.edu)

from sys import stderr
from __init__ import send_notification
from datetime import datetime


def notify_after(wrapped_func):
    """
    Sends a notification when some func finishes execution.
    notify-send must be installed on your system, else it 
    prints a message to stderr.
    """
    def wrapper(*args, **kwargs):
        starting_time = datetime.now()
        res = wrapped_func(*args, **kwargs)
        ending_time = datetime.now()
        if res == "INTERNAL NOTIFY AFTER FAIL":
            return -1
        time_diff = ending_time-starting_time
        diff_report = time_diff.total_seconds()
        unit = "seconds"
        if diff_report >= 3600:
            diff_report /= 3600  # report time in hours
            unit = "hours"
        elif diff_report >= 60:
            diff_report /= 60  # report time in minutes
            unit = "minutes"
        elif diff_report < 1:
            diff_report *= 1000
            unit = "milliseconds"

        try:
            process = "Python"
            name = wrapped_func.__name__
            if name == "call_from_shell":
                name = process = args[0][1]
            title = f"{process} execution completed"
            message = f"'{name}' has finished executing after {diff_report:.4} {unit}"
            send_notification(title, message)

        except Exception as e:
            print(str(e), file=stderr)
        finally:
            return res
    return wrapper
