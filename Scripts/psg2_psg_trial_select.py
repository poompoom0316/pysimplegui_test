#!/usr/bin/env python3
import PySimpleGUI as sg
import subprocess
import os


def execute_command_blocking(command):
    expanded_args = []

    try:
        sp = subprocess.Popen(command, shell=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if out:
            print(out.decode("utf-8"))
        if err:
            print(err.decode("utf-8"))
    except:
        out = ''
        print("Something is Wring!!")
    return out


def main():
    path_dir = "Analysis"
    script_dir = "Scripts"
    sg.theme("DarkBlue")

    script_items = ["t3_echo_hello.py", "t4_add_hello.py"]
    commnad_dict = {key: value in zip(["output csv", ""])}
    items = ["Run", "Stand", "Sing", "Fight for Freedom"]
    option_list = os.listdir(path_dir)

    fiction_index = [3, 4, 6, 7]

    layout = [
        [sg.Text("Please select what you want to write.")],
        [sg.OptionMenu(items, size=(20, 10), key="-wish")],
        [sg.Text("Where do you want to do?")],
        [sg.OptionMenu(script_items, size=(20, 10), key="-command")],
        [sg.Text("Please select folder in which you want to save file.")],
        [sg.OptionMenu(option_list, size=(20, 10), key="-Output path")],
        [sg.Button("Quit"), sg.Button("RUN")],
        [sg.Output(size=(88, 20))]
    ]

    window = sg.Window("Sample program", layout, finalize=True)
    # listbox = window["-LISTBOX"].Widget
    # for index in fiction_index:
    #     listbox.itemconfigure(index, bg="blue", fg="white")

    while True:
        event, values = window.read()

        # ここで窓が閉じられたときの対応をしている？
        if (event == sg.WINDOW_CLOSED)|(event == "Quit"):
            break
        # elif event in (None, "Quit"):
        #     print("閉じると思った？残念でした！")

        elif event == 'RUN':
            window.refresh()  # make the print appear immediately
            print(f"Running {values['-command']}. Please wait until process is finished.")
            output_path = f"{path_dir}/{values['-Output path']}"
            commands = f"python  {script_dir}/{values['-command']} {values['-wish']} {output_path}"

            out = execute_command_blocking(command=commands)
            print(out)
            # print(f"python  {script_dir}/{values['-command']} {values['-wish']} {values['-Output path']}")

        print(f"{event} {values}")

    window.close()


if __name__ == '__main__':
    main()