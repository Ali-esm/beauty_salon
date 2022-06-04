from salon.models import Service, Agent


def all_services():
    """
    used to get all services queryset
    """
    return Service.objects.all()


def all_agents():
    """
    used to get all agents queryset
    """
    return Agent.objects.all()


def get_service_agents(service_id):
    """
    used to get specific service agents
    """
    service = Service.objects.get(id=service_id)
    agents = service.agent_set.all()
    return agents
