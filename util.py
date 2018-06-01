import subprocess
import time
BASE_MONKEY_COMMAND = open('raw_command.txt').read()


def run_monkey():
    temp = subprocess.Popen(BASE_MONKEY_COMMAND, shell=True)
    time.sleep(1)
    temp.terminate()


def stop_monkey():
    subprocess.run('adb shell reboot', shell=True)
