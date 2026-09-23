import sys
if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    match_count = text.count(keyword)
    if match_count > 0:
        print(match_count)
    else:
        print("none")