class FileUploadError(Exception):
    pass

def upload_cover_letter(file_path):
    try:
        # Check if the file exists
        with open(file_path, 'rb') as file:
            # Check if the file size exceeds a certain limit
            max_file_size = 5 * 1024 * 1024  # 5 MB
            if len(file.read()) > max_file_size:
                raise FileUploadError("File size exceeds the allowed limit.")

            # Check if the file format is supported
            supported_formats = ['.pdf', '.doc', '.docx', '.txt']
            if not any(file_path.lower().endswith(format) for format in supported_formats):
                raise FileUploadError("Unsupported file format.")

        # Proceed with the file upload
        print("File uploaded successfully.")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except FileUploadError as e:
        print(f"File upload error: {e}")
    except Exception as ex:
        print(f"Unexpected error: {ex}") 