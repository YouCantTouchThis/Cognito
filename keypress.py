from pynput import keyboard 
import time
from run import analysis


def k_press():
    t = {
        'time': time.time(),
        'time_flight': time.time(),
        'released': True,
        'keys_pressed': 0,
        'keys': []
    }


        


    LOAD_THRESH = 700

    def load_to_csv(keys, fname='presses.csv'):
        with open(fname, 'a') as f:
            for key_name, hold_time, release_time in keys:
                k = str(key_name)
                if '\\' in k:
                    continue
                k = k.replace("'", "")
                k = k.replace("Key.", "")
                k = k.replace(')', 'parenleft')
                k = k.replace(',', 'comma')
                k = k.replace(':', 'colon')
                k = k.replace(';', 'semicolon')
                k = k.replace('.', 'period')
                k = k.replace('(', 'parenright')
                k = k.replace('?', 'question')
                k = k.replace('enter', 'Return')
                if k == 'shift':
                    k = 'Shift_L'
                k = k.replace('shift_r', 'Shift_R')
                k = k.replace('backspace', 'BackSpace')
                k = f.write(f'"{k}",{hold_time},{round(hold_time+release_time, 4)},{release_time}\n')
        
        a = analysis()
        if a:
            



    def on_press(key):
        if t['released']:
            t['time'] = time.time()
            t['released'] = False
            print(f'{key} pressed after {time.time() - t["time_flight"]}')
            

    def on_release(key):
        print('{0} held for {1}s'.format(
            key, time.time() - t['time']))
        t['released'] = True
        t['keys_pressed'] += 1
        if t['keys_pressed'] % LOAD_THRESH == 0:
            load_to_csv(t['keys'])
            t['keys'] = []
        t['keys'].append(
            (
                str(key),
                round(time.time() - t['time'], 4),
                round(time.time() - t['time_flight'], 4)
            )
        )
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release,
    ) as listener:
        listener.join()

     
