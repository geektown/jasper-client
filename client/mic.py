# -*- coding: utf-8-*-
"""
    The Mic class handles all interactions with the microphone and speaker.
"""
import logging
import tempfile
import wave
import audioop
import pyaudio
import alteration
import jasperpath
import os

class Mic:

    speechRec = None
    speechRec_persona = None

    def __init__(self, speaker, passive_stt_engine, active_stt_engine):
        """
        Initiates the pocketsphinx instance.

        Arguments:
        speaker -- handles platform-independent audio output
        passive_stt_engine -- performs STT while Jasper is in passive listen
                              mode
        acive_stt_engine -- performs STT while Jasper is in active listen mode
        """
        self._logger = logging.getLogger(__name__)
        self.speaker = speaker
        self.passive_stt_engine = passive_stt_engine
        self.active_stt_engine = active_stt_engine
        self._logger.info("Initializing PyAudio. ALSA/Jack error messages " +
                          "that pop up during this process are normal and " +
                          "can usually be safely ignored.")
        self._audio = pyaudio.PyAudio()
        self._logger.info("Initialization of PyAudio completed.")

    def __del__(self):
        self._audio.terminate()

    def getScore(self, data):
        rms = audioop.rms(data, 2)
        score = rms / 3
        return score


    def passiveListen(self, PERSONA):
        os.system("arecord -d 2 -r 16000 -f S16_LE -D plughw:1,0 /run/shm/001.wav")
        transcribed = self.passive_stt_engine.transcribe(file('/run/shm/001.wav'))
        print transcribed
        #print "check passiveListen for " , PERSONA.decode('utf-8')
        THRESHOLD = 1200
        for p in PERSONA.split("|"):
            if any(p.decode('utf-8') in phrase for phrase in transcribed):
                return (THRESHOLD, p)
        
        return (False, transcribed)

    def activeListen(self, THRESHOLD=None, LISTEN=True, MUSIC=False):
        """
            Records until a second of silence or times out after 12 seconds

            Returns the first matching string or None
        """

        options = self.activeListenToAllOptions(THRESHOLD, LISTEN, MUSIC)
        if options:
            return options[0]

    def generalListen(self, THRESHOLD=1000, LISTEN=True, MUSIC=False):
        """
            通用对话模式下主动监听，监听的所有内容都交给后台的状态机处理。
        """

        options = self.activeListenToAllOptions(THRESHOLD, LISTEN, MUSIC)
        return options            
            
            
    def activeListenToAllOptions(self, THRESHOLD=None, LISTEN=True,
                                 MUSIC=False):
        
        self.speaker.play(jasperpath.data('audio', 'beep_hi.wav'))

        os.system("arecord -d 4 -r 16000 -f S16_LE -D plughw:1,0 /run/shm/001.wav")
        self.speaker.play(jasperpath.data('audio', 'beep_lo.wav'))
        transcribed = self.passive_stt_engine.transcribe(file('/run/shm/001.wav'))
        print '#'.join(transcribed)
        return transcribed

    def say(self, phrase,
            OPTIONS=" -vdefault+m3 -p 40 -s 160 --stdout > say.wav"):
        # alter phrase before speaking
        phrase = alteration.clean(phrase)
        self.speaker.say(phrase)
        
    def playMP3(self, mp3):
        os.system('omxplayer --no-osd ' + mp3)
