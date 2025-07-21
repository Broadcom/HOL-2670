#!/usr/bin/env python3
# version 1.3 24-May 2023
# Huge thanks to HOL Captain Nick Robbins for developing this tool.

import os
import pathlib
#import PySimpleGUI as sg
import FreeSimpleGUI as sg
import argparse
import base64
import subprocess
import re
# import sys
# import math
# from pydoc import describe
# import ansible_runner

parser = argparse.ArgumentParser(description="Hands-on Labs Module Switcher")

# parser.add_argument('--sku',action="store", dest="sku")
parser.add_argument('--dir', action="store", dest="workdir",
                    help="Working directory, optional, will use current working directory if not specified")

args = parser.parse_args()
scriptfolder = 'module-scripts'

if args.workdir is None:
    args.workdir = os.getcwd()


skupath = os.path.join(args.workdir, 'skulist.txt')
script_path = os.path.join(args.workdir, scriptfolder)
icon_path = os.path.join(args.workdir, 'hol-logo.png')

iconb64 = base64.b64encode(open(icon_path, 'rb').read())
panel_name = 'Hands-on Labs Module Switcher'


def execute(cmd):
    popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, universal_newlines=True)
    for stdout_line in iter(popen.stdout.readline, ""):
        yield stdout_line
    popen.stdout.close()
    return_code = popen.wait()
    if return_code:
        raise subprocess.CalledProcessError(return_code, cmd)


def sort_and_dedupe_list(the_list):
    """remove duplicates from and sort a list"""
    the_new_list = list(set(the_list))
    the_new_list.sort()
    return the_new_list


class ButtonPanel:
    def __init__(self, module_scripts):
        active_module = 0
        sg.theme('LightBlue7')
        layout_buttons = []
        # print(rows)
        """
        from:
        https://stackoverflow.com/questions/9671224/split-a-python-list-into-other-sublists-i-e-smaller-lists/9671301
        """
        chunks = [module_scripts[x:x + 4] for x in range(0, len(module_scripts), 4)]
        # print(chunks)
        for the_list in chunks:
            # print(f"this is the list: {the_list}")
            row = []
            for item in the_list:
                # print(f"this is the item: {item}")
                script_str = str(item)
                row.append(sg.Button(script_str.replace(script_path + '/', "").split(".", 1)[0],
                                     size=(20, 1),
                                     key=script_str.replace(script_path + '/', ""),
                                     button_color='dodgerblue4'))
            layout_buttons.append(row)

        modulelayout = [
            [layout_buttons],
            [sg.Text('Script output....', size=(40, 1))],
            [sg.Output(size=(88, 20), font='Courier 10', text_color='black', background_color='white')],
        ]

        window = sg.Window('Select Hands-on Labs Module', modulelayout, icon=iconb64, auto_size_buttons=True)

        while True:
            panelevent, values = window.read()
            if panelevent == 'EXIT' or panelevent == sg.WIN_CLOSED or panelevent is None:
                exit(0)
            try:
                script = os.path.join(script_path, panelevent)
                modnumbers = re.findall(r'\d+', str(panelevent))
                requested_module = int(modnumbers[2])
                # print(f"Run Script: {script} active mod: {active_module} requested mod: {requested_module}")
                if requested_module > active_module:
                    for path in execute(["/bin/bash", script]):
                        print(path, end="")
                        window.refresh()
                    active_module = requested_module
                    # run_sync = ansible_runner.run(project_dir=script_path, playbook=panelevent, rotate_artifacts=1)
                    # print(run_sync.stdout.readlines())
                else:
                    print(f"Please choose a module greater than {active_module}")
            except Exception as e:
                print(e)


if __name__ == '__main__':
    sg.theme('LightBlue7')
    skulist = open(skupath).readlines()
    layout = [
        [sg.Text('Please Select the Lab', size=(50, 1))],
        [sg.Listbox(values=skulist,
                    key="skulist",
                    size=(50, len(skulist)),
                    text_color='black',
                    background_color='ghost white')],
        [sg.Button('Go to Module Selection', button_color='dodgerblue4')]
    ]
    if len(skulist) > 1:
        win = sg.Window('Hands-on Labs Module Switcher', layout, icon=iconb64)
        event, sku = win.read()
        if event is None:
            exit(1)
        while len(sku['skulist']) == 0:
            event, sku = win.read()
        win.close()
        skuname = (sku['skulist'][0])[4:11]
    else:
        skuname = (skulist[0])[4:11]

    list_of_scripts = []
    if os.path.exists(script_path) and os.path.isdir(script_path):
        list_of_scripts = [p for p in pathlib.Path(script_path).glob(f"{skuname}-module*.sh") if p.is_file()]

    sorted_list_of_scripts = sort_and_dedupe_list(list_of_scripts)
    ButtonPanel(sorted_list_of_scripts)
