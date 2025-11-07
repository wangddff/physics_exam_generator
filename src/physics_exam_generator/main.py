#!/usr/bin/env python
import sys
from physics_exam_generator.crew import PhysicsExamGeneratorCrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': '上海市高中一年级上半学期物理试卷'
    }

    try:
        result = PhysicsExamGeneratorCrew().crew().kickoff(inputs=inputs)
        print("\n=== 物理试卷生成完成 ===")
        print(f"生成结果: {result}")

        # 检查输出文件
        import os
        if os.path.exists('output/physics_exam.pdf'):
            print("✓ 试卷PDF已生成: output/physics_exam.pdf")
        if os.path.exists('output/physics_exam_answers.pdf'):
            print("✓ 答案PDF已生成: output/physics_exam_answers.pdf")
        if os.path.exists('output/research_report.md'):
            print("✓ 调研报告已生成: output/research_report.md")
        if os.path.exists('output/answer_key.md'):
            print("✓ 答案文档已生成: output/answer_key.md")

    except Exception as e:
        print(f"生成过程中出现错误: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run()