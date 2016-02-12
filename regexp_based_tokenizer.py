import re


def tokenize(sentence):
	"""
	Takes a sentence of type string and returns a tokenized sentence using regex. The tokens account for:

	- words (containing only letters and hyphens)
	- contractions ("'ll", "'re", "n't", etc.)
	- punctuation signs (commas, periods, exclamation and question marks, brackets and quotation marks, etc.)
	- numbers with or without currency ("$1,000", "113", etc.)
	- abbreviations and contractions with periods (e.g., "U.S.", "Jr.")

	"""
	sentence = re.sub(r"(n't\b|'ll\b|'re\b|'ve\b|'d\b|'s\b|'m\b|,((\s)|(?=\"))|(?<!\.)\.((?=\")|(?=$))|:|;|\)|}|]|!|\?|\"(\s|$|,|;|:|\)|}|]))", r" \1", sentence)
	sentence = re.sub(r"(\(|{|\[|(\s|^)\")(\S+)", r"\1 \3", sentence)
	return sentence
