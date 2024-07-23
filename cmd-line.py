from communicator import speak, recognize_speech_from_microphone as micInput
from csv_editor import CSVEditor
from csv_editor import CreateCSV, EditCSV
from csv_sub_tasks import CSV_Sub_Tasks
from utils import print_starting_messages, seperate_commands
import sys

# Global Variable

main_commands = [
    ("create csv", "Create a new CSV file."),
    ("edit csv", "Edit a CSV file."),
]

sub_commands = [
    ("load csv", "Load a CSV file."),
    ("add row", "Add a new row with the specified values."),
    ("drop row", "Drop a row at the specified index."),
    ("edit row",
     "Edit a specific row and column with a new value."),
    ("add column",
     "Add a new column with the specified name and optional values."),
    ("drop column", "Drop a column with the specified name."),
    ("edit column",
     "Edit a specific cell in a column."),
    ("get row", "Get the data for a specific row."),
    ("set row", "Set a new row at the specified index."),
    ("get column", "Get the data for a specific column."),
    ("set column",
     "Set a new column with the specified name."),
]


def runSubTasks(csv_: CSVEditor):
    csv_sub_tasks = CSV_Sub_Tasks(csv_)

    try:
        print_starting_messages('sub', sub_commands, csv_)

        user_sub_cmd = micInput("Please say the command")

        sub_commands_only = seperate_commands(sub_commands)

        if user_sub_cmd in sub_commands_only:
            if user_sub_cmd != 'exit':

                if user_sub_cmd == "load csv":
                    # Code to load the current CSV data to a file
                    pass
                elif user_sub_cmd == "add row":
                    # Code to add a new row with specified values
                    csv_sub_tasks.addRow()

                elif user_sub_cmd == "drop row":
                    # Code to drop a row at the specified index
                    pass
                elif user_sub_cmd == "edit row":
                    # Code to edit a specific row and column with a new value
                    pass
                elif user_sub_cmd == "add column":
                    # Code to add a new column with the specified name and optional values
                    pass
                elif user_sub_cmd == "drop column":
                    # Code to drop a column with the specified name
                    pass
                elif user_sub_cmd == "edit column":
                    # Code to edit a specific cell in a column
                    pass
                elif user_sub_cmd == "get row":
                    # Code to get the data for a specific row
                    pass
                elif user_sub_cmd == "set row":
                    # Code to set a new row at the specified index
                    pass
                elif user_sub_cmd == "get column":
                    # Code to get the data for a specific column
                    pass
                elif user_sub_cmd == "set column":
                    # Code to set a new column with the specified name
                    pass
            else:
                speak('"Program exited successfully. See you next time!"')
        else:
            speak(
                "Command not recognized. Please say a valid command from the list.")
            runSubTasks(csv_)
    except Exception as e:
        speak(str(e))
        runSubTasks(csv_)


def runMainTasks(user_cmd):
    try:
        if user_cmd != 'exit':
            if user_cmd == "create csv":
                # Code to create a CSV file
                csv_filename_path = micInput(
                    'Say the name/path of the csv you want to create')

                csv_ = CreateCSV(csv_filename_path)
                runSubTasks(csv_)
            elif user_cmd == "edit csv":
                # Code to edit a CSV file
                csv_filename_path = micInput(
                    'Say the name/path of the csv you want to edit')

                csv_ = EditCSV(csv_filename_path)
                runSubTasks(csv_)

        else:
            speak('"Program exited successfully. See you next time!"')
            sys.exit(0)

    except Exception as e:
        speak(str(e))
        runMainTasks(user_cmd)


def take_user_cmd():
    user_cmd = micInput(
        "Please say the command")

    cmds_only = seperate_commands(main_commands)

    if user_cmd in cmds_only:
        runMainTasks(user_cmd)
    else:
        speak(
            "Command not recognized. Please say a valid command from the list")
        take_user_cmd()


# Main Programme


def main():
    try:
        print_starting_messages('main', main_commands)
        take_user_cmd()

    except Exception as e:
        speak(str(e))
        main()


main()
