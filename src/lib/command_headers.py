commands = {

    '!kajfklajflksajlkfjlksjf': {
        'limit': 200,
        'argc': 1,
        'return': 'command',
        'space_case': True,
        'ul': 'mod',
        'usage': "!report [insert bug report text here]"

    },

    '!asndan,mna,n,awmn,man,m': {
        'limit': 15,
        'return': 'There is a README for me on my profile',
        'usage': '!help'

    },

}


def initalizeCommands(config):
    for channel in config['channels']:
        for command in commands:
            commands[command][channel] = {}
            commands[command][channel]['last_used'] = 0
