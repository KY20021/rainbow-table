import hashlib
import json


def md5hash(string: str) -> str:
    """
    Generate an MD5 hash for a given string.
    :param string: The input string to hash.
    :return: The MD5 hash of the input string in hexadecimal format.
    """
    return hashlib.md5(string.encode()).hexdigest()


def write_to_json(data, filename: str):
    """
    Write data to a JSON file.
    :param data: The data to write to the file.
    :param filename: The name of the file to write to.
    """

    with open(filename, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    """
    Main function to demonstrate the md5hash function.
    """
    test_string = "Hello, World!"
    print(f"MD5 hash of '{test_string}': {md5hash(test_string)}")
    print(f"MD5 hash of '{test_string}': {md5hash(test_string)}")
    print(f"MD5 hash of '{test_string}': {md5hash(test_string)}")
    print(f"MD5 hash of '{test_string}': {md5hash(test_string)}")
    print(f"MD5 hash of '{test_string}': {md5hash(test_string)}")

    # with open("common.txt", "r") as f:
    #     data = f.readlines()

    # # Create a dictionary to store the hashes
    # hash_dict = {}
    # for line in data:
    #     line = line.strip()  # Remove any leading/trailing whitespace
    #     if line:  # Ensure the line is not empty
    #         hash_value = md5hash(line)
    #         hash_dict[line] = hash_value

    # # Write the hash dictionary to a JSON file
    # write_to_json(hash_dict, "hashes.json")

    # # Test the hash function with an example
    # test_string = "Jayisgreat"
    # expected_hash = "f03aa483677e92b76db5a4e591f2c1a1"  # Replace with the actual expected hash for "Jayisgreat"
    # the_hash = md5hash(test_string)
    # assert (
    #     the_hash == expected_hash
    # ), f"Hash mismatch: expected {expected_hash}, got {the_hash}"
    # print(
    #     f"MD5 hash of '{test_string}' matches expected hash: {the_hash == expected_hash}"
    # )
