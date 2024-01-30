blocks = [["false", "true", "false"],
          ["true", "false", "false"],
          ["true", "true", "false"],
          ["false", "true", "false"],
          ["false", "true", "true"]]
h_list = []
flag = 0

for i in range(len(blocks)):
    if not h_list:
        h_list = blocks[i].copy()
    else:
        for j in range(len(blocks[i])):
            if blocks[i][j] == h_list[j] == "false":
                pass
            elif blocks[i][j] == "true" and h_list[j] == "false":
                pass
            else:
                h_list[j] = blocks[i][j]

    for bol in h_list:
        if bol == "false":
            flag += 1
        else:
            flag =0

    if flag == 3:
        print(i - 1)
        break
