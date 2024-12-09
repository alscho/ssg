import os
import shutil
from textnode import TextNode, TextType

def replace_dest_with_src_copy(src, dest):
    if os.path.exists(src):
        if not os.path.exists(dest):
            dirs = dest.split("/")
            #print(f"### dirs: {dirs}")
            dir = ""
            for i in range(0, len(dirs)):
                dir = os.path.join(dir, dirs[i])
                if not os.path.exists(dir):
                    #print(f"### dir: {dir}")
                    os.mkdir(dir)
                    print(f"made directory '{dir}'")
        else:
            print(f"removed tree at '{dest}'")
            shutil.rmtree(dest)
        src_contents = os.listdir(src)
        for content in src_contents:
            new_path = os.path.join(src, content)
            #print(f"#### content: {new_path} isfile: {os.path.isfile(new_path)}")
            if os.path.isfile(new_path):
                shutil.copy(new_path, dest)
                print(f"copied '{new_path}' to '{dest}'")
            else:
                new_dest = os.path.join(dest, content)
                print(f"'{new_path}' is a directory, start new iteration with new_src: '{new_path}' and new_dest '{new_dest}'")
                replace_dest_with_src_copy(new_path, new_dest)
                print(f"iteration at '{new_path}' successful")

    else:
        raise Exception("source path not found")

def main():
    src = "static"
    dest = "public"
    print(f"starting to copy '{src}' to '{dest}'")
    replace_dest_with_src_copy(src, dest)
    print(f"copy complete!")

main()