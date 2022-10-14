s = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"

output = "".join(
    list(chr(219 - ord(s[i])) if s[i].islower() else s[i] for i in range(len(s)))
)
print(output)
