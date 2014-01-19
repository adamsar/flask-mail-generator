#!/usr/bin/python  # -*- encoding: utf-8 -*-
"""Wikipedia api utility functions"""


import wikipedia
import random

#Stop words that mark a sentence as invalid
STOP_WORDS = [
    "==",
    "External links"
    ]

wikipedia.set_lang("ja")

def to_system_format(page):
    """Convert wikipedia page to the internal content type"""
    
    sentences = [s + u"。" for s in page.content.split(u"。")]
    
    #Get the first valid random sentence 
    def valid_sentence(sentence):
        return reduce(lambda x, y: x and y,
                      map(lambda word: word not in sentence, STOP_WORDS))
    #Give it 10 tries to get a random sentence. Otherwise discard it.
    random_sentence = None
    for x in xrange(0, 10):
        random_sentence = sentences[random.randint(0, len(sentences) - 1)]
        if valid_sentence(random_sentence):
            break
        
    return {
        'title': page.title,
        'url': page.url,
        'full_text': page.content,
        'random_sentence': random_sentence
        }

def read_random_from_topic(topic = None):
    """Reads from a topic (or random topic if not specified), and returns
    an internal content type that includes a random sentence"""
    
    if not topic:
        topic = wikipedia.random()
    content = wikipedia.page(topic)
    return to_system_format(content)
