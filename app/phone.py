#!/usr/bin/env python3
"""
phone.py - Interface application with telephones
"""

from flask import Blueprint, session, url_for, request
from twilio.twiml.voice_response import VoiceResponse, Gather
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import hashlib
import json
from app import app

phone = Blueprint("phone", __name__)


@phone.route("/voice", methods=['GET', 'POST'])
def answer_call():
    """Interface between service and telephone"""
    response = PhoneInterface()
    response.accept_call()

    # New session
    response.next('chatbot.greeting')
    # if 'status' not in session:
    #     # chatbot.speak/listenbot.listen
    #     session['status'] = 'chatbot.speak'

    # Connect to chatbot/listenbot
    # response.next(session['status'])

    # Read a message aloud to the caller
    # response.say('Bye.', voice='alice')
    return str(response)


class PhoneInterface(VoiceResponse, MessagingResponse):

    def get_my_number(self):
        if request:
            return request.values.get('To')
        return ''

    def get_incoming_number(self):
        if request:
            return request.values.get('From')
        return ''

    def get_user_id(self):
        if 'user_id' not in session:
            self.speak('The call has not been accepted.')
        return session['user_id']

    def accept_call(self):
        if self.get_incoming_number():
            session['user_id'] = hashlib.sha224(
                self.get_incoming_number().encode('utf-8')).hexdigest()

    def end_call(self):
        self.hangup()

    def next(self, endpoint):
        self.redirect(url=url_for(endpoint), method='GET')

    def speak(self, text):
        self.say(text, voice='alice', language='en')

    def listen(self, endpoint, hint=None):
        # session['forward'] = endpoint
        action = url_for(endpoint)
        if hint:
            gather = Gather(input='speech', action=action, hints=hint)
        else:
            gather = Gather(input='speech', action=action)
        self.append(gather)
        self.next(endpoint)
        # self.record(
        #     action=action,
        #     method='GET',
        #     transcribe=True
        # )
        # self.speech_queue[endpoint] = None

    def reply(self, text):
        """Reply to the current number"""
        self.message(text)

    def send(self, text, to_num=None):
        """Send a SMS to a different number"""
        ACCOUNT_SID = 'ACdab50f233a93d277f7518b830148d5cb'
        AUTH_TOKEN = 'caacae6e1da3561db5152c870c4b6f63'
        if not self.client and ACCOUNT_SID and AUTH_TOKEN:
            self.client = Client(ACCOUNT_SID, AUTH_TOKEN)
        if not to_num:
            to_num = self.incoming_number
        self.client.api.account.messages.create(
            to=to_num,
            from_=my_number,
            body=text)

    def receive(self):
        """Mock mFarm response"""
        pass

    def transcribe(self):
        if request.values.get('AddOns'):
            add_ons = json.loads(request.values['AddOns'])

            # If the Watson Speech to Text add-on found nothing, return immediately
            if 'ibm_watson_speechtotext' not in add_ons['results']:
                return 'Add Watson Speech to Text add-on in your Twilio console'

            payload_url = add_ons["results"]["ibm_watson_speechtotext"]
            if payload_url.get('status') == 'failed':
                self.speak('I did not hear that. Would you please say it again?')
                self.end_call()
            # ["payload"][0]["url"]

            # resp = requests.get(payload_url, auth=(
            #     self.ACCOUNT_SID, self.AUTH_TOKEN)).json()

            # results = resp['results'][0]['results']
            # transcripts = map(lambda res: res['alternatives'][0]['transcript'], results)

            # raise ValueError(''.join(transcripts))
        return ''

    def repeat(self):
        recording_url = request.values.get("RecordingUrl", None)
        print(recording_url)
        self.speak("You said")
        self.play(recording_url)
        self.say("Correct.")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
