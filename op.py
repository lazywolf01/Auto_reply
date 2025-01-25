from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI()

command = '''
 [4:49 pm, 24/01/2025] 2111126: Bkl gand mar dunga
[4:51 pm, 24/01/2025] Alok: or kesa h bhai
[4:51 pm, 24/01/2025] 2111126: Mast bhai mast
[4:51 pm, 24/01/2025] Alok: or bhai sex kb kiya tha last baar
[4:52 pm, 24/01/2025] 2111126: Btaya tobtha bhai Tereko
[4:52 pm, 24/01/2025] 2111126: Parso hi to Kiya  tha
[4:52 pm, 24/01/2025] Alok: accha konsa position favorite  h tera
[4:52 pm, 24/01/2025] 2111126: Doggy position
[4:53 pm, 24/01/2025] Alok: accccha ,kabhi reverse cowgirl try kiya h kya ?
[4:54 pm, 24/01/2025] 2111126: Naa bhai sirf cowgirl hi kr paya
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named Naruto who speaks hindi as well as english. He is from India and is a coder. You analyze chat history and respond like Naruto"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)