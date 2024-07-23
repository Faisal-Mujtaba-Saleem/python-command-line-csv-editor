from communicator import speak, recognize_speech_from_microphone as micInput
import shutil
import sys


def centeralizing_width():
    size = shutil.get_terminal_size()
    width = size.columns
    return width


def is_convertible_to_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


# def continue_or_exit(programme, args=None):
#     speak('Did you want to continue the programme or exit?')
#     isContinue = micInput(
#         'Say continue to continue the programme or say any word to exit')
#     if isContinue == 'continue':
#         if args != None:
#             programme(args)
#         else:
#             programme()

#     else:
#         sys.exit(1)


def print_commands(commands):
    for i, command_with_description in enumerate(commands):
        command, description = command_with_description
        print(f"{i}. {command} - {description}")


def seperate_commands(commands_with_description):
    return [cmd for cmd, desc, in commands_with_description]


def print_starting_messages(command_type, commands_to_print, csv_=None):
    if command_type == 'main':
        speak(
            "Welcome to Commandline-CSV-Editor!".center(centeralizing_width()), dots=False)
        speak("Switch to typing by pressing \'shift\' on the keyboard. Say 'exit' at any time to leave the editor.".center(
            centeralizing_width()), dots=False)
        speak("Note: If you need to enter a number - or - symbol - or - path to file, please switch to typing. Numbers symbols & paths can't be saved or written using speech input.".center(centeralizing_width()), dots=False)

    if command_type == 'sub':
        speak(f'Here\'s the overview of {
              csv_.csv_file_path}')
        df = csv_.get_dataframe()
        print(df)

    if command_type == 'main':
        speak(f"Here are the {
              command_type}-commands related to csv you can use:")
    else:
        speak(f"Here are the {
              command_type}-commands you can apply on your csv:")

    print_commands(commands_to_print)
