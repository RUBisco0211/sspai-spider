# paiping-app-spider

[少数派](https://sspai.com) 网站文章爬虫，专注于抓取「派评」栏目中的应用推荐。

## 功能

- 自动抓取少数派「派评 - 近期值得关注」文章
- 解析文章内容，按应用拆分提取
- 将每个应用保存为独立的 Markdown 文件
- 自动下载并本地化文章中的图片

## 依赖

```
requests
beautifulsoup4
markdownify
pytest
```

安装依赖：
```bash
pip install -r requirements.txt
```

## 使用

```bash
python main.py
```

抓取结果保存在 `data/` 目录下，格式为：
```
data/YYYY-MM-DD/App标题_[支持平台列表].md
data/YYYY-MM-DD/images/图片.jpg
```

## 项目结构

```
sspai-spider/
├── main.py           # 入口脚本
├── spider/
│   ├── fetcher.py    # API 请求模块
│   ├── parser.py     # HTML 解析模块
│   ├── saver.py      # 文件保存模块
│   └── util.py       # 工具函数
├── requirements.txt
└── data/             # 输出目录
```
