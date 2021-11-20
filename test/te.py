#image转base64
import base64
with open("E:\\Workspace-Python\\Winp-Tool\\Winp-Tool 2.0.0\\image\\icon\\intel_net.png","rb") as f:#转为二进制格式
    base64_data = base64.b64encode(f.read())#使用base64进行加密
    print(base64_data)
    file=open('1.txt','wt')#写成文本格式
    file.write(base64_data)
    file.close()