from googletrans import Translator
from . import SERVICE_URLS


class Word:
    def __init__(self, word: str):
        self.__word = word.lower()

    def fetch(self):
        translator = Translator(service_urls=SERVICE_URLS)

        rep = translator.translate(self.__word, src="en", dest="zh-cn")

        self.means = {}
        for o in rep.extra_data['all-translations']:
            self.means[o[0]] = []
            for j in o[2]:
                s = ""
                s += j[0] + "  " + "[ "
                for k in j[1]:
                    s += str(k) + "/"
                s += " ]"
                self.means[o[0]].append(s)

    def get_means(self):
        return self.means
