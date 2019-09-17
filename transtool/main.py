from transtool.google_translate.Word import Word as GW
from transtool.merriam_webster.Word import Word as MW
import sys, os
from jinja2 import Environment, FileSystemLoader
from transtool.anki.operation import add_card, add_media
import requests
import base64


def run():
    word = sys.argv[1]
    dir_source = os.path.dirname(os.path.abspath(__file__))
    dir_templates = dir_source
    jinja_env = Environment(loader=FileSystemLoader(dir_templates))

    gw = GW(word=word)
    mw = MW(word=word)

    gw.fetch()
    mw.fetch()

    front = jinja_env.get_template("front.md")
    back = jinja_env.get_template("back.md")

    # download audio
    for k in mw.get_audio():
        rep = requests.get(mw.get_audio()[k])

        add_media(b64=str(base64.b64encode(rep.content), encoding="utf-8"), filename="%s.wav" % k, version=6)
    front_str = front.render(word=word, mw=mw.get_mw(), audios=mw.get_audio().keys())
    back_str = back.render(means=gw.get_means())

    add_card('Vocabulary-toefl-practices', model_name="Basic (and reversed card)", version=6, front=front_str,
             back=back_str)


if __name__ == "__main__":
    run()
