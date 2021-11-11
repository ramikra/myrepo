## client.py ##
import sequence
# Create an instance of the Sequence class.
example_sequence1 = sequence.Sequence('AGCT')
example_sequence2 = sequence.Sequence('CCCC')
# Call the first_base method on our instance.
example_first_base = example_sequence1.first_base()
print(f'The first base is: {example_first_base}')
# TODO add method calls to complete the tasks
example_second_base = example_sequence2.complement()
print(f'The first base is: {example_second_base}')
