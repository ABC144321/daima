print("我可以帮你读取文件。（要和海龟编辑器同目录）")
a = input("请输入你要读取的文件（可输入完整路径）：")
try:
    with open(a, "r", encoding="gbk") as file:
        print("文件内容为：")
        for line in file:
            print(line.rstrip('\n'))
except FileNotFoundError:
    print("文件不存在！请检查路径和文件名是否正确。错误信息：{e} \n")
except UnicodeDecodeError:
    print("文件编码不是GBK，读取失败！可以尝试更换编码为utf-8。\n")
except Exception:
    print("文件不存在或已损坏！\n")