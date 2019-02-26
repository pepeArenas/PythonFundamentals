# Strings are inmitable unicode sequences

# We can use both double or single quotes, this is helpful because we can use and
# take advantage to avoid escape characters
# We need to be consistent, we can't start with single quotes and end with double or viceversa
# This fulfills the zen principle Practically beats purity because we can use in order to avoid escape characters
stringDoubleQuotes = "Hello"
print(stringDoubleQuotes)
stringWithSingleQuotes = 'Hello'
print(stringWithSingleQuotes)
stringWithDoubleQuotesAndTilde = "Hello's"
print(stringWithDoubleQuotesAndTilde)

# In order to have multiple lines we can do with triple set of single quotes or doble quotes and press enter
multiline = """Line one
Line two
Line Three"""

print(multiline)

# Also we can escape manually by the \n, this is universal in python no matter in which OS we are
multilineEscapedManually = "Line one\nline two\nline three"
print(multilineEscapedManually)

print("We can use to escape \" \'")
print("We can use to escape \\")

# Raw string we need a single quotes and prefix the string with r for 'raw'

rawString = r'C:\Users\Jesus\Document'

# String are treated as arrays or sequences so we can access by index to the separate chars
exampleString = "Jesus"

print(exampleString[0])
