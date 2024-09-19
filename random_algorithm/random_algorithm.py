import time
import random
from .words_list import WORDS_LIST

def shuffle_words():
  """Shuffle the word list to ensure randomness on each call."""
  random.shuffle(WORDS_LIST)

def get_random_index():
  """Generate a random index based on the current time."""
  current_time = time.time()
  index = int(current_time * 1000) % len(WORDS_LIST)  # Multiply for higher precision

  return index

def ascii_reduce(word, index):
  """Reduce a word's ASCII values to a single number."""
  def reduce_to_single_digit(n):
    while n >= 10:
      n = sum(int(digit) for digit in str(n))
    return n

  ascii_values = [ord(char) for char in word]  # Convert each character to its ASCII value
  reduced_digits = [reduce_to_single_digit(value) for value in ascii_values]  # Reduce each ASCII value to a single digit

  total_sum = sum(reduced_digits)  # Sum all the reduced digits
  final_value = reduce_to_single_digit(total_sum)  # Reduce the total sum to a single digit

  current_time = int(time.time())
  if (current_time * index) % final_value == 0:
    final_value = int(str(current_time * final_value)[-1])  # Take the last digit to ensure values like 0 and 1 are included

  return final_value

def gen_random(desired_size):
  """Main function to generate a random number of the desired size."""
  if not isinstance(desired_size, int):
    raise TypeError("Desired size must be an integer")
  if desired_size < 1:
    raise ValueError("Desired size must be at least 1")
  final_value = ""

  for _ in range(desired_size):
    shuffle_words()
    index = get_random_index()
    word = WORDS_LIST[index]

    final_value += str(ascii_reduce(word, index))
  
  return int(final_value)
