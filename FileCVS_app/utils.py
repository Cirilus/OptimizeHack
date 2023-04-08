import io
import os
import shutil
from unidecode import unidecode
import chardet as chardet
from docx import Document
from git import Repo


class Git:
    def __init__(self):
        self.repo_path = os.path.join(os.getcwd(), 'word_docs')
        if os.path.exists(self.repo_path):
            self.repo = Repo.init(self.repo_path)
        else:
            self.repo = Repo(self.repo_path)

    def new_version(self, file_name, file, name_commit):
        doc_path = os.path.join(self.repo_path, file_name)
        document = Document(file)
        document.save(doc_path)
        index = self.repo.index
        index.add([doc_path])
        index.commit(name_commit)

    def get_all_commits(self, file_name):
        commits = []
        for commit in self.repo.iter_commits(paths=file_name):
            commits.append(commit.message)

    def get_commit(self, commit_name, file_name):
        for commit in self.repo.iter_commits(paths=file_name):
            if commit.message == commit_name:
                contents = commit.tree[file_name].data_stream.read()
                return io.BytesIO(contents)