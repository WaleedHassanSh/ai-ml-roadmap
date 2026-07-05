# A program that identifies a person based on their DNA sequence, using a database of known DNA profiles and the longest match of Short Tandem Repeats (STRs) in the given DNA sequence.

import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit(1)

    # TODO: Read database file into a variable
    with open(sys.argv[1]) as file:
        database = csv.DictReader(file)
        headers = database.fieldnames
        database = list(database)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as file:
        dna = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    if headers is None:
        sys.exit(1)
    str_counts = [longest_match(dna, i) for i in headers[1:]]

    # TODO: Check database for matching profiles
    for data in database:
        found = True

        for position, current_str in enumerate(headers[1:]):
            if int(data[current_str]) != str_counts[position]:
                found = False

        if found:
            print(data["name"])
            break

        if not found:
            print("No match")

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


main()
