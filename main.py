import sys

def word_count(contents):
	words = contents.split()
	return len(words)

def get_character_counts(contents):
	counts = {}
	for char in contents:
		char = char.lower()
		if char in counts:
			counts[char] += 1
		else:
			counts[char] = 1
	return counts

def report(character_counts):
	count_list = []
	for key in character_counts:
		if key.isalpha():
			count_list.append((character_counts[key], key))
	count_list.sort(reverse=True)
	for count in count_list:
		print(f"The '{count[1]} character was found {count[0]} times")

def main():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
		count = word_count(file_contents)
		character_counts = get_character_counts(file_contents)
		print(f"The book contains {count} characters")
		print()
		report(character_counts)

if __name__ == '__main__':
	sys.exit(main())
