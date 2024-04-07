s=input().lower()
print("".join("."+e for e in s if e not in "aeiouy"))