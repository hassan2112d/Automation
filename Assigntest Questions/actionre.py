# question 1
#import re

# def check_zip_code(text):
#     pattern = r" (?<!^)\d{5}(?:-\d{4})?(?=\D|$)"
#     result = re.search(pattern, text)
#     return result is not None

# # Test the function
# print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
# print(check_zip_code("90210 is a TV show"))  # False
# print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
# print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False


#Question 2
#The contains_acronym function checks the text for the presence of 2 or more characters or digits surrounded by parentheses, with at least the first character in uppercase (if it's a letter), returning True if the condition is met, or False otherwise. For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication" should return True since (IM) satisfies the match conditions." Fill in the regular expression in this function: 

# import re

# def contains_acronym(text):
#     pattern = r"\([A-Z][A-Z0-9]+\)"
#     result = re.search(pattern, text)
#     return result is not None

# # Test the function
# print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication"))  # True
# print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication"))  # True
# print(contains_acronym("Please do NOT enter without permission!"))  # False
# print(contains_acronym("PostScript is a fourth-generation programming language (4GL)"))  # True
# print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!"))  # True

#question 3

#The check_web_address function checks if the text passed qualifies as a top-level web address, meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores), as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using escape characters, wildcards, repetition qualifiers, beginning and end-of-line characters, and character classes.


# import re

# def check_web_address(text):
#     pattern = r"^\w+[\w\.\-\+]*\.[a-zA-Z]+$"
#     result = re.search(pattern, text)
#     return result is not None

# # Test the function
# print(check_web_address("gmail.com"))  # True
# print(check_web_address("www@google"))  # False
# print(check_web_address("www.Coursera.org"))  # True
# print(check_web_address("web-address.com/homepage"))  # False
# print(check_web_address("My_Favorite-Blog.US"))  # True
