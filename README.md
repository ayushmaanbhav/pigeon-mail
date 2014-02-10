# PIGEON ![](http://www.ju2framboise.com/wp-content/uploads/2013/10/pigeon-voyageur.png "Pigeon")

## Introduction
Basic text mail delivering library in python.Contains all commands to connect to network mailserver and send mail through it.Only text mails are supported.Telnet commands are built as functions.It has a gui component for basic demonstration.

## Requirements
* Python-dev package
* Python-tk ( GUI component )
* Tcl and Tk 5.6
* Python-distutils-extra ( installation and build )

## Installation 
__Make sure the requirements are satisfied before installing__
* Goto the libs folder and run `python setup.py install`
* For running the gui, goto the gui folder and  type `python mlc.py`

## Demo 

### Code for sending a small mail
```python
import pigeon
t = pigeon.pigeon("<network mailserver address>")
print t #check t for return codes and handling errors
t = pigeon.sayHello("<domain>")
print t #check t for return codes and handling errors
t = pigeon.msgFrom("<senders mail address>")
print t #check t for return codes and handling errors
t = pigeon.rcptTo("<recipient mail address>")
print t #check t for return codes and handling errors
pigeon.beginData() #start sending data
pigeon.writeData("<data>") 
t = pigeon.sendMsg()
print t #check t for return codes and handling errors
```

You can also try the gui which shows the same msg recieved from network when the following communications are being made.

##Bugs/Suggestions
Would love to hear about any suggestions or improve any bugs cuz this was just a small tutorial to build a python library.Drop in a mail at saswatrj2010@gmail.com



