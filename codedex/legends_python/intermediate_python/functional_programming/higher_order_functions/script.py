"""

Instructions
If you're on Duolingo, this exercise is for you! 🦉

Let's use higher-order functions to translate some common phrases from different languages.

First, define a translator() function that takes a single language parameter.

Inside the function, add a translations dictionary that contains translations for common phrases in different languages:

translations = {
  'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
  'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
  'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
}

Next, define an inner translate_word() function that takes a word parameter and returns a translation if the word exists in a specific language.

Return the inner translate_word() function from the outer translator() function.

Finally, let's test our translator() function with different languages:

translate_to_spanish = translator('spanish')
print(translate_to_spanish('hello')) # Output: hola

"""


def translator(lang):
  translations = {
  'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
  'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
  'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
}
  def translate_word(word):
    if word.lower() in translations[lang]:
      return translations[lang][word.lower()]
    else:
      return f"Translation not available"

  return translate_word # return inner function

translate_to_spanish = translator('spanish')
print(translate_to_spanish('hello')) # Output: hola

translate_to_french = translator('french')
print(translate_to_french('hello'))  # Output: bonjour

translate_to_italian = translator('italian')
print(translate_to_italian('good night')) # translation not available
