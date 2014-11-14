#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymongo
from pymongo import MongoClient
#from bson.objectid import ObjectId
import datetime
from scapy.all import *
import threading
from Tkinter import *

#############################################
################### GUI #####################
#############################################

def gui():
    global pktCount
    root = Tk()
    bgColor = '#000000'
    root.configure(bg=bgColor)
    root.geometry("500x300")
    title = "Packet Sniffer"
    label = Label(root, text=title, font=("ubuntu mono", 12), fg="green", bg="black")
    label.pack()
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    def quitCallBack():
        root.destroy()
    text = Text(root, bg="Black", fg="Green")
    text.insert(INSERT, pktCount)
    text.pack()
    button = Button(root, text ="quit", command = quitCallBack)
    button.pack(side=BOTTOM)
    root.mainloop()
#############################################
#############################################

#MONGODB STUFF
#Connect to the database at mongolab.com
#client = MongoClient('mongodb://technoxaman:tiger_vs_dragon@ds051640.mongolab.com:51640/thesis_prototype_1')
client = MongoClient('mongodb://localhost:27017')
db = client.thesis_prototype_1
#connect to the collection
collection = db.data_consume
#clean stored data when the application starts
collection.remove()

#############################################
############### Main loop ###################
#############################################
pktCount = 0
pktCountLimit = 0
totalSummary = ""
def mainThread():
    def callback(pkt):
        if pkt.haslayer(TCP):
            global pktCount
            global pktCountLimit
            global totalSummary
            #print pkt.summary()
            # print pkt.show()
            # print pkt[TCP]
            totalSummary += pkt.summary() + "\n"
            pktCount += 1
            pktCountLimit += 1
            print pktCount, "Packets in total"
            if pktCountLimit >= 1000:
                data = {
                    'pkgCount'  : pktCount,
                    'summary'   : totalSummary
                }
                print totalSummary
                collection.insert(data) #Write the packet count and summary to the DB
                totalSummary = ""
                pktCountLimit = 0

    sniff(filter="port 80", prn=callback, store=0, iface='eth1')
#############################################
#############################################

#############################################
###############THREADS#######################
#############################################
"""
#THREAD FOR TKINTER GUI
guiStart = threading.Thread(target=gui)
guiStart.daemon = True
guiStart.start()
"""

#SNIFFING THREAD
mainStart = threading.Thread(target=mainThread)
mainStart.daemon = True
mainStart.start()

try:
    while True:
        mainStart.join(1)
        #guiStart.join(1)
except KeyboardInterrupt:
    print "^C is caught, exiting"
#############################################
#############################################



"""
def get(post_id):
    document = db.data_consume.find_one({'_id': ObjectId(post_id)})
    document.update(dataUpdate)
    print document

get('54614021f76d425a40814232')

data = {
                'pkgCount': pkgCount,
                'packets':
                [{
                    'packet_1': {
                        'ip': '192.168.1.1',
                        'ammount': 1000
                    },
                    'packet_2': {
                        'ip': '194.100.1.6',
                        'ammount': 3000
                    }
                }]
            }
"""
