# sms-decorator

## Requirements

- python 3.6+
- a Twilio account

## About

The `sms_decorator.py` file contains a decorator that will send you a text message with details about the execution when a decorated function finishes execution.  This is helpful when waiting on long processes, as you don't have to constantly check your python process to see if it has finished.  The output will look something like this:

    Sent from your Twilio trial account - A python function has finished exectuting.

            Function: test_function

            Arguments: (1, 2)

            Keyword Arguments: {'kwarg1': 3, 'kwarg2': 4}

            Returned: 10

            Length of Execution: 2.002 seconds

            Sent at: 22:57

or this

    Sent from your Twilio trial account - A python function has finished exectuting, but the information is too large to display.

            Function: batch_classify

            Length of Execution: 2.947 minutes

            Sent at: 00:07

## How to use

### Setup

1) Clone this repo.
```bash
git clone https://github.com/jrodal98/sms-decorator.git
```
2) Install dependencies doing something like this:
```bash
cd sms-decorator
pip3 install -r requirements.txt
```
3) Copy `sms_decorator.py` and `config.py` into any project you want to use the decorator in.
4) Setup a free twilio account [here](https://www.twilio.com/)
5) Setup the config.py file (skeleton provided).  It should include the following:
    1) Your account SID
    2) Your auth token
    3) Your twilio number
    4) Your cellphone number
6) import `sms_decorator as sms_decorator` into the file you desire.  You might need to import it differently depending on the structure of your project. (Left as an exercise to the reader)
I recommend running `test.py` to verify that everything is setup properly.

### Usage
If you don't know what decorators are, consider reading this [short explanation](https://www.geeksforgeeks.org/decorators-in-python/).  Essentially, decorators allow you to wrap another function to extend its behavior without permanently modifying it.  In our case, the SMS decorator grants your function the ability to operate as you write it with the bonus behavior of also sending a text message when your function completes its execution.  It can be used like so:

```python
from sms_decorator import sms_decorator

@sms_decorator
def your_function():
    print("Do whatever you want here")

"""Above code is equivalent to - 
  
def your_function():
    print("Do whatever you want here")
      
your_function = sms_decorator(your_function)"""
```

When `your_function` is executed, it will print "Do whatever you want here" and then send you a text message.
