# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def some_jokes(n, repeat=False):
   list_of_jokes = []
   for i in range(0, n):
      if repeat and len(nouns) == 0:
         break
      nouns_select = choice(nouns)
      adverbs_select = choice(adverbs)
      adjectives_select = choice(adjectives)
      list_of_jokes.append(f"{nouns_select}, {adverbs_select}, {adjectives_select}")
      if repeat:
         nouns.remove(nouns_select)
         adverbs.remove(adverbs_select)
         adjectives.remove(adjectives_select)
   return list_of_jokes


print(some_jokes(7, True))