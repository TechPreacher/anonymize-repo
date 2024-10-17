import os
import re
import uuid

import helpers

COMPANY_NAME = "Test Company"

def anonymize_url(url: str) -> str:
    # Create a hash of the URL
    return f"https://anonymized.url/{uuid.uuid4()}"


def anonymize_email(email: str) -> str:
    return f"anonymized.email@{uuid.uuid4()}.com"


def anonymize_urls_in_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()

        # Regular expression to find URLs
        url_pattern = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
        email_pattern = r"/([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)/gi"

        # Replace each URL with its anonymized version
        anonymized_url = re.sub(
            url_pattern, lambda m: anonymize_url(m.group(0)), content
        )
        anonymized_email = re.sub(
            email_pattern, lambda m: anonymize_email(m.group(0)), anonymized_url
        )

        anonymized_company = anonymized_email.replace(
            COMPANY_NAME, "Contoso Inc."
        )

        anonymized_final = anonymized_company

        with open(file_path, "w") as file:
            file.write(anonymized_final)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")


def process_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(
                (
                    ".py",
                    ".json",
                    ".xml",
                    ".txt",
                    ".yml",
                    ".yaml",
                    ".tf",
                    ".tfvars",
                    ".md",
                    ".toml",
                    ".rst",
                    ".csv",
                    ".ini",
                    ".cfg",
                    ".conf",
                    ".properties",
                    ".env",
                    ".sh",
                    ".bash",
                )
            ):
                file_path = os.path.join(root, file)
                anonymize_urls_in_file(file_path)
                print(f"Processed: {file_path}")
            else:
                print(f"Skipped: {file}")


subfolders = helpers.list_subfolders(os.path.dirname(os.path.abspath(__file__)))

for subfolder in subfolders:
    process_files(subfolder)
