# Text Compression Using Character Runs

text = "aaabbbccccdd"

encoded = ""
count = 1

for i in range(1, len(text)):

    if text[i] == text[i-1]:
        count += 1
    else:
        encoded += text[i-1] + str(count)
        count = 1

encoded += text[-1] + str(count)

print("Original String:", text)
print("Encoded String:", encoded)

if len(encoded) < len(text):
    print("Compression is Beneficial")
else:
    print("Compression is Not Beneficial")

print("Original Length:", len(text))
print("Encoded Length:", len(encoded))