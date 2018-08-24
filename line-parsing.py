# testing Python's parsing of the metrics got from JXM URL
test = "jvm_memory_bytes_used{area=\"heap\",} 7.01277184E8"
a = re.split(' ', test)
type(a[1])

print(test)