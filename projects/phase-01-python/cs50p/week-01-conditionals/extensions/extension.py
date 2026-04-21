# Asks the user for a file name. If the file name ends with .pdf, then output application/pdf. If the file name ends with .jpg or .jpeg, then output image/jpeg. If the file name ends with .gif, then output image/gif. If the file name ends with .png, then output image/png. If the file name ends with .txt, then output text/plain. If the file name ends with .zip, then output application/zip. If the file name ends with .bin, then output application/octet-stream. Otherwise, output application/octet-stream.

file_name = input("Enter the file name with extension: ")

file_name = file_name.lower().strip()

if file_name.endswith(".pdf"):
    print("application/pdf")
elif file_name.endswith(".jpg"):
    print("image/jpeg")
elif file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".jpeg"):
    print("image/jpeg")
elif file_name.endswith(".png"):
    print("image/png")
elif file_name.endswith(".txt"):
    print("text/plain")
elif file_name.endswith(".zip"):
    print("application/zip")
elif file_name.endswith(".bin"):
    print("application/octet-stream")
else:
    print("application/octet-stream")
