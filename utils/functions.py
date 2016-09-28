import functools


def command(name, store=True):
    def decorator(func):
        func.__command_name__ = name
        func.__store__ = store
        return func
    return decorator


def private_command_handler(func):
    @functools.wraps(func)
    def wrapper(bot, update, args, **kwargs):
        if update.message.chat.type == 'private':
            func(bot, update, args, **kwargs)
        else:
            bot.sendMessage(update.message.chat_id,
                            text="Questa operazione è ammessa solamente in chat privata con il bot.")

    wrapper.__command_handler__ = True
    wrapper.__private_command_handler__ = True
    return wrapper


def pprint(l):
    fmt = "```\n{}\n```"
    if type(l) is list:
        if len(l) == 0:
            return []
        if type(l[0]) is list:
            return [fmt.format("\n".join(e)) for e in l]
        return [fmt.format("\n".join(l))]
    else:
        return [fmt.format(l)]