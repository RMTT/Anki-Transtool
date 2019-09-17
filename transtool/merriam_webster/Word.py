import requests
from . import KEY, AUDIO_URL
import json


class Word:
    def __init__(self, word: str):
        self.__word = word.lower()

    def __audio_file(self, id: str):
        subdirectory = self.__word[0]
        if self.__word.startswith("bix"):
            subdirectory = "bix"
        elif self.__word.startswith("gg"):
            subdirectory = "gg"
        elif self.__word[0].isdigit():
            subdirectory = "number"

        return AUDIO_URL % (subdirectory, id)

    def fetch(self):
        req = requests.get(url="https://www.dictionaryapi.com/api/v3/references/collegiate/json/%s" % self.__word,
                           params={
                               "key": KEY
                           })
        rep = json.loads(req.text)[0]
        self.mw = ""
        self.audio = {}
        for o in rep['hwi']['prs']:
            if self.mw != "":
                self.mw += ','
            self.mw += o['mw']

            if 'sound' in o:
                self.audio[o['sound']['audio']] = self.__audio_file(o['sound']['audio'])

    def get_mw(self):
        return self.mw

    def get_audio(self):
        return self.audio
