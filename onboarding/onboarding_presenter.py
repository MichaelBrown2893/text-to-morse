"""Onboarding Presenter

This script is responsible for printing the onboarding elements of the
morse-to-text application

This file can also be imported as a module and contains the following
functions:

    * print_title - prints ascii art for the app title
    * print_welcome_message - prints welcome message
    * print_instructions - prints instructions for using the app
"""

from . import onboarding_model

def display_onboarding():
    """Displays all onboarding information for the app"""
    __display_title()
    __display_welcome_message()
    __display_instructions()


def __display_title():
    """Displays the title of the app"""
    print(onboarding_model.TITLE)


def __display_welcome_message():
    """Displays the app welcome message"""
    print(onboarding_model.WELCOME_MESSAGE)


def __display_instructions():
    """Displays the app instructions"""
    print(onboarding_model.INSTRUCTIONS)
