import configparser


# move the variables from the settings files into a dictionary
def def_vars(conf_path, env_path):
    values = {}
    values2 = {}
    config = configparser.ConfigParser()
    config.read(conf_path)

    env = configparser.ConfigParser()
    env.read(env_path)

    values['time'] = int(config['general']['time'])
    values['phone'] = int(env['personal']['phone'])

    # use a for or while loop
    values2['API'] = (env['API_key']) + (env['API_num'])
    # TODO: pull the rest of the values from the .config and .env into the dictionary

    return values

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
# class jsonFormatter(news_json):



# TODO
# class apiQuerier(file):


# main program
# run continuously, wait until time input to scheduler
# create json job, convert to formatted obj, combine to string obj, send
def newslettersms(values):
    while True:
        scheduler(values['time'])
        news_json = apiQuerier()
        news_formatted = jsonFormatter(news_json)
        message = string_combiner(news_formatted)
        sms_send(message, values['phone'])

# run program
if __name__ == '__main__':
    settings = def_vars('../.conf', '../.env')
    newslettersms(settings)
