# 使用说明

## 快速开始

### 1. 配置API密钥

1. 获取DeepSeek API密钥：
   - 访问 https://platform.deepseek.com/
   - 注册账号并获取API密钥

2. 配置环境变量：
   ```bash
   # 复制环境变量模板
   cp .env.example .env

   # 编辑.env文件，填入你的API密钥
   DEEPSEEK_API_KEY=your_deepseek_api_key_here
   ```

### 2. 运行项目

```bash
# 安装依赖
uv sync

# 运行试卷生成器
uv run python simple_main.py
```

### 3. 查看输出

运行完成后，在`output/`目录下会生成以下文件：

- `research_report.md` - 考试趋势调研报告
- `exam_questions.md` - 20道物理简答题
- `answer_key.md` - 详细的答案和解析
- `physics_exam.pdf` - PDF格式物理试卷
- `physics_exam_answers.pdf` - PDF格式答案文档

## 项目特点

### 智能生成流程

1. **考试趋势分析**：基于2023-2025年上海市高中物理考试趋势
2. **题目生成**：生成20道符合位育中学难度标准的简答题
3. **答案编写**：为每道题目提供详细的解题步骤和解析
4. **PDF输出**：生成专业的PDF格式试卷和答案

### 涵盖知识点

- 力学（运动学、牛顿定律、能量守恒等）
- 热学（温度、热量、物态变化等）
- 光学（光的反射、折射、成像等）
- 电学基础（静电、电路等）

### 定制化选项

如需修改题目数量或难度，可以编辑`simple_main.py`文件中的相关参数：

```python
# 修改题目数量
"请生成20道符合上海市高中一年级上半学期物理课程要求的简答题"

# 修改难度描述
"难度符合位育中学标准"
```

## 故障排除

### 常见问题

1. **API密钥错误**
   - 检查`.env`文件中的`DEEPSEEK_API_KEY`是否正确
   - 确保API密钥有足够的额度

2. **网络连接问题**
   - 检查网络连接
   - 确保可以访问 https://api.deepseek.com

3. **PDF生成失败**
   - 确保`output`目录有写入权限
   - 检查fpdf库是否正确安装

### 技术支持

如有问题，请检查：
- Python版本（推荐3.10+）
- 依赖包是否完整安装
- API密钥是否正确配置