from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    bad_words = [
        'fuck', 'piss',
        'bastard', 'wanker',
        'bollocks', 'shit',
        'whore'
    ]
    text = set(value.split())
    for word in text:
        for bad_word in bad_words:
            if word == bad_word:
                return value.replace(word, '*' * len(word))

        return value


