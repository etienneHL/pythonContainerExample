import numpy as np

def main():
    print("Hello World")

    # Example of a call to an external dependency
    a = np.array([1, 2, 3, 4, 5, 6])
    print(a[0])

    # Example of access to the host file system
    f = open("app/fileToRead.txt", "r")
    print(f.read())