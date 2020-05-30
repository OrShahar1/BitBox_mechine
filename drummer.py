import time
import threading
from playsound import playsound

class Bitbox:
      def __init__(self , name_file):
            self.name_file = name_file

      def runSound(self, name):
            playsound("{name}.wav".format(name=name))

      def play(self):
            while True:
                  with open(self.name_file, newline='') as f:
                        reader = f.read()
                        for row in reader:
                              row_clen = row.split()
                              for step in row_clen:
                                    s_thread = threading.Thread(target=self.runSound, args=(), kwargs={"name":step})
                                    s_thread.start()
                                    time.sleep(0.25)
            f.close()

def main():
      x = Bitbox("sequenser.txt")
      x.play()

main()

