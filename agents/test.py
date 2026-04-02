import os
import subprocess
# # 查看所有环境变量
# for key, value in os.environ.items():
#     print(f"{key} = {value}")


# # 查看数量
# print(f"共有 {len(os.environ)} 个环境变量")
print("------------------------------'dir'-------------------")
result = subprocess.run(['dir'],shell=1,capture_output=0)#shell=1 可以直接运行字符串命令 capture_output=1
# print(result.stdout)
print()
print("------------------------------hello Test-------------------")
result = subprocess.run(['echo', 'Hello'], capture_output=0,shell=True,text=1)
print(type(result.stdout))  # <class 'bytes'>
print(result.stdout)        # b'Hello\n'

current = os.getcwd()
print(f"当前工作目录: {current}")