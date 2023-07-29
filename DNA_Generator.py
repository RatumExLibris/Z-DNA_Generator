import numpy as np
import tensorflow as tf

# Instantiate the DNA generator model
sequence_length = 128
num_nucleotides = 4

dna_generator_model = tf.keras.models.load_model(r'')

# Generate new DNA sequences using the trained model
iter = 1

def generate_dna_sequence(model, sequence_length, num_nucleotides=4):
    global iter
    # Creation of a matrix with zeros for DNA generation
    seed_sequence = np.zeros((1, sequence_length, num_nucleotides), dtype=np.float32)
    generated_sequence = np.zeros((1, sequence_length, num_nucleotides), dtype=np.float32)

    # Predicting each nucleotide step by step
    for nucleotide in range(sequence_length):
        predicted_nucleotide_probs = model.predict(seed_sequence)
        predicted_nucleotide = np.random.choice(np.arange(num_nucleotides), p=predicted_nucleotide_probs[0, nucleotide, :])
        generated_sequence[0, nucleotide, predicted_nucleotide] = 1.0
        seed_sequence[0, nucleotide, predicted_nucleotide] = 1.0
        iter += 1
        print(f'Iteration number:{iter}')

    # Convert one-hot encoding back to DNA sequence
    nucleotides = ['A', 'C', 'G', 'T']
    dna_sequence = ''.join([nucleotides[np.argmax(generated_sequence[0, i, :])] for i in range(sequence_length)])
    return dna_sequence


num_seq = 80 #multiplied by 128 = all nucleotides
generated_list = []

for i in range(num_seq):
    # Generate a new DNA sequence using the trained model
    generated_dna_sequence = generate_dna_sequence(dna_generator_model, sequence_length, num_nucleotides)
    generated_list.append(generated_dna_sequence)

print(f'Generated DNA: {"".join(generated_list)}')
