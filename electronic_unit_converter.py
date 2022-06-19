import PySimpleGUI as sg

sg.theme('DarkBrown7')
layout = [
    [sg.Text('Choose an option below ', expand_x=1, justification='center')],
    [sg.Spin(['Voltage', 'Current', 'Resistance', 'Power'],
             key='-MENU-', expand_x=True), sg.Button('OK', key='-OK-', size=(15, 1))],
    [sg.Push(), sg.Text(enable_events=0, key='-LEB1-'),
     sg.Input(expand_x=0, key='-INPUT_1-', do_not_clear=0)],
    [sg.Push(), sg.Text(enable_events=0, key='-LEB2-'),
     sg.Input(expand_x=0, key='-INPUT_2-', do_not_clear=0)],
    [sg.Button('Submit', key='-BUTTON_1-', expand_x=True, size=(15, 2)),
     sg.Button('Clear', key='-BUTTON_2-', expand_x=True, size=(15, 2))],
    [sg.Text('OUTPUT', expand_x=True, justification='center',
             enable_events=True, key='-OUTPUT-')]
]
my_window = sg.Window('Electronic Converter', layout)


while True:
    event, values = my_window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-OK-':
        match values['-MENU-']:
            case 'Voltage':
                my_window['-LEB1-'].update('Current:')
                my_window['-LEB2-'].update('Resistance:')
            case 'Current':
                my_window['-LEB1-'].update('Voltage:')
                my_window['-LEB2-'].update('Resistance:')
            case 'Resistance':
                my_window['-LEB1-'].update('Voltage:')
                my_window['-LEB2-'].update('Current:')
            case 'Power':
                my_window['-LEB1-'].update('Voltage:')
                my_window['-LEB2-'].update('Current:')

    if event == '-BUTTON_1-':
        input_val_1 = values['-INPUT_1-']
        input_val_2 = values['-INPUT_2-']
        try:
            if float(input_val_1) and float(input_val_2):
                match values['-MENU-']:
                    case 'Voltage':
                        my_window['-LEB1-'].update('Current:')
                        my_window['-LEB2-'].update('Resistance:')
                        v = float(input_val_1) * float(input_val_2)
                        out_msg = f"Voltage : {round(v, 2)} Volt(V)"

                    case 'Current':
                        my_window['-LEB1-'].update('Voltage:')
                        my_window['-LEB2-'].update('Resistance:')
                        i = float(input_val_1) / float(input_val_2)
                        out_msg = f"Current : {round(i, 2)} Ampere(A)"

                    case 'Resistance':
                        my_window['-LEB1-'].update('Voltage:')
                        my_window['-LEB2-'].update('Current:')
                        r = float(input_val_1) / float(input_val_2)
                        out_msg = f"Resistance : {round(r, 2)} Ohms"
                    case 'Power':
                        my_window['-LEB1-'].update('Voltage:')
                        my_window['-LEB2-'].update('Current:')
                        p = float(input_val_1) * float(input_val_2)
                        out_msg = f"Power : {round(p, 2)} Watt(W)"

                my_window['-OUTPUT-'].update(out_msg)
        except:
            my_window['-OUTPUT-'].update(
                "Please,enter a valid input(integer or floating point number)")
    elif event == '-BUTTON_2-':
        my_window['-OUTPUT-'].update('OUTPUT')

my_window.close()
