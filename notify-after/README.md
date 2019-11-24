# notify-after

## Requirements:

- Linux
  - You can use this script on mac os by replacing `send-notify` calls with the mac equivalent - tt would take maybe 2 minutes to implement.  If you want me to implement it for you, open an issue and I'll do it.
  - Fuck windows (I'm not even going to bother with changing my script to run over there)
- python 3.6+
- `send-notify`
  - I think this comes with most desktop and window managers.  If not, google how to install it.

## About

This python script contains a python shell script (and decorator) that sends a desktop notification whenever a shell process or decorated function finishes execution.  This can be used inside of python scripts (see my [sms-decorator](../sms-decorator/) for an explanation of how to use decorators) or it can be used with shell scripting like so:

`./notify-after echo test`

or

`notify-after sudo pacman -Syu`

or in actual scripts:

```bash
my_func () {
    ls *
    sleep 2
    echo "nice"   
}

./notify-after my_func
```

It can, of course, also be used as a decorator.  Some examples of using decorators can be found in my [sms-decorator](../sms-decorator/) - the principle here is the same.
