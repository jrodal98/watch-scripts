# backup-system

This shell script decrypts my external hard drive, mounts the hard drive, uses `rsync` to backup files, unmounts the hard drive, and then terminates the decrypted session.  Lastly, it uses my `notify-after` script found [here](../notify-after/) to send me a notification that the task has been completed.
