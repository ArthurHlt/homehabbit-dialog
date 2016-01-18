from stt_watson.SttWatsonAbstractListener import SttWatsonAbstractListener


class HomeHabbitListener(SttWatsonAbstractListener):
    def __init__(self, watsonDialogClient, watsonTts):
        self.watsonDialogClient = watsonDialogClient
        self.watsonTts = watsonTts
        self.lock = False

    def listenHypothesis(self, hypothesis):
        if self.lock:
            return
        print "Hypothesis: {0}".format(hypothesis)
        self.lock = True
        resp = self.watsonDialogClient.converse(hypothesis[0]['transcript'])
        print "Your profile:"
        for name, value in self.watsonDialogClient.get_profile().get_data().iteritems():
            print "\t" + name + ": " + value
        self.watsonTts.play(resp.response)
        self.lock = False

    def listenPayload(self, payload):
        pass

    def listenInterimHypothesis(self, interimHypothesis):
        pass
