#!/usr/bin/env python3
import telnetlib, time,threading,re
import sys

device={}

class ampControl():

    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.timer = None
        self.conn =  telnetlib.Telnet()

    def connect(self):
        self.start_timer()
        self.conn.open(self.ip, self.port, 3)
        print("[CONNECTED]")
        return self.conn

    def disconnect(self):
        self.conn.close()
        print("Disconnected")
        self.timer.cancel()
        self.timer = None

    def start_timer(self):
        self.timer = threading.Timer(10, self.disconnect)
        self.timer.start()

    def reset_timer(self):
        print("Resetting timer.")
        self.timer.cancel()
        self.start_timer()

    def send_command(self,command):
        t = self.connect()
        t.write(command.encode())
        self.disconnect()
       
    def set_mute(self,onoff):
        if onoff.upper() not in ["ON", "OFF"]:
           print("bad mute:",onoff)
           return "INVALID"
        self.send_command("MU" + onoff.upper() +"\r")
        return "OK"

    def set_power(self,onstandby):
        if onstandby.upper() not in ["ON", "STANDBY"]:
           print("bad power:",onstandby)
           return "INVALID"
        self.send_command("PW" + onstandby.upper() +"\r")
        return "OK"

    def set_input(self,input):
        if input.upper() not in [ "USB", "TUNER","V.AUX","MPLAY"]:
           print("bad input:",input)
           return "INVALID"
        self.send_command("SI" + input.upper() +"\r")
        return "OK"

    def set_volume(self,level):
        if level.upper() not in [ "UP", "DOWN"]:
          if re.search(r'[0-9][0-9]',level) == None:
             print("bad input:",input)
             return "INVALID"
        self.send_command("MV" + level.upper() +"\r")
        return "OK"


#main()

amp = ampControl("192.168.1.56",23)

#amp.set_mute("on")

#time.sleep(5)

#amp.set_mute("off")

#time.sleep(5)

#amp.set_volume("up")

#time.sleep(5)

#amp.set_volume("down")

#time.sleep(5)

#amp.set_input("MPLAY")

#time.sleep(5)

#amp.set_input("V.AUX")

#time.sleep(5)

#amp.set_volume("10")

#time.sleep(5)

#amp.set_volume("50")

#time.sleep(5)

amp.set_power("standby")
