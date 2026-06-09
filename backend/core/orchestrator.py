class SuperAgentOrchestrator:

    def route(self, request: str):

        request = request.lower()

        if "contract" in request:
            return "legal"

        if "logo" in request:
            return "designer"

        if "api" in request:
            return "developer"

        if "research" in request:
            return "research"

        return "documents"