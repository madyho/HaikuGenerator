from ai import call_gpt

def main():
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    print("Creating your haiku...")
    prompt = f"create a haiku using {name} and {topic}"
    print(call_gpt(prompt))


if __name__ == "__main__":
    main()
