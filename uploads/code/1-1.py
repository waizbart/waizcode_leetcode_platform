n = int(input())

fibonacci_sequence = []
    
if n <= 0:
    print(" ".join(fibonacci_sequence))
    
a, b = 0, 1
    
fibonacci_sequence.append(str(a))
    
if n > 1:
    fibonacci_sequence.append(str(b))
    
for _ in range(2, n):
    a, b = b, a + b
    fibonacci_sequence.append(str(b))

print(" ".join(fibonacci_sequence))