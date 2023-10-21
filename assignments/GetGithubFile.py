# read a text file from my Github repository, change all instances of Andrew to Eleanor and push back to Github

import git
import requests
from config import config as cfg # to store my API key and keep it private, this file added to gitignore

def update_file_content(repo_url, file_path, old_text, new_text, github_token):
    # Get current content of the file from GitHub
    raw_url = f'{repo_url}/raw/main/{file_path}'
    response = requests.get(raw_url, headers={'Authorization': f'token {github_token}'})
    
    if response.status_code == 200:
        current_content = response.text
        
        # Replace old_text with new_text
        updated_content = current_content.replace(old_text, new_text)
        
        # Update the file using GitHub API
        update_url = f'{repo_url}/contents/{file_path}'
        
        # details for updating the file
        data = {
            "message": f"Replace '{old_text}' with '{new_text}'",
            "content": updated_content
        }
        
        # PUT request to update the file content
        update_response = requests.put(update_url, json=data, headers={'Authorization': f'token {github_token}'})
        
        if update_response.status_code == 200:
            print("File updated successfully.")
        else:
            print(f"Failed to update file. Status code: {update_response.status_code}")
    else:
        print(f"Failed to fetch file from GitHub. Status code: {response.status_code}")

if __name__ == "__main__":
    # GitHub repository URL
    repository_url = 'https://github.com/Scunnies/data-representation-coursework'
    
    # Path to the file within the repository
    file_path = 'assignments/andrew.txt'
    
    # Text to replace in the file
    old_text = 'Andrew'
    new_text = 'Eleanor'

    # GitHub personal access token
    github_token = cfg["githubkey"]

    # Update the file content on GitHub
    update_file_content(repository_url, file_path, old_text, new_text, github_token)
