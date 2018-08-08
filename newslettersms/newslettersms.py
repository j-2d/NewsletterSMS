import configparser

def def_vars(conf_path, env_path):
    settings = {}
    config = configparser.ConfigParser()
    config.read(conf_path)

    env = configparser.ConfigParser()
    env.read(env_path)

    settings["time"] = int(config['general']['time'])

    return settings

# TODO
# send message via sms
def sms_send(message, phone):

    return

# TODO
# combine all the formatted string in json_formatter
def string_combiner(json_formatter):

    message = "hi"

    return message

# TODO
# wait until the scheduled time to run the program
def scheduler(time):


    return

# TODO
class json_formatter(news_json):




# TODO
class api_querier(file):


# main program
# run continuously, wait until time input to scheduler
# create json job, convert to formatted obj, combine to string obj, send
def newsletterSMS(time, phone):
    while True:
        scheduler(time)
        news_json = api_querier()
        news_formatted = json_formatter(news_json)
        message = string_combiner(news_formatted)
        sms_send(message, phone)

# run program
if __name__ == '__main__':
    def_vars('../.conf', '../.env')
    newsletterSMS()