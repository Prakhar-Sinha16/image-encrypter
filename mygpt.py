import openai
openai.api_key = "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"
model_engine = "text-davinci-002"
prompt = str(input("Enter your promt: "))
completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_tokens=1024,
    n=1,
    stop = None,
    temperature=0.9)
response = completion.choices[0].text
print(response)