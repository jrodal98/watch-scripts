#!/usr/bin/env python3
# Jacob Rodal (https://www.jrodal.dev) (jr6ff@virginia.edu)

import subprocess
import sys
from __init__ import send_notification
from notify_after import notify_after


@notify_after
def call_from_shell(argv):
    try:
        if len(argv) < 2:
            raise IndexError
        return subprocess.run(argv[1], shell=True, check=True)
    except IndexError:
        send_notification("notify-after error",
                          "shell command not provided", error=True)
    except subprocess.CalledProcessError as e:
        send_notification("notify-after error", str(e), error=True)
    except Exception as e:
        send_notification("notify-after error", str(e), error=True)
    sys.exit(1)


if __name__ == "__main__":
    call_from_shell(sys.argv)
