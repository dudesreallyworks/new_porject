from django import template

register = template.Library()


@register.filter()
def censor(value):
    censored_words = ['мат', 'плохое слово']
    for word in censored_words:
        value = value.replace(word, '*')
    return value
