# pangu-precommit

为 [pangu.py](https://github.com/vinta/pangu.py) 提供 pre-commit hooks 的项目，用于自动在中文字符和半角字符（字母、数字、符号）之间插入空格，提升文本可读性。

## 功能

pangu-precommit 是一个 pre-commit hook，可以自动处理以下文件类型：
- Markdown 文件 (`.md`)
- reStructuredText 文件 (`.rst`)
- 纯文本文件 (`.txt`)

它会自动在 CJK（中文、日文、韩文）和半角字符之间添加适当的空格，使文本更加易读。

## 安装

### 使用 uv（推荐）

```bash
uv install
```

### 使用 pip

```bash
pip install -e .
```

## 配置

### 1. 安装 pre-commit

如果你还没有安装 pre-commit，请先安装：

```bash
pip install pre-commit
```

### 2. 添加 hook

在你的项目根目录创建 `.pre-commit-config.yaml` 文件，并添加以下配置：

```yaml
repos:
  - repo: https://github.com/yourusername/pangu-precommit
    rev: v0.1.0  # 使用最新的版本号
    hooks:
      - id: pangu
```

或者，如果你在本地开发：

```yaml
repos:
  - repo: local
    hooks:
      - id: pangu
        name: pangu
        entry: pangup
        language: python
        types: [text]
        files: \.(md|rst|txt)$
```

### 3. 安装 hooks

```bash
pre-commit install
```

## 使用

### 手动运行

```bash
pre-commit run pangu --all-files
```

### 自动运行

当你提交代码时，pre-commit 会自动运行 pangu hook 来格式化你的文件。

## 示例

**输入：**
```
这是一个测试test，包含中文和English。
```

**输出：**
```
这是一个测试 test，包含中文和 English。
```

## 依赖

- Python >= 3.13
- pangu >= 4.0.6.1

## 项目结构

```
pangu-precommit/
├── .pre-commit-hooks.yaml  # pre-commit hook 配置
├── pangup.py               # CLI 入口文件
├── pyproject.toml          # 项目配置和依赖
└── README.md               # 项目文档
```

## 开发

### 运行 CLI

```bash
python pangup.py 文件名.md
```

### 测试

```bash
pangup README.md
```

## 许可证

本项目遵循 pangu.py 的许可证。

## 相关链接

- [pangu.py](https://github.com/vinta/pangu.py) - 原始项目
- [pre-commit](https://pre-commit.com/) - pre-commit 框架