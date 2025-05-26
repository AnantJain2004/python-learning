def show_details(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Keyword: {kwargs}")

show_details("mango", "banana", color = "yellow", size = "medium")