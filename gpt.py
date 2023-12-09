import tiktoken

encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')

# get text from file
with open('dialogs/192_filtered.txt', 'r') as file:
    text = file.read()


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

print(num_tokens_from_string(text, "gpt-3.5-turbo"))
