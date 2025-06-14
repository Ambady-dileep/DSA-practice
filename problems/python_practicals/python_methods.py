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

# Check if two strings are anagrams (same letters, different order)
# Input = "listen", "silent"
# str1 = "listen"
# str2 = "silent"

# if sorted(str1) == sorted(str2):
#     print(True)
# else:
#     print(False)

# Expected Output: True

# Find the longest word in a sentence
# Input = "Code every single day"
# count = 0
# ans = ""
# for i in Input.split():
#     if len(i) > count:
#         count = len(i)
#         ans = i
        
# print(ans)
# Expected Output: "single"

# Replace every vowel with '*'
# Input = "developer"
# result = ""
# vowels = "aeiou"
# for i in Input:
#     if i in vowels:
#         result+="*"
#     else:
#         result+=i
# print(result)
# Expected Output: "d*v*l*p*r"

# Print all unique characters from a string (preserve order)
# Input = "success"
# seen = set()
# result = ""
# for i in Input:
#     if Input.count(i) == 1:
#         result += i
# print(result)
# Expected Output: "u e"

# Count how many words start with a vowel
# Input = "Always open up ideas everyday"
# vowels = "aeiouAEIOU"
# count = 0
# for i in Input.split():
#     if i[0] in vowels:
#         count+=1
        
# print(count)
# Expected Output: 4

# Extract digits from a string and return them as a list of integers
# Input = "I scored 95 in math and 88 in science"
# ll = []
# for i in Input:
#     if i.isdigit():
#         ll.append(int(i))
# print(ll)
# Expected Output: [9, 5, 8, 8]

# Print only words that contain the letter 'e'
# Input: "the pen is on the table"

# Expected Output: ['the', 'pen', 'the', 'table']

# Count the frequency of each word in a sentence
# Input = "work hard play hard"
# new = Input.split()
# freq = {}
# for i in new:
#     freq[i] = freq.get(i,0)+1
    
# print(freq)
# Expected Output: {'work': 1, 'hard': 2, 'play': 1}
