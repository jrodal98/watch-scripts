# Jacob Rodal (https://www.jrodal.dev) (jr6ff@virginia.edu)

try:
    from twilio.rest import Client
    from twilio.base.exceptions import TwilioRestException
except:
    print("You must install twilio! Run `pip3 install -r requirements.txt` from source directory.")

try:
    import config
except:
    print("You must create a config.py file containing your twilio credentials.  See the README for further instructions.")

from datetime import datetime


def sms_decorator(wrapped_func):
    """
    Sends a text message when wrapped_func finishes execution
    """

    def wrapper(*args, **kwargs):
        # get result from executing function
        starting_time = datetime.now()
        result = wrapped_func(*args, **kwargs)
        ending_time = datetime.now()
        time_diff = ending_time-starting_time
        diff_report = time_diff.total_seconds()
        unit = "seconds"
        if diff_report >= 3600:
            diff_report /= 3600  # report time in hours
            unit = "hours"
        elif diff_report >= 60:
            diff_report /= 60  # report time in minutes
            unit = "minutes"
        try:
            end = ending_time.strftime("%H:%M")
            try:
                res_message = str(result)
                if len(res_message > 800):
                    res_message = "Result is too large to be represented in text form"
            except:
                res_message = "Result cannot be represented in text form"
            finally:
                message = f"""
            A python function has finished exectuting.\n
            Function: {wrapped_func.__name__}\n
            Arguments: {args}\n
            Keyword Arguments: {kwargs}\n
            Returned: {res_message}\n
            Length of Execution: {diff_report:.4} {unit}\n
            Sent at: {end}
                """
                if len(message) > 1500:
                    message = f"""
            A python function has finished exectuting, but the information is too large to display.\n
            Function: {wrapped_func.__name__}\n
            Length of Execution: {diff_report:.4} {unit}\n
            Sent at: {end}
                """

            twilio_client = Client(config.account_sid, config.authtoken)
            twilio_client.api.messages.create(
                body=message, from_=config.twilio_number, to=config.my_cellphone)
        except TwilioRestException as e:
            print(
                f"Something is wrong with twilio.  Verify that the account is setup correctly and that the values in the config file are correct.\n{e}")
        except Exception as e:
            print(
                f"Error: {e}")
        finally:  # ensures that the function still returns the result despite not sending the text message
            return result
    return wrapper
