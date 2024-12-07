import eel
import os
import subprocess
import sys
from queue import Queue
from threading import Thread


class ChatBot:

    started = False
    userinputQueue = Queue()

    def isUserInput():
        return not ChatBot.userinputQueue.empty()

    def popUserInput():
        return ChatBot.userinputQueue.get()

    def close_callback(route, websockets):
        # if not websockets:
        #     print('Bye!')
        exit()

    @eel.expose
    def getUserInput(msg):
        ChatBot.userinputQueue.put(msg)
        print(msg)
    
    def close():
        ChatBot.started = False
    
    def addUserMsg(msg):
        eel.addUserMsg(msg)
    
    def addAppMsg(msg):
        eel.addAppMsg(msg)

    def start():
        path = os.path.dirname(os.path.abspath(__file__))
        eel.init(path + r'\web', allowed_extensions=['.js', '.html'])
        try:
            eel.start('index.html', mode='chrome',
                                    host='localhost',
                                    port=27005,
                                    block=False,
                                    size=(350, 480),
                                    position=(10,100),
                                    disable_cache=True,
                                    close_callback=ChatBot.close_callback)
            ChatBot.started = True
            while ChatBot.started:
                try:
                    eel.sleep(10.0)
                except:
                    #main thread exited
                    break
        
        except:
            pass

# Function to start mouse control
@eel.expose
def startMouseControl():
    # Define the function to launch "mouse-cursor-control.py"
    def launch_mouse_cursor_control():
        script_path = "C:/Users/umang/OneDrive/Desktop/Gesture Based Cursor Navigator/Gesture-Based-Cursor-Navigator/src/mouse-cursor-control.py"
        subprocess.Popen(["python", script_path], shell=True)


    # Launch "mouse-cursor-control.py" in a new thread
    Thread(target=launch_mouse_cursor_control).start()

if __name__ == "__main__":
    ChatBot.start()