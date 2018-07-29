sms_send(message):



def string_combiner(json_formatter):

    return message


class json_formatter(news_json):


class api_querier(file):



def newsletterSMS(config_file, time):
    while True:
        scheduler(time)
        news_json = api_querier(config_file)
        news_formatted = json_formatter(news_json)
        message = string_combiner(news_formatted)
        sms_send(message)


def get_parser():

    return parser

def command_line_runner():
    parser = get_parser()
    newsletterSMS(parser.config, parser.time)

if __name__ == '__main__':
    command_line_runner()