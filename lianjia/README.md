# 链家网租房信息(上海)爬虫

## 数据文件 `data` 文件夹
- houses.json   # 抓取后数据
- houses.json.backup
- houses.csv   # 整理后数据
- houses.csv.backup
- solved.csv   # 按自定义条件整理后数据

## 分析脚本(未完成)
> mining.py   # 使用 pandas 处理数据

## 高德API + 数据展示
- `index.html`   # 数据展示页面
- `solved.csv`   # 房源文件

### 步骤
> 1. `python -m SimpleHTTPServer 3000`   # 启动服务器

> 2. 进入浏览器输入 `localhost:3000` 进入展示页面

> 3. 输入工作地点，定位地图

> 4. 选择通勤方式，确定通勤范围

> 5. 导入房源文件，在地图上标记房源

## ToDo
- 修改 `index.html` 中的script代码，使房源信息可以跳转到具体页面
- ...
