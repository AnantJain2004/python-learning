with open("demo.txt", "r") as f:
    content = f.read()
    print(content)
    # No need to write f.close() because the file closes automatically with with statement