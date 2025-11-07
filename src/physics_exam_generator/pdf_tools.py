import os
from fpdf import FPDF

def create_exam_pdf(content: str, output_path: str):
    """
    创建物理试卷PDF
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # 添加标题
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="上海市高中一年级上半学期物理试卷", ln=True, align='C')
    pdf.ln(10)

    # 添加基本信息
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="考试时间：90分钟    满分：100分", ln=True)
    pdf.ln(5)

    # 添加内容
    pdf.set_font("Arial", size=11)
    lines = content.split('\n')
    for line in lines:
        if line.strip():
            pdf.multi_cell(0, 8, txt=line)

    pdf.output(output_path)

def create_answer_pdf(content: str, output_path: str):
    """
    创建答案PDF
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # 添加标题
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="物理试卷参考答案及解析", ln=True, align='C')
    pdf.ln(10)

    # 添加内容
    pdf.set_font("Arial", size=11)
    lines = content.split('\n')
    for line in lines:
        if line.strip():
            pdf.multi_cell(0, 8, txt=line)

    pdf.output(output_path)