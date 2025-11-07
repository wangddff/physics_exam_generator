from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from .config import get_deepseek_llm
import os

@CrewBase
class PhysicsExamGeneratorCrew():
    """PhysicsExamGenerator crew"""

    @agent
    def exam_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['exam_researcher'],
            verbose=True,
            tools=[SerperDevTool()],
            llm=get_deepseek_llm()
        )

    @agent
    def question_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['question_generator'],
            verbose=True,
            llm=get_deepseek_llm()
        )

    @agent
    def answer_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['answer_generator'],
            verbose=True,
            llm=get_deepseek_llm()
        )

    @agent
    def pdf_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['pdf_generator'],
            verbose=True,
            llm=get_deepseek_llm()
        )

    @task
    def research_exam_trends(self) -> Task:
        return Task(
            config=self.tasks_config['research_exam_trends'],
        )

    @task
    def generate_exam_questions(self) -> Task:
        return Task(
            config=self.tasks_config['generate_exam_questions'],
            output_file='output/research_report.md'
        )

    @task
    def generate_answer_key(self) -> Task:
        return Task(
            config=self.tasks_config['generate_answer_key'],
            output_file='output/answer_key.md'
        )

    @task
    def create_exam_pdf(self) -> Task:
        return Task(
            config=self.tasks_config['create_exam_pdf'],
            output_file='output/physics_exam.pdf'
        )

    @task
    def create_answer_pdf(self) -> Task:
        return Task(
            config=self.tasks_config['create_answer_pdf'],
            output_file='output/physics_exam_answers.pdf'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the PhysicsExamGenerator crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )