## tests.py ##
import sequence
# Create an instance of the Sequence class.
test_sequence1 = sequence.Sequence('ACGT')
test_sequence2 = sequence.Sequence('TGCA')
test_sequence3 = sequence.Sequence('')
test_sequence4 = sequence.Sequence('Z')
test_sequence5 = sequence.Sequence('ACGTGCG')
test_sequence6 = sequence.Sequence('ACGTTCG')

# Test method length number of bases
# non-zero length and zero length
Number_of_bases_1 = test_sequence1.length()
Number_of_bases_2 = test_sequence3.length()
if Number_of_bases_1 == 4:
    print('Pass')
else:
    print('Fail')
if Number_of_bases_2 == 0:
    print('Pass')
else:
    print('Fail')


# Test method is_dna()
# not valid DNA base e.g Z
# zero length -> False

DNA_base_1 = test_sequence4.is_dna()
DNA_base_2 = test_sequence4.is_dna()

if DNA_base_1 == False:
    print('Pass')
else:
    print('Fail')
if DNA_base_2 == False:
    print('Pass')
else:
    print('Fail')

# Test the complement method
# A becomes a T, and every C a G – and vice-versa 
# Do not reverse the complement sequence.

Seq_complement_1 = test_sequence1.complement()
Seq_complement_2 = test_sequence2.bases

if Seq_complement_1 == Seq_complement_2:
    print('Pass')
    
else:
    print('Fail')
if Seq_complement_2 == Seq_complement_2[::-1]:
    print('Fail')
else:
    print('Pass')


# Test compare method
# Comparing sequences ACGTGCG and ACGTTCG returns 4.
# Return -1 if the sequences are identical (or empty). 

Seq_compare_1 = test_sequence5.compare(test_sequence6)
Seq_compare_2 = test_sequence3.compare(test_sequence3)
if Seq_compare_1 == 4:
    print('Pass')
else:
    print('Fail')
if Seq_compare_2 == -1:
    print('Pass')
else:
    print('Fail')