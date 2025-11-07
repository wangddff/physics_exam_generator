#!/usr/bin/env python
"""
简化的物理试卷生成器
使用DeepSeek API直接生成试卷和答案
"""
import os
import json
import requests
from fpdf import FPDF

class PhysicsExamGenerator:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.deepseek.com/v1/chat/completions"

    def call_deepseek(self, messages):
        """调用DeepSeek API"""
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = {
            "model": "deepseek-chat",
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 4000
        }

        response = requests.post(self.base_url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"API调用失败: {response.status_code} - {response.text}")

    def generate_research_report(self):
        """生成考试趋势调研报告"""
        messages = [
            {
                "role": "system",
                "content": "你是一位专业的物理教育研究员，专门研究上海市高中物理考试。"
            },
            {
                "role": "user",
                "content": "请分析2023-2025年上海市高中一年级物理考试的主要趋势，包括：\n"
                        "1. 常见的考点和知识点分布\n"
                        "2. 题目类型和难度特点\n"
                        "3. 位育中学的考试难度标准\n"
                        "4. 适合高中一年级上半学期的物理题目示例\n"
                        "请提供详细的调研报告。"
            }
        ]

        print("正在生成考试趋势调研报告...")
        return self.call_deepseek(messages)

    def generate_exam_questions(self, research_report):
        """生成20道物理简答题"""
        messages = [
            {
                "role": "system",
                "content": "你是一位经验丰富的物理教师，擅长设计符合上海市高中物理课程标准的考题。"
            },
            {
                "role": "user",
                "content": f"基于以下调研报告：\n{research_report}\n\n"
                        "请生成20道符合上海市高中一年级上半学期物理课程要求的简答题。要求：\n"
                        "1. 难度符合位育中学标准\n"
                        "2. 涵盖力学、热学、光学等主要知识点\n"
                        "3. 每道题目清晰明确，考察物理概念的理解和应用\n"
                        "4. 题目格式：题目编号、题目内容、考察知识点、预估难度\n"
                        "请按以下格式输出：\n"
                        "## 物理试卷\n"
                        "### 第1题\n"
                        "**题目内容：** [题目]\n"
                        "**考察知识点：** [知识点]\n"
                        "**难度：** [简单/中等/困难]\n"
                        "...（共20题）"
            }
        ]

        print("正在生成物理试卷题目...")
        return self.call_deepseek(messages)

    def generate_answers(self, exam_questions):
        """生成答案和解析"""
        messages = [
            {
                "role": "system",
                "content": "你是一位资深的物理教师和阅卷专家，熟悉上海市物理考试的评分标准。"
            },
            {
                "role": "user",
                "content": f"请为以下20道物理题目编写详细的答案和解析：\n{exam_questions}\n\n"
                        "每道题目的答案应该包括：\n"
                        "1. 正确答案\n"
                        "2. 详细的解题步骤\n"
                        "3. 关键知识点说明\n"
                        "4. 易错点分析\n"
                        "5. 评分标准建议\n"
                        "请按以下格式输出：\n"
                        "## 参考答案及解析\n"
                        "### 第1题\n"
                        "**答案：** [答案]\n"
                        "**解析：** [详细解析]\n"
                        "**关键知识点：** [知识点]\n"
                        "**易错点：** [易错点分析]\n"
                        "**评分标准：** [评分建议]\n"
                        "...（共20题）"
            }
        ]

        print("正在生成答案和解析...")
        return self.call_deepseek(messages)

    def create_pdf(self, content, title, filename):
        """创建PDF文档"""
        pdf = FPDF()
        pdf.add_page()

        # 设置字体
        pdf.set_font("Arial", size=12)

        # 添加标题
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt=title, ln=True, align='C')
        pdf.ln(10)

        # 添加内容
        pdf.set_font("Arial", size=11)
        lines = content.split('\n')
        for line in lines:
            if line.strip():
                # 处理标题格式
                if line.startswith('## '):
                    pdf.set_font("Arial", 'B', 14)
                    pdf.cell(0, 8, txt=line[3:], ln=True)
                    pdf.set_font("Arial", size=11)
                elif line.startswith('### '):
                    pdf.set_font("Arial", 'B', 12)
                    pdf.cell(0, 8, txt=line[4:], ln=True)
                    pdf.set_font("Arial", size=11)
                elif line.startswith('**') and line.endswith('**'):
                    pdf.set_font("Arial", 'B', 11)
                    pdf.cell(0, 8, txt=line[2:-2], ln=True)
                    pdf.set_font("Arial", size=11)
                else:
                    pdf.multi_cell(0, 8, txt=line)

        # 确保输出目录存在
        os.makedirs('output', exist_ok=True)
        pdf.output(f'output/{filename}')
        print(f"✓ PDF已生成: output/{filename}")

def main():
    # 检查API密钥
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        print("错误：请设置DEEPSEEK_API_KEY环境变量")
        print("请在.env文件中设置：DEEPSEEK_API_KEY=your_api_key_here")
        return

    generator = PhysicsExamGenerator(api_key)

    try:
        # 1. 生成调研报告
        research_report = generator.generate_research_report()
        with open('output/research_report.md', 'w', encoding='utf-8') as f:
            f.write(research_report)
        print("✓ 调研报告已生成: output/research_report.md")

        # 2. 生成试卷题目
        exam_questions = generator.generate_exam_questions(research_report)
        with open('output/exam_questions.md', 'w', encoding='utf-8') as f:
            f.write(exam_questions)
        print("✓ 试卷题目已生成: output/exam_questions.md")

        # 3. 生成答案
        answers = generator.generate_answers(exam_questions)
        with open('output/answer_key.md', 'w', encoding='utf-8') as f:
            f.write(answers)
        print("✓ 答案文档已生成: output/answer_key.md")

        # 4. 生成PDF
        generator.create_pdf(exam_questions, "上海市高中一年级上半学期物理试卷", "physics_exam.pdf")
        generator.create_pdf(answers, "物理试卷参考答案及解析", "physics_exam_answers.pdf")

        print("\n=== 物理试卷生成完成 ===")
        print("生成的文件：")
        print("- output/research_report.md (调研报告)")
        print("- output/exam_questions.md (试卷题目)")
        print("- output/answer_key.md (答案文档)")
        print("- output/physics_exam.pdf (PDF试卷)")
        print("- output/physics_exam_answers.pdf (PDF答案)")

    except Exception as e:
        print(f"生成过程中出现错误: {e}")

if __name__ == "__main__":
    main()