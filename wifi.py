import subprocess
from wireless import Wireless
import stdiomask
from getpass import getpass


class Wifi:
    def find_best_wifi(self):
        '''
        description: This function is used to find the available networks which is
        stored in devices_data. The user gets to choose the wifi he/she wants to
        connect with and provide the password for the same.
        :return: not required
        '''

        # Fetching network term retrival
        devices_data = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])

        # Converting data to String
        devices_data = devices_data.decode('ascii')
        devices_data = devices_data.replace("\r", "")

        network = []

        lines = devices_data.split("\n")
        for line in lines:
            if "SSID" in line:
                network.append(line.split(":")[1])

        connect_wifi = subprocess.check_output(['netsh', 'wlan', 'show', 'interface'])
        connect_wifi = connect_wifi.decode('ascii')
        connect_wifi = connect_wifi.replace("\r", "")

        i=1
        for wifi in network:
            print("[" + str(i) + "] " + wifi)
            i = i + 1

        print("Your choice?")
        select_wifi = input()

        wire = Wireless('wlan1')
        passwd = stdiomask.getpass(mask='*')
        status = wire.connect(ssid=network[int(select_wifi)-1], password=passwd)
        if status == True:
            print("connected!")
        else:
            print("Incorrect password!")


w = Wifi()
w.find_best_wifi()

