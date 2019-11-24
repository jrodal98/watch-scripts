from sms_decorator import sms_decorator
import time

# usage 1


@sms_decorator
def test_function(arg1, arg2, kwarg1=1, kwarg2=2):
    time.sleep(2)
    return arg1 + arg2 + kwarg1 + kwarg2

# usage 2


# def test_function(arg1, arg2, kwarg1=1, kwarg2=2):
#     time.sleep(2)
#     return arg1 + arg2 + kwarg1 + kwarg2


# another function = sms_decorator(test_function)


# both of the above styles will produce the same result.

result = test_function(1, 2, kwarg1=3, kwarg2=4)
print(f"Test result: {result}\n If you see an error or don't recieve a text message, something is wrong with your setup.")
