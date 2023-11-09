import google.generativeai as palm

palm.configure(api_key="")


# driver function 
def lang_model(question):
    messages.append(question)
    response = palm.chat(
        **defaults,
        context=context,
        examples=examples,
        messages=messages
    )
    g = response.last  # Response of the AI to your most recent request

    def replace(string, replacements):
        new_string = ""
        for character in string:
            if character in replacements:
                new_string += replacements[character]
            else:
                new_string += character
        return new_string

    string = g
    replacements = {"\n": " ", "\r": " ", "\s": " ", "\t": " "}
    new_string = replace(string, replacements)
    messages.append(new_string)
    return new_string


messages = []
messages = [
    "how are you ?",
    "I am doing well"
]

defaults = {
    'model': 'models/chat-bison-001',
    'temperature': 0.9,
    'candidate_count': 1,
    'top_k': 40,
    'top_p': 0.95,
}
instructions = "obtain these details from user , 1.Name 2.phone number 3.children details and their names 4.highest education"
context = """Be a friendly and polite data entry customer support agent from a company, your job is to take information such as name, phone number and other details from the user as given in this  instruction - "{instruction}" and give your response in 30-50 words only not more than that"""
examples = [
    ["no there's no questions",
     "thank you for connecting with me, have a good day"
     ],
    [
        'my passion is to drive a car',
        'Nice, but can you provide me your vehicle number to proceed further'
    ]
]

lang_model('Hello, Who are you.?')

