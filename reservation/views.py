import json
import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from salon.models import Service, Agent
from reservation.models import Booking
from salon.queries import all_services, get_service_agents
from core.utils import queryset_to_dict, time_durations


class Reservation(View):
    def get(self, request):
        services = all_services()
        context = {
            "services": services,
        }
        return render(request, "layout/_base.html", context=context)


class GetAgentsJson(View):
    def get(self, request):
        service_id = request.GET.get("service", None)
        if service_id:
            agents_queryset = get_service_agents(service_id)
            agents = queryset_to_dict(agents_queryset, "id", "name")
            return JsonResponse(agents, safe=False)
        return JsonResponse({"Error": 0})


class GetServiceTime(View):
    def get(self, request):
        service_id = request.GET.get("service", None)
        if service_id:
            service = Service.objects.get(id=service_id)
            times = service.times_list
            durations = time_durations(times)
            return JsonResponse({"times": durations})
        return JsonResponse({"Error": 0})


class CheckReservationExists(View):
    def post(self, request):
        data = json.loads(request.body)

        formatted_date = datetime.datetime.strptime(data["date"], "%m/%d/%Y").date()
        exist = Booking.objects.filter(
            agent_id=data["agent_id"],
            service_id=data["service_id"],
            reserve_time=data["time"],
            reserve_date=formatted_date,
        ).exists()
        if not exist:
            return JsonResponse({"ok": 1})
        return JsonResponse({"error": 0})
