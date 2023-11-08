import google.generativeai as palm
messages=[]
messages = [
  "how are you ?",
  "I am doing well"
]   
palm.configure(api_key="your-api-key")

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.9,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}
instructions = "obtain these details from user , 1.Name 2.phone number 3.children details and their names 4.highest education"
context = """Be a friendly and polite data entry customer support agent from a company, your job is to take information susch as name, phone number and other details from the user as given in this  instruction - "{instruction}" and give your reponse in 30-50 words only not more than that"""
examples = [
  [  "no their's no questions",
      "thankyou for connecting with me , have a good day"
  ],
  [
      'my passion is to drive car',
      'Nice, but can you provide me your vehicle number to proceed further'
  ]
]
def lang_model(question):
  messages.append(question)
  response = palm.chat(
      **defaults,
      context=context,
      examples=examples,
      messages=messages)
  g=response.last # Response of the AI to your most recent request
  def replace(string, replacements):
    new_string = ""
    for character in string:
      if character in replacements:
        new_string += replacements[character]
      else:
        new_string += character
    return new_string
  string=g
  replacements = {"\n" : " ", "\r" : " ", "\s" : " ","\t":" "}
  new_string = replace(string,replacements)
  messages.append(new_string)
  return new_string
lang_model("hello who are you")
