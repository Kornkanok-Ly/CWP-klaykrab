import sys
if len(sys.argv) == 1:
    print("none")
else:
    print(f"parameters: {len(sys.argv) - 1}")
    for word in sys.argv[1:]:
        print(f"{word}: {len(word)}")