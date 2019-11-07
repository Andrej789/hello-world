def get_hello_world():
    print('Hello World')

def set_hello_world(text:str) -> None:
    print(text)

#if __name__ == '__main__':
def main():
    get_hello_world()
    set_hello_world('Set: Hello World')

if __name__ == "__main__":
    main()
