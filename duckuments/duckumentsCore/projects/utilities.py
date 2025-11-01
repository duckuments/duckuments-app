# INFO : all utilities for generate a doc

from pathlib import Path
import zipfile
import os
from django.conf import settings
from .models import ProjectModel

from openai import OpenAI


# INFO : generate doc for a project
def generator(extract_path, project_slug, project_title, project_des, file_extension):
    extract_file_path = Path(extract_path)

    try:
        """
        for file_path in extract_file_path.rglob(f"*{file_extension}"):
            if file_path.is_file():
                file_name = file_path.name  # "main.py"
                # Now change file_name extension to .md
                new_file_name = Path(file_name).with_suffix(".md").name
                full_file_path = str(file_path.resolve())  # Absolute file path
                file_content = reader(file_path)
                response_content = sender(
                    file_name, full_file_path, file_content, project_title, project_des
                )
                exporter(response_content, new_file_name, project_slug, full_file_path)

        """

        files = itrate_in_folder(extract_file_path)

        try:
            for file in files:
                response_content = sender(
                    file.get("name"),
                    file.get("path"),
                    file.get("content"),
                    project_title,
                    project_des,
                )
                exporter(
                    response_content, file.get("name"), project_slug, file.get("path")
                )
        except Exception as e:
            print(f"custom itrate error : {e}")

        # set project fields :
        project = ProjectModel.objects.filter(slug=project_slug).first()
        project.set_extract_file_path(str(extract_file_path))
        project.set_doc_folder_path(
            f"{settings.BASE_DIR}\\media\\documents\\{project_slug}"
        )
        project.save()
        return True
    except Exception as e:
        print(f"generator error : {e}")
        return False


# INFO : make dir
def mkdir(path: str):
    try:
        os.mkdir(path)
        print(f"Directory '{path}' created successfully.")
        return True
    except FileExistsError:
        print(f"Directory '{path}' already exists.")
        return False
    except PermissionError:
        print(f"Permission denied: Unable to create '{path}'.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


# INFO : extract zip file content to a path
def extractor(file, slug: str):
    # first create a project-folder
    DIRECTORY = f"{settings.BASE_DIR}/media/extractor/{slug}"
    mkdir(DIRECTORY)

    # extract file with zip file ;
    try:
        with zipfile.ZipFile(file, mode="r") as archive:
            archive.extractall(DIRECTORY)
            print("extract done")

            # return directory path for save in object
            return DIRECTORY

    except Exception as e:
        print(f"An error occurred: {e}")


# INFO : send file content and other proejct information to AI for generate doc
def sender(filename: str, filePath: str, code, projectTitle: str, projectDes: str):
    SYSTEM_PROMPT = """
            You are Duckuments AI — an intelligent assistant designed to generate clear, human-readable documentation from raw source code files. 
            You specialize in explaining code to developers as if you're part of their team, keeping things practical, structured, and easy to understand.

            Your goal is to:
            - Analyze and understand the purpose of each file.
            - Break down classes, functions, and logic.
            - Explain what each part of the code does in simple but accurate terms.
            - Follow a documentation style that resembles how expert developers document their own projects.
            - Output Markdown-friendly content.

            Always aim for clarity, consistency, and readability.
    """

    USER_PROMPT = f"""Please generate clear and human-readable documentation for the following code:

            **Filename**: {filename}
            **FilePath**: {filePath}
            **ProjectName**: {projectTitle}
            **ProjectDescription**: {projectDes}

            **Guidelines**:
            - Start with a short summary explaining what the file does overall.
            - Document each function/class with its purpose, parameters, and return values.
            - Convert any inline comments into fluent explanations when appropriate.
            - Format the output using **Markdown** (use headers, lists, and code blocks as needed).
            - The tone should be professional yet friendly, like a senior developer helping a peer.

            Here is the code:
            ```python
            {code}
            ```
    """

    url = "https://agentrouter.org/v1"

    # Insert your AIML API key in the quotation marks instead of <YOUR_AIMLAPI_KEY>:
    key = "sk-JJQ30ATZhD5x2ARQdnRgbQ86QwbVFb44xt78F2PF2XuZpVjg"

    api = OpenAI(api_key=key, base_url=url)

    completion = api.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT},
        ],
        temperature=0.7,
        max_tokens=256,
    )

    message = completion.choices[0].message.content
    print("sender done")
    return message


# INFO : read content in file
def reader(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            print("reader done")
            return content
    except Exception as e:
        print(f"reder error : {e}")


# INFO : export returned content from sender
def exporter(file_content, file_name, project_name, file_path):
    """
    Save file_content as a .md file inside media/documents/{project_name}/{file_path}
    """

    # Base directory
    base_dir = f"{settings.BASE_DIR}/media/documents/{project_name}"

    # make dir for project
    mkdir(base_dir)

    # Full path to target directory
    target_dir = os.path.join(base_dir, file_path)
    # os.makedirs(target_dir, exist_ok=True)
    mkdir(target_dir)

    # Ensure .md extension
    if not file_name.endswith(".md"):
        file_name = os.path.splitext(file_name)[0] + ".md"
        print(f"file name in exporter : {file_name}")

    # Full file path
    full_file_path = os.path.join(target_dir, file_name)

    # Write content to file
    with open(full_file_path, "w", encoding="utf-8") as file:
        file.write(file_content)

    return full_file_path


# INFO : for show tree structure online preview.
# how to get dynamic path ? for show online tree preview.
def get_folder_structure(project_slug):
    doc_path = f"{settings.BASE_DIR}\\media\\documents\\{project_slug}"
    structure = []

    for dirpath, dirnames, filenames in os.walk(doc_path):
        folder = {
            "path": os.path.relpath(dirpath, doc_path),
            "folders": dirnames,
            "files": filenames,
        }
        structure.append(folder)

    # for exsample -> return data like this : a list of dic for each path in doc folder
    #
    # {'path': '.', 'folders': ['folder1', 'folder2'], 'files': ['main.md']}, {'path': 'folder1', 'folders': ['dfolder1'], 'files': ['folder1.md']}, {'path': 'folder
    # 1\\dfolder1', 'folders': [], 'files': ['dfolder1.md']}, {'path': 'folder2', 'folders': ['dfolder2'], 'files': ['folder2.md']}, {'path': 'folder2\\dfolder2', 'fo
    # lders': [], 'files': ['dfolder2.md']}]

    return structure


def itrate_in_folder(base_folder):
    """
    Recursively extract file name, content, and relative path for all files in the folder.
    """
    files_data = []

    for root, dirs, files in os.walk(base_folder):
        for file in files:
            file_path = os.path.join(root, file)

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue

            # Relative path from the base folder
            relative_dir = os.path.relpath(root, base_folder)
            files_data.append(
                {
                    "name": file,
                    "content": content,
                    "path": relative_dir.replace("\\", "/"),  # Normalize for Unix-style
                }
            )

    return files_data


# INFO :  get folder_path and project slug for create_doc_kzip_file
def create_zip_file(folder_path, project_slug):
    # create folder in zip folder for project
    output_path = f"{settings.BASE_DIR}/media/zip/{project_slug}"
    mkdir(output_path)

    # create file output path
    file_name = os.path.splitext(project_slug)[0] + ".zip"
    output_path = os.path.join(output_path, file_name)

    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, start=folder_path)
                zipf.write(abs_path, arcname=rel_path)

    return output_path
