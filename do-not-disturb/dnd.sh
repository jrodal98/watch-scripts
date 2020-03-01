#!/usr/bin/env bash
# Jacob Rodal (www.jrodal.dev)

# toggles notification do not disturb mode
# automatically turned off at reboot

lock_file="/tmp/.dnd_lock_file"
dnd_icon="$HOME/.local/share/icons/dunst_icons/half-moon.svg"
error_icon="$HOME/.local/share/icons/dunst_icons/icons8-high-importance-48.png"

turn_on_dnd() {
    notify-send -i $dnd_icon "Do not disturb" "Do not disturb enabled"
    sleep 5 # sleep so that I can see the dnd notification
    notify-send "DUNST_COMMAND_PAUSE";
    touch $lock_file
}

turn_off_dnd() {
    notify-send "DUNST_COMMAND_RESUME";
    notify-send -i $dnd_icon "Do not disturb" "Do not disturb disabled"
    rm $lock_file
}


case $1 in

    state) # returns true if dnd is enabled, false otherwise
        if [ -f $lock_file ]; then
            true
        else
            false
        fi
        ;;
    on) # manually turn it on
        turn_on_dnd
        ;;
    off) # manually turn it off
        turn_off_dnd
        ;;
    "") # toggle on or off automatically
        if [ -f $lock_file ]; then
            turn_off_dnd
        else
            turn_on_dnd
        fi
        ;;
    *)
        notify-send -i $error_icon "Error" "Invalid option passed to do not disturb script"
        ;;
esac
