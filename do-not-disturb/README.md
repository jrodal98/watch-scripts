# Do not disturb

A bash script that enables or disables a do not disturb mode for dunst notifications.

## Usage

There are two modes - automatic mode and manual mode.  Automatic mode will detect whether or not do-not-disturb is on or off and automatically swap states.

### Automatic mode

To automatically toggle between modes, run `dnd.sh` with no arguments. If do-not-disturb is not currently on, running `dnd.sh` will turn do-not-disturb on.  If do-not-disturb is on, running `dnd.sh` will turn do-not-disturb off.

### Manual mode

Run `dnd.sh on` to manually turn do-not-disturb on and run `dnd.sh off` to manually turn do-not-disturb off.

### Optional icons

To add an icon for the notification that tells you whether or not do not disturb is on, simply change the `dnd_icon` variable in the bash script.  Additionally, there is an `error_icon` variable for if the script is ever used incorrectly.
