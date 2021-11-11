## client.py ##
import sequence
# Create an instance of the Sequence class.
example_sequence1 = sequence.Sequence('ACGTGCG')
example_sequence2 = sequence.Sequence('ACGTTCG')

# Return the number of bases
Number_of_bases = example_sequence1.length()
print(f'The number of DNA bases: {Number_of_bases}')

# Validate if the characters are valid DNA bases: A,T, C or G.
Check_DNA_bases = example_sequence1.is_dna()
print(f'The characters are valid DNA bases: {Check_DNA_bases}')

# Return the complement of the Sequence
Complement_of_sequence = example_sequence1.complement()
print(f'The complement of the sequence: {example_sequence1.bases} is the sequence: {Complement_of_sequence}')

# Return the zero-based index of the first non-matching base
Compare_two_sequences = example_sequence1.compare(example_sequence2)
print(f'The zero-based index of the first non-matching base is: {Compare_two_sequences}')
