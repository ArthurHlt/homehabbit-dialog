from tts_watson.TtsWatson import TtsWatson
from dialog_watson_client.Client import Client
from stt_watson.SttWatson import SttWatson
from homehabbit_dialog.HomeHabbitListener import HomeHabbitListener
import anyconfig
import bunch


def main():
    conf = anyconfig.load('config.yml')
    bconf = bunch.bunchify(conf)
    print bconf['watson-dialog'].user
    watsonDialogClient = Client(bconf['watson-dialog'].user, bconf['watson-dialog'].password, "dialogs/homehabbit.xml",
                                "homehabbit")
    ttsWatson = TtsWatson(bconf['watson-tts'].user, bconf['watson-tts'].password, bconf['watson-tts'].voice)
    homeHabbitListener = HomeHabbitListener(watsonDialogClient, ttsWatson)
    resp = watsonDialogClient.start_dialog()
    ttsWatson.play(resp.response)

    sttWatson = SttWatson(bconf['watson-stt'].user, bconf['watson-stt'].password, model=bconf['watson-stt'].model,
                          rate=bconf['watson-stt']['audio-rate'],
                          chunk=bconf['watson-stt']['audio-chunk'],
                          channels=1)
    sttWatson.addListener(homeHabbitListener)
    sttWatson.run()


main()
