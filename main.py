import funciton_tool
while True:
    funciton_tool.show_menu()
    column_name = input()
    if column_name == "1":
        funciton_tool.str_filter("标题", funciton_tool.gl_data)
    elif column_name == "2":
        funciton_tool.num_filter("销量", funciton_tool.gl_data)
    elif column_name == "3":
        funciton_tool.num_filter("价格", funciton_tool.gl_data)
    elif column_name == "4":
        funciton_tool.str_filter("类型", funciton_tool.gl_data)
    elif column_name == "5":
        funciton_tool.str_filter("卖家旺旺", funciton_tool.gl_data)
    elif column_name == "6":
        funciton_tool.str_filter("一级类目", funciton_tool.gl_data)
    elif column_name == "7":
        funciton_tool.str_filter("子类目", funciton_tool.gl_data)
    elif column_name == "8":
        funciton_tool.str_filter("多级类目", funciton_tool.gl_data)
    elif column_name == "9":
        funciton_tool.str_filter("关键词", funciton_tool.gl_data)
    elif column_name == "10":
        print("欢迎你下次再次光临本系统")
        break
    else:
        print("你的输入有误，请按屏幕的提示信息重新输入")
