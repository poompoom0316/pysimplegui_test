#!/usr/bin/env python3
import PySimpleGUI as sg
import subprocess
import os


def main():
    path_dir = "Analysis"
    command = "python Scripts/Demo_Script_Launcher.py"
    sg.theme("DarkBlue")

    items = ["USA", "Mexico", "Japan", "NoWhere", "TwilightZone", "Japan", "Unbalance Zone", "D-island"]
    items2 = ["Run", "Stand", "Sing", "FightforFreedom"]
    option_list = os.listdir(path_dir)

    fiction_index = [3, 4, 6, 7]

    layout = [
        [sg.Text("Where do you want to go?")],
        [sg.Listbox(items, size=(50, 18), key="-LISTBOX")],
        [sg.Text("What do you want to do?")],
        [sg.Listbox(items2, size=(25, 18), key="-LISTBOX_do")],
        [sg.Text("Please select choice you want to select.")],
        [sg.OptionMenu(option_list, size=(20, 10), key="-Select_choice")],
        [sg.Button("Quit"), sg.Button("OK")],
        [sg.Output(size=(88, 20))]
    ]

    window = sg.Window("Sample program", layout, finalize=True)
    listbox = window["-LISTBOX"].Widget
    for index in fiction_index:
        listbox.itemconfigure(index, bg="blue", fg="white")

    while True:
        event, values = window.read()

        # ここで窓が閉じられたときの対応をしている？
        if event == sg.WINDOW_CLOSED:
            break
        if event in (None, "Quit"):
            print("閉じると思った？残念でした！")

        print(f"イベント:{event}, 値: {values}")
        # subprocess.run(f"echo '-LISTBOX: {values['-LISTBOX'][0]}, -LISTBOX_do: {values['-LISTBOX_do'][0]}, -Select_choice: {values['-Select_choice']}'")
        os.system(f"echo '-LISTBOX: {values['-LISTBOX'][0]}, -LISTBOX_do: {values['-LISTBOX_do'][0]}, -Select_choice: {values['-Select_choice']}'")

        sp = subprocess.Popen([command], shell=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()

    window.close()


if __name__ == '__main__':
    main()