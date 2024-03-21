import glob
import os
import my_butt

class MarkdownBuilder:

    def __init__(self, directory: str):
        self.directory = directory
        self.current_directory = os.getcwd()
        # print(self.current_directory)
        # print(self.check_for_original())

    def delete_original(self):
        if self.check_for_original():
            os.remove(self.current_directory + "/main.md")

    def check_for_original(self):
        os.chdir(self.current_directory)
        return "main.md" in glob.glob("*.md")

    def combine_files(self):
        self.delete_original()
        os.chdir(self.directory)
        for f in glob.glob("*.md"):
            os.system("cat " + f + " >> " + self.current_directory + "/main.md")


if __name__ == "__main__":
    mb = MarkdownBuilder("Text_Snippets")
    mb.combine_files()
