file = input("Enter a file name: ")

words = file.split(".")
if len(words) > 1:
    extension = words[-1]
else:
    extension = "none"

match extension:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpeg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case "none":
        print("application/octet-stream")