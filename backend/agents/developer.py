from backend.services.llm_service import LLMService


class DeveloperAgent:

    def execute(self, task):

        prompt = f"""
You are a senior software architect.

Task:
{task}

Generate production-ready code.
Explain the solution.
"""

        answer = LLMService().generate(prompt)

        return {
            "agent": "developer",
            "task": task,
            "result": answer
        }