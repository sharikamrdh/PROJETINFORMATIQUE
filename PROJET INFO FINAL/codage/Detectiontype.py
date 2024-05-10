import os

def determine_data_type(file_path):
    """
    Determines the type of a file based on its extension.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The type of the file.
    """
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension in ['.txt', '.csv', '.json', '.xml', '.yaml', '.ini']:
        return 'text'
    elif file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff']:
        return 'image'
    elif file_extension in ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a']:
        return 'audio'
    elif file_extension in ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm']:
        return 'video'
    elif file_extension in ['.pdf', '.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx', '.odt', '.ods', '.odp']:
        return 'document'
    elif file_extension in ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2']:
        return 'compressed'
    elif file_extension in ['.html', '.htm', '.css', '.js', '.php', '.asp', '.jsp']:
        return 'web'
    elif file_extension in ['.py', '.c', '.cpp', '.java', '.php', '.rb', '.pl', '.sh', '.bat']:
        return 'code'
    elif file_extension in ['.exe', '.dll', '.so']:
        return 'executable'
    elif file_extension in ['.ttf', '.otf']:
        return 'font'
    elif file_extension in ['.stl', '.obj', '.fbx', '.blend']:
        return '3d_model'
    elif file_extension in ['.csv', '.kml', '.gpx']:
        return 'GIS_data'
    else:
        return 'unknown'


file_path = input("Enter the file path: ")
data_type = determine_data_type(file_path)
print(f"The file appears to be of type: {data_type}")
