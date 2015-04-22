#!/bin/python2
import sys
#from notify.all import *
from gi.repository import Notify
import pyinotify
import math
def notify():
	fp=open("/home/notify.txt","r+")
	fp.write("This is a watch notify project\n");
	fp=open("/home/notify.txt","r+")
	str=fp.read(30);
	print "The string read is: ",str
	fp.close()
def fileoperations():
	fip=open("/home/ops.txt","r+")
	fip.write("I am a big fan of Liverpool\nHello World\nMy name is Tanay\n");
	fip=open("/home/ops.txt","r+")
	str=fip.read(10);
	print "\nstr"
	position=fip.tell();
	print "Position is ",position
	position=fip.seek(0,0)
	print "Again Position is ",position
	fip.close()
def pynotify():
	wm = pyinotify.WatchManager()
	notifier=pyinotify.Notifier(wm)
	
if __name__=="__main__":
	notify()
	fileoperations()
	pynotify()
