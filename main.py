'''
Description: Voice assistant to run on a linux platform
Author: Emmanuel Sanchez
Date: 5/13/2020
Python Version 3.6.9
'''


import pyaudio
import wave
import speech_recognition as sr
#calls any terminal instruction
import os
import assortedCommands as AC
import smtplib
from datetime import datetime


#get computer to say stuff
#linux say command requires  gnustep-gui-runtime installation
def say(text):
    os.system('say ' + text)

def play_audio(file):
    chunk = 1024

    #reads as binary 
    wf = wave.open(file, "rb")
    #PyAudio class
    pa = pyaudio.PyAudio()

    #loading sound 
    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate=wf.getframerate(),
        output=True
    )
    #1024 bytes of the file
    data_stream = wf.readframes(chunk)

    #keep reading at the next chink of frames
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)
    #cleanup
    stream.close()
    pa.terminate()

def commandLogic():
    r = sr.Recognizer()

    
    with sr.Microphone() as source:
        play_audio('./audio/start.wav')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration =1)
        
        print ('Listening.......')
        audio = r.listen(source)
    play_audio('./audio/end.wav')
    command = ''


    try:
        command = r.recognize_google(audio)
    except:
        print('Your last command was not understood')
        say('Please repeat your command')
        command = commandLogic()

    if command != '':
        print ('your command')
        print (command)
        return command.lower()
    else:
        pass



def voiceAssistant(command):
    if command in ['quit', 'exit', 'terminate']:
        global running
        running = False


    elif 'send email' in command:
        say('Who is the message going to')
        receiver = commandLogic()

        if 'manny' in receiver:
            say('What is going to be in the email')
            body = commandLogic()

            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()

            user = 'inserthere'
            password = 'inser'


            mail.login(user, password)

            mail.sendmail('Assistant', 'insert contact list', body)

            mail.close()
            say('Email sent')

    elif 'journal entry' in command:

        def makeFile(file_content):

            os.chdir(path)

            fileName = 'Entry_' +dt_string+'.txt'
            fileName = fileName.replace("/", "_")
            fileName = fileName.replace(" ", "_")

            f = open(fileName, 'w')
            f.write(file_content)
            f.close()
            os.chdir('..')
        say('What would you like to enter in this entry')
        journal_content = commandLogic()
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        path = 'journals'
        isdir = os.path.isdir(path)

        if isdir == True:
            makeFile(journal_content)

        else:
            os.system('mkdir '+ path)
            makeFile(journal_content)

    else:
        cmd = AC.Commands()
        cmd.discover(command)

running = True
while running == True:
    voiceAssistant(commandLogic())
