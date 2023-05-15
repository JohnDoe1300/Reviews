import os
import math


def main():
    paths = os.listdir()
    paths.sort()

    output_path = "index.md"

    # clear the output file
    with open(output_path, 'w') as output:
        output.write("""## Reviews\n[回到主页](https://boheme130.github.io/Fiction.git.io/)<br><br>\n\n""")

    urls = []
    for path in paths:
        if path.find(".") != -1:
            continue
        urls.append([path, f"https://boheme130.github.io/Reviews/{path}/", f"./{path}/index.md"])
        subs = os.listdir(f"./{path}")
        if len(subs) > 1:
            for sub in subs:
                if sub == "index.md":
                    continue
                urls.append([sub, f"https://boheme130.github.io/Reviews/{path}/{sub}/", f"./{path}/{sub}/index.md"])

    with open(output_path, 'a+') as output:
        for url in urls:
            with open(url[2], 'r') as markdown:
                lines = markdown.readlines()
                book, output_str, keys = "", "", ""
                find_book, find_rate, find_key = False, False, False
                count = 0
                for line in lines:
                    line = line.rstrip()
                    if line.find("作品") != -1 and not find_book:
                        index = line.find('<')
                        book = line[3:index]
                        find_book = True
                        output_str = f"[{book}]({url[1]}) "
                    if line.find("评分") != -1 and line.find('/') != -1 and not find_rate:
                        index = line.find('/')
                        count = float(line[3:index]) - 4.7
                        if count < -0.1:
                            continue
                        count = int((count + 0.001) / 0.1) + 1
                        # print(book, count)
                        for i in range(min(count, 3)):
                            output_str += "⭐️"
                        output.write(f"{output_str}<br>\n")
                        find_rate = True
                    if line.find("关键词") != -1 and not find_key:
                        keys = line
                        find_key = True
                if not find_rate:
                    output.write(f"{output_str}<br>\n")
                if find_key:
                    output.write(f"{keys}")
                output.write("\n\n")
                     

if __name__ == "__main__":
    main()