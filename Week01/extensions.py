def get_extension(file_name):
    return file_name.strip().split(".")[-1].lower()


filename = input("Input your file name: ")

extension = get_extension(filename)

types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip",
}

print(types.get(extension))
