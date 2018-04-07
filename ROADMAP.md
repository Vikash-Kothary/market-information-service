# Road Map

## Project Setup

### Documentation
- [x] Readme
- [x] License
- [x] Changelog
- [x] Roadmap

### Docker support
- [x] Dockerfile
- [x] Docker compose

### Python application
- [x] Python files
- [x] Requirements file

### Continous Integration
- [x] Setup Travis CI

### Scripts
- [ ] Install (From Docker Hub)
- [ ] Run (From Docker Hub)
- [x] Develop (Build + Run local)
- [x] Test
- [ ] Release (To Github)
- [x] Release (To Docker Hub)
- [ ] Release (To Heroku)

### Ngrok
- [ ] Ngrok docker

## Minimum Viable Product v0.0.0
 
### CLI
> http://www.patricksoftwareblog.com/unit-testing-a-flask-application/
> https://damyanon.net/post/flask-series-testing/
> https://pythonhosted.org/Flask-Testing/
> https://github.com/colingorrie/flask-boilerplate/blob/master/tests/__init__.py
- [ ] Unit Tests Framework
- [ ] Input text field
- [ ] Output text area 

### Natural Language Understanding
> https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/
> https://dzone.com/articles/nlp-tutorial-using-python-nltk-simple-examples
- [x] Define a model for the data queries/reponses
- [x] Setup NLTK
- [x] Tokenise
- [x] Noice Removal
> https://nlp.stanford.edu/IR-book/html/htmledition/dropping-common-terms-stop-words-1.html
- [x] Lexicon Normalisation
- [?] Object Standardisation
- [x] Part of speech tagging
- [ ] Dependency trees
- [ ] Generate json query

## Minimum Viable Product v0.1.0

### Natural Language Generation
- [ ] Mock json query response
- [ ] Represent the response as a sentence

## Phone v0.2.0 

### Twilio
- [ ] Setup Twilio
- [ ] Test receive phone call
- [ ] Test receive speech through phone call
- [ ] Test reply speech through phone call
- [ ] Test recognise phone number
- [ ] Receive multiple phone calls at the same time
- [ ] Add to queue of waiting calls?

### SMS
- [ ] Mock send SMS to mFarm

## Chatbot v0.3.0

### Chatbot
> https://medium.com/@allanmeriales/a-simple-chatbot-using-nltk-chat-640456dcdf72
> https://chatbotsmagazine.com/delbot-nlp-python-bot-1a46d865e38b
> https://apps.worldwritable.com/tutorials/chatbot/
- [x] Greeting
- [x] Talkback (because it may have misheard the speech)
- [ ] Ignore filler words such as 'umm' and 'hmm'

## Memory v0.4.0

### User Sessions
- [x] User model
- [ ] Mock phone numbers
- [ ] Remember user's name
- [ ] Remember currency and location of user 
- [ ] Store search history
- [ ] Ask for more information if not enough given

### Privacy
- [ ] Store phone number as hash


## Future v0.5.0


### Extensions
- [ ] Multiple queries in one call
- [ ] Multiple queries in one sentence
- [ ] Edit the query (correct themselves)

### Tests
- [ ] Test response time

### Web Speech API
- [ ] Speech Recognition
- [ ] Test receive
- [ ] Speech Synthesis