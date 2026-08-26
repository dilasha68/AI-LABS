import re

# 1. Define your dictionary mapping keywords to values
keyword_dict = {
    # "apple": "fruit",
    # "banana": "fruit",
    # "carrot": "vegetable",
    # "broccoli": "vegetable"
    
}

def extract_values(natural_language_text):
    # 2. Normalize text: lowercase and remove punctuation
    words = re.findall(r'\b\w+\b', natural_language_text.lower())
    
    # 3. Match words to the dictionary and return unique mapped values
    assigned_values = {keyword_dict[word] for word in words if word in keyword_dict}
    return list(assigned_values)

# Test the function
text = "I bought an apple and a very crunchy carrot today."
print(extract_values(text))
# Output: ['fruit', 'vegetable']
