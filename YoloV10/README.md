

# 1、环境依赖

```
pip install python-daemon
pip install ultralytics
```





# 2、模型脚本（ai_model.py）：

## 支持两种图片文件传入的方式

**区别就在--url参数上**

### 本地文件，支持相对、绝对路径

```
python ai_model.py ./capture/2407/202407/1706853602.8558.jpg
python ai_model.py  /var/www/xiot_qihe_ai/public/capture/2407/202407/1706853602.8558.jpg
```

### 网络文件，注意增加--url参数

```
python ai_model.py  --url  http://qhai.xxxxx.top/capture/2407/3602.8558.jpg 
```





# 3、对外部署http服务文件（http_server.py）

### 支持2种形式启动，守护进程、堵塞进程，区别就是-d参数

### 堵塞进程

```
python http_server.py
```

### 守护进程

**注意，守护进程方式启动时，程序会自动在http_server.py的同级目录内创建tmp文件夹，存放的是进程的pid文件，所以要注意文件夹权限**

```
python http_server.py -d
```



### 启动命令

解释：先找到占用8000端口的服务，并且杀死，然后启动当前服务，以8000端口启动。端口可以任意修改。

```
(sudo lsof -t -i :8000 && sudo lsof -t -i :8000 | xargs sudo kill -9) || echo "No process running on port 8000" && rm -rf ./tmp/http_server.pid && python http_server.py -d && sudo lsof -i :8000
```





