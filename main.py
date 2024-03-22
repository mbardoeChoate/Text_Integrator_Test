import glob
import os


class MarkdownBuilder:
    def __init__(self, directory: str):
        self.directory = directory
        self.current_directory = os.getcwd()

    def delete_original(self):
        """
        Deletes the file main.md if it exists

        :return:
        None
        """
        if self.check_for_original():
            os.remove(self.current_directory + "/main.md")

    def check_for_original(self):
        """
        Checks if the file main.md exists

        :return:

        bool: True if main.md exists, False otherwise
        """
        os.chdir(self.current_directory)
        return "main.md" in glob.glob("*.md")

    def combine_files(self):
        """
        Combines all the files in the directory into one file

        :return:
        None
        """
        self.delete_original()
        os.chdir(self.directory)
        cmd = "cat "
        for f in glob.glob("*.md"):
            cmd += f + " "
        os.system(cmd + " >> " + self.current_directory + "/main.md")


if __name__ == "__main__":
    mb = MarkdownBuilder("Text_Snippets")
    mb.combine_files()
