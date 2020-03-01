# notify-after

## Requirements:

- Linux or MacOS
    - If running Linux, `send-notify` also needs to be installed
        - Google it for your distro. It's probably already installed, unless you're running something like arch with no desktop enviroment.
    - If running MacOS, `terminal-notifier` also needs to be installed
        - `brew install terminal-notifier`
- python 3.6+

## About

This python package contains a python shell script (and decorator) that sends a desktop notification whenever a shell process or decorated function finishes execution.  This can be used inside of python scripts (see my [sms-decorator](../sms-decorator/) for an explanation of how to use decorators) or it can be used with shell scripting like so (NOTE - notify-after is the directory name):

`python3 /path/to/notify-after "echo test"`

or

`notify-after "sudo pacman -Syu"`

or inside the directory itself

`python3 /path/to/notify-after . "sleep 1; echo test"`

or in actual scripts:

```bash
my_func () {
    ls *
    sleep 2
    echo "nice"   
}

python /path/to/notify-after my_func
```

It can, of course, also be used as a decorator.  Some examples of using decorators can be found in my [sms-decorator](../sms-decorator/) - the principle here is the same.
