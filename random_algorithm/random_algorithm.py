import itertools
import random
import time
from .words_list import WORDS_LIST


def shuffle_words():
    """
    Shuffle the word list to ensure randomness on each call.
    The only call to the built-in random :)

    :return: Nothing.
    :rtype: None
    """

    random.shuffle(WORDS_LIST)


def reduce_to_single_digit(n):
    """
    Reduce a number to a single digit by repeatedly summing its digits.

    This function takes an integer `n` and repeatedly sums its digits until
    the result is a single digit. For example, if the input is 9875, the
    function will compute 9 + 8 + 7 + 5 = 29, then 2 + 9 = 11, and finally
    1 + 1 = 2. The function will return 2.

    :param int n: The number to reduce.

    :return: The reduced number.
    :rtype: int
    """

    while n >= 10:
        n = sum(int(digit) for digit in str(n))

    return n


def ascii_reduce(word, index):
    """
    Reduce a word's ASCII values to a single number.

    This function takes a word and an index, converts each character in the word
    to its ASCII value, reduces each ASCII value to a single digit, and then sums
    these reduced digits. The total sum is further reduced to a single digit.
    Additionally, the function uses the current time and the provided index to
    potentially modify the final reduced value.

    The steps are as follows:
    1. Convert each character in the word to its ASCII value.
    2. Reduce each ASCII value to a single digit by summing its digits repeatedly.
    3. Sum all the reduced digits.
    4. Reduce the total sum to a single digit.
    5. Use the current time and the provided index to potentially modify the final value.
       - If the product of the current time and index is divisible by the final value,
         the final value is replaced by the last digit of the product of the current time
         and the final value.

    :param str word: The word to convert.
    :param int index: The index to use in the calculation.

    :return: The final reduced single digit value.
    :rtype: int
    """

    # Convert each character to its ASCII value and reduce to a single digit
    ascii_values = [ord(char) for char in word]
    reduced_digits = [reduce_to_single_digit(value) for value in ascii_values]

    total_sum = sum(reduced_digits)
    final_value = reduce_to_single_digit(total_sum)

    # Randomly take the last digit to ensure values like 0 and 1 can be included
    current_time = int(time.time())
    if (current_time * index) % final_value == 0:
        final_value = int(str(current_time * final_value)[-1])

    return final_value


def get_time_seed():
    """
    Create a seed based on reduction of the current time.

    This function generates a seed value by performing the following steps:
    1. Obtain the current time in seconds since the epoch and multiply it by 10,000,000 for higher precision.
    2. Convert the current time to a string and ensure it is at least 17 digits long by padding with zeros if necessary.
    3. Split the string into chunks of 2 to 4 digits in the following order: first 3 digits, next 2 digits, next 4 digits, next 2 digits, next 3 digits, and the last 3 digits.
    4. Convert each chunk to its corresponding ASCII character.
    5. Generate all possible permutations of these characters.
    6. Concatenate the characters in each permutation to form words.
    7. Calculate an index by summing the digits of the current time string.
    8. For each permutation word, pass it to the `ascii_reduce` function along with the index and sum the results.
    9. Return the total sum of all results.

    :return: The calculated seed value.
    :rtype: int
    """

    # Multiply for higher precision
    current_time = int(time.time() * 10000000)
    # Ensure the string is always long enough
    current_time_str = str(current_time).zfill(17)

    # Split the string into chunks of 2 to 4 digits
    chunks = [
        current_time_str[0:3],
        current_time_str[3:5],
        current_time_str[5:9],
        current_time_str[9:11],
        current_time_str[11:14],
        current_time_str[14:17],
    ]

    # Convert each chunk to its corresponding character
    characters = [chr(int(chunk)) for chunk in chunks]

    # Generate all possible permutations of these characters
    permutations = list(itertools.permutations(characters))
    permutations_words = ["".join(perm) for perm in permutations]
    index = sum(int(digit) for digit in current_time_str)

    total_sum = 0
    for perm in permutations_words:
        total_sum += ascii_reduce(perm, index)

    return total_sum


def get_random_index():
    """
    Generate a random index based on the current time's seed.

    :return: The calculated index.
    :rtype: int
    """
    index = get_time_seed() % len(WORDS_LIST)

    return index


def gen_random(desired_size):
    """
    Generate a random number of the desired size.

    This function generates a random number of the specified size by performing the following steps:
    1. Initialize an empty string `final_value` to store the generated random number.
    2. For each iteration up to `desired_size`:
       - Call `shuffle_words()` to shuffle the `WORDS_LIST`.
       - Generate a random index using `get_random_index()`.
       - Retrieve the word at the generated index from `WORDS_LIST`.
       - Pass the word and index to `ascii_reduce()` to get a reduced value.
       - Append the reduced value to `final_value`.
    3. Ensure the final value has the desired size by adding random digits if necessary.
       - Use `get_time_seed() % 17` to generate a random digit and append it to `final_value`.
       - Repeat until the length of `final_value` (excluding leading zeros) is at least `desired_size`.
    4. Convert `final_value` to an integer and return it.

    :param int desired_size: The size of the random number to generate.

    :return: The generated random number.
    :rtype: int

    :raises TypeError: If desired_size is not an integer.
    :raises ValueError: If desired_size is less than 1.
    """

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

    # Add a random digit to ensure the final value has the desired size
    while len(final_value.lstrip("0")) < desired_size:
        final_value += str(get_time_seed() % 17)[:1]

    return int(final_value)
