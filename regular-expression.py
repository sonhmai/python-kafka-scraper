import re

test = """# HELP jvm_memory_bytes_used Used bytes of a given JVM memory area.
# TYPE jvm_memory_bytes_used gauge
jvm_memory_bytes_used{area="heap",} 7.01277184E8
jvm_memory_bytes_used{area="nonheap",} 5.460908E7"""

lines = test.splitlines()
print(lines)

matches = {}

for line in lines:
    if re.match(r'\w', line):
        print('MATCH: ', line)
        b = line.split()
        print(b)
