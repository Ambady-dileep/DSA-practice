Input = "hello world"
vowels = "aeiou"
count = 0
for i in Input:
    if i in vowels:
        count+=1
print(count)
# Expected Output: 3

Input = "abc123def45"
count = 0
for i in Input:
    if i.isdigit():
        count+=1
print(count)
# Expected Output: 5

Input = "PyThOn"
uppercase = 0
lowercase = 0
for i in Input:
    if i.isupper():
        uppercase+=1
    else:
        lowercase+=1
print(f"Uppercase: {uppercase}, Lowercase: {lowercase}")
# Expected Output: Uppercase: 3, Lowercase: 3

Input = "madam"
reverse = Input[::-1]
if Input == reverse:
    print(True)
else:
    print(False)
# Expected Output: True

Input = "beautiful"
vowels = "aeiou"
result = ""
for i in Input:
    if i not in vowels:
        result+=i
    else:
        result
print(result)
# Expected Output: "btfl"

Input = "abc123#@!"
result = ""
for i in Input:
    if i.isalpha():
        result+=i
    else:
        result
print(result)
# Expected Output: "abc"

Input = "hello world"
new = Input.replace(" ","")
freq = {}
for i in new:
    freq[i] = freq.get(i,0)+1
    
a = max(freq,key = freq.get)
print(a)
print(freq)  
# Expected Output: "l"

Input = "communication"
vowels = "aeiou"
freq={}
for vowel in vowels:
    freq[vowel] = Input.count(vowel)
print(freq)
# Expected Output: {'a': 1, 'e': 0, 'i': 2, 'o': 2, 'u': 2}

Input = "aabbccdef"
freq = {}
for i in Input:
    freq[i] = freq.get(i,0)+1
    
for i in Input:
    if freq[i]==1:
        print(i)
        break
    
# Expected Output: "d"

Input = "banana"
result = ""
seen = set()
for i in Input:
    if i not in seen:
        result += i
        seen.add(i)

print(result)

# Expected Output: "ban"