import glob
import os


class MarkdownBuilder:
    def __init__(self, directory: str):
        self.directory = directory
        self.current_directory = os.getcwd()

    def delete_original(self):
        if self.check_for_original():
            os.remove(self.current_directory + "/main.md")

    def check_for_original(self):
        os.chdir(self.current_directory)
        return "main.md" in glob.glob("*.md")

    def combine_files(self):
        self.delete_original()
        os.chdir(self.directory)
        cmd = "cat "
        for f in glob.glob("*.md"):
            cmd += f + " "
        os.system(cmd + " >> " + self.current_directory + "/main.md")


if __name__ == "__main__":
    mb = MarkdownBuilder("Text_Snippets")
    mb.combine_files()
