import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def clean_prompt(text: str):
    
    doc = nlp(text)
    
    entities = {ent.text for ent in doc.ents}
    
    cleaned_tokens = []
    for token in doc:
        if token.text in entities or token.pos_ in ["NOUN", "VERB", "PROPN", "ADJ"]:
            cleaned_tokens.append(token.text)
        elif not token.is_stop and not token.is_punct:
            cleaned_tokens.append(token.text)
            
    return " ".join(cleaned_tokens)

# # Example
# raw = """Hello AI,

# I would like you to explain Python programming language to me. I am completely new to programming and I have never worked with Python before. Please explain Python in a simple way that is easy to understand.

# I am a beginner, so please use beginner-friendly language. Avoid using difficult technical jargon because I might not understand advanced terminology. Try to make the explanation simple and clear.

# Can you explain what Python is and why it is used? I would also like to know where Python is commonly used in the real world. Please explain the applications of Python in web development, artificial intelligence, machine learning, data science, automation, and cybersecurity.

# Since I am a beginner, please explain Python for beginners. Use simple language. Make the explanation easy to understand. Please avoid complex technical terms. If you use any technical terms, explain them in a simple way.

# I would appreciate examples. Please provide examples. Examples will help me understand Python better. Give simple examples that a beginner can follow easily.

# Can you also explain variables in Python? I want to understand variables with examples. Please explain variables in a beginner-friendly way. Give examples of variables and explain how variables are used.

# Please explain data types in Python. Explain strings, integers, floating-point numbers, booleans, lists, tuples, dictionaries, and sets. Use examples for each data type.

# I would also like to understand loops in Python. Please explain for loops and while loops. Give simple examples for both. Explain how loops work in an easy way.

# Can you explain functions in Python? I want to know why functions are useful. Please provide examples of functions and explain them in simple language.

# Please explain Python step by step. Since I am a beginner, I learn better when concepts are introduced gradually. Make the explanation structured and organized.

# Please include practical examples. Real-world examples are very helpful. Beginner-friendly examples are preferred. Avoid advanced examples.

# Please make sure the explanation is easy to understand. Use simple language. Use beginner-friendly language. Avoid jargon. Provide examples wherever possible.

# At the end, summarize the important points and provide a simple learning roadmap for a beginner who wants to become proficient in Python programming."""
# print(clean_prompt(raw))