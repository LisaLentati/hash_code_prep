from src import bests, read_data


pairs = bests.twos(read_data.read_data('data/b_little_bit_of_everything.in')[4])

print(pairs)
