# TODO
# send message via sms
def sms_send(message, phone):

# TODO
# combine all the formatted string in json_formatter
def string_combiner(json_formatter):

    return message

# TODO
class json_formatter(news_json):

# TODO
class api_querier(file):


# main program
# run continuously, wait until time input to sceduler
# create json job, convert to formatted obj, combine to string obj, send
def newsletterSMS(config_file, time, phone):
    while True:
        scheduler(time)
        news_json = api_querier(config_file)
        news_formatted = json_formatter(news_json)
        message = string_combiner(news_formatted)
        sms_send(message, phone)

# TODO
# allow for text file and 4 digit, 24hr time value, and phone number to be input via cli
# all three are required
# uses argparse library
def get_parser():

    return parser

#get values from cli and run main program with them
def command_line_runner():
    parser = get_parser()
    newsletterSMS(parser.config, parser.time, parser.phone)

# run program
if __name__ == '__main__':
    command_line_runner()
