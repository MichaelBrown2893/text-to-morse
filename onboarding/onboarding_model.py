"""Onboarding Model

This script is responsible for storing the onboarding elements of the
morse-to-text application

This file can also be imported as a module and contains the following
fields:

    * TITLE_ASCII - ascii art for the app title
    * WELCOME_MESSAGE - app welcome message
    * INSTRUCTIONS - app instructions
"""

TITLE_ASCII: str = ('\n'
                '  _____        _      _____        __  __                 \n'
                ' |_   _|____ _| |_ __|_   _|__ ___|  \/  |___ _ _ ___ ___ \n'
                '   | |/ -_) \ /  _|___|| |/ _ \___| |\/| / _ \ \'_(_-</ -_)\n'
                '   |_|\___/_\_\\__|    |_|\___/   |_|  |_\___/_| /__/\___|\n')

WELCOME_MESSAGE: str = 'Welcome to text-to-morse!'

INSTRUCTIONS: str = 'When prompted, input your text to convert to morse and press "ENTER".'
