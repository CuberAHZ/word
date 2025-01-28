input_txt_path = input("输入文件名称:")
output_txt_path = input("输出文件名称:")

with open(input_txt_path, "r", encoding="utf-8") as r:
    input_text_list = r.read().split("\n")
    for i in range(len(input_text_list)):
        try:
            if input_text_list[i] == "":
                del input_text_list[i]
            if input_text_list[i-1] == "":
                del input_text_list[i-1]
        except IndexError:
            pass

with open(output_txt_path, "w", encoding="utf-8") as w:
    output_text_str = ""
    for i in range(int(len(input_text_list)/2)):
        output_text_str = output_text_str + input_text_list[i*2+1] + ":" + input_text_list[i*2] + "\n"
    w.write(output_text_str[0:-2])
