from os.path import dirname

def load_words(file_path):
  """Load words from a text file into a list."""
  with open(file_path, "r") as file:
    words = file.read().splitlines()

  return words

WORDS_LIST = load_words(f"{dirname(__file__)}/wordlist.txt")
