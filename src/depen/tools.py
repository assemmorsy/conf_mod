def clearPunc(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in text:
        if char not in punctuations:
            no_punct += char
        else :
            no_punct += " "
    return no_punct