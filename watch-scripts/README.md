# watch-scripts

As seen on reddit: <https://www.reddit.com/r/unixporn/comments/e65cb1/ticwatch_pro_launching_scripts_from_smartwatch/?utm_source=share&utm_medium=web2x>

I can launch shell scripts from my smartwatch on my linux machine using a combination of KDEConnect and Tasker (an android application).  My scripts are in this repo, as well as a guide for setting it up yourself.

Launching scripts from an android device to a linux machine is fairly straightfoward, so I will explain that first.  Then, I will explain a simple approach for launching scripts on a wear OS smartwatch.

## Launching scripts from android device

I'm assuming an arch linux i3 WM setup in my below instructions since that is what I'm running.  It should be very similar on other linux distros and WM.

1) install KDEconnect with `sudo pacman -Syu kdeconnect`
2) add `exec --no-startup-id /usr/lib/kdeconnectd` to i3config
3) Optionally, add `exec --no-startup-id kdeconnect-indicator` to add the kdeconnect-indicator to your system tray
   - If the indicator doesn't show up on your bar, you might need to enable the system tray on your bar.  Google how to do that if you don't know what I'm talking about.
4) restart i3 session
5) Download kdeconnect app on android device
6) run `kdeconnect-cli -l` to list devices
	- My android device didn't show up for me right away, probably because of my University's network.  To get around this, I added my laptop's IP address manually on the android app and then they could communicate with each other.
6) run `kdeconnect-cli -d DEVICE_ID --pair` to pair the devices
    - The device ID is the hash (or whatever it is) that comes up when you run `kdeconnect-cli -l`
7) Open the kdeconnect-indicator and add commands you want to run.
    - This instruction is purposefully vague, as you should look at KDEConnect tutorials for this instead of listening to me :) It's very easy though, dont worry.

If everything is set up correctly, you should be able to run commands from your phone!  Consider adding the KDEConnect command widget to your android home screen.  If you don't know what I'm talking about, google "android widgets" or something like that.

## Launching scripts from Wear OS smartwatch

This is where things got a little tricky for me.  First off, in order to do this the way I did it, you'll need to purchase Tasker from the google play store, which costs $3.49.  From my limited experience with it, it seems like an amazing app and it's been worth the money for me.  There may be other approaches that work for free, but I didn't come across anything from my research.

Also, I don't think my solution is the best Tasker based solution.  I send a notification dialogue to my smartwatch, but ideally, you would want to map it to a hardware button on your watch.  If I get around to doing that, I'll update the README with the alternative instructions.  You may want to look at this [Reddit comment](https://www.reddit.com/r/unixporn/comments/e65cb1/ticwatch_pro_launching_scripts_from_smartwatch/f9o06bu?utm_source=share&utm_medium=web2x) that outlines an approach for doing this.

Nevertheless, here is how I did it:

1) Download Tasker from google play ($3.49 purchase)
2) For each KDEConnect command you want on your watch (a maximum of 3, unfortunately):
   1) Copy the command URL by pressing and holding the command
   2) Go to the tasks tab on tasker
   3) Click the add button and name the task whatever you want it to be
   4) Add the following action: Net -> Browse URL.  Paste your URL in the prompt.
3) Once you have your tasks ready, add another task that will serve as the notification dialogue.
   1) Add the following action: Alert -> Notify
   2) Fill out title and optionally the text, add notification icon, etc.  **Make sure that the notification is not set to permanent**
   3) At the bottom of the screen, you'll see "Actions."  Add your tasks from the previous step (the KDEconnect commands) here.
      1) To do this, click the + button, which directs you to a new page.  Select an icon and name it whatever you want (e.g. lock).  For the action section, click the search icon and navigate to Task -> Perform Task.
      2) In the name section, click the search icon.  Select the task you want to associate with this action.
   4) Repeat 1-3 for each of your KDEConnect command tasks.

5) Launch the notification task in Tasker by clicking on its name under the Tasks tab and hitting the play button.  This will send it to your watch's notification screen.
    - There are some shortcomings to this approach, as it won't launch automatically and will show up even if your phone and laptop aren't connected.  I personally don't mind this, but you might want to look into changing this
    - If you clear the notification on the watch or your phone, you'll have to relaunch it in Tasker

Obviously, there are some improvements to be made here, but this gets the job done for me.  I've only had to launch the notification in Tasker twice because I accidentally cleared the notification once.  I will update this document if I change my setup significantly.

Feel free to submit an issue or make a pull request if you have any suggestions for improving this experience!
