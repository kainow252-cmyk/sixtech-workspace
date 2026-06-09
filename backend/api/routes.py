from fastapi import APIRouter

from backend.agents.developer import DeveloperAgent
from backend.core.orchestrator import SuperAgentOrchestrator

router = APIRouter()


@router.get("/agents")
def list_agents():

    return {
        "agents": [
            "developer",
            "research",
            "legal",
            "designer",
            "documents"
        ]
    }


@router.post("/orchestrate")
def orchestrate(request: dict):

    task = request.get("task", "")

    orchestrator = SuperAgentOrchestrator()

    selected_agent = orchestrator.route(task)

    if selected_agent == "developer":
        result = DeveloperAgent().execute(task)
    else:
        result = {
            "agent": selected_agent,
            "task": task
        }

    return result