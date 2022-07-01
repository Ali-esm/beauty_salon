import json
import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from customer.forms import CustomerForm
from customer.models import Customer
from salon.models import Service, Agent
from reservation.models import Booking
from salon.queries import all_services, get_service_agents
from core.utils import queryset_to_dict, time_durations


class Reservation(View):
    def get(self, request):
        customer_form = CustomerForm()
        services = all_services()
        context = {
            "services": services,
            "customer_form": customer_form,
        }
        return render(request, "layout/_base.html", context=context)

    def post(self, request):
        reservation_info = json.loads(request.COOKIES.get("reservation"))
        date_object = datetime.datetime.strptime(
            reservation_info["date"], "%m/%d/%Y"
        ).date()
        customer_info = request.POST
        customer_form = CustomerForm(customer_info)
        if customer_form.is_valid():
            print(reservation_info)
            print(customer_info)
            customer_obj = Customer.objects.create(
                name=customer_form.cleaned_data["name"],
                last_name=customer_form.cleaned_data["last_name"],
                phone=customer_form.cleaned_data["phone"],
            )

            booking_obj = Booking.objects.create(
                agent_id=reservation_info["agent_id"],
                service_id=reservation_info["service_id"],
                customer_id=customer_obj.id,
                reserve_time=reservation_info["time"],
                reserve_date=date_object,
            )
            print(booking_obj.reservation_uuid)
            return JsonResponse({"status": 1}, status=201)
        return JsonResponse(
            {"status": 0, "error": customer_form.errors.as_json()}, status=400
        )


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
        booking_exist = Booking.objects.filter(
            agent_id=data["agent_id"],
            service_id=data["service_id"],
            reserve_time=data["time"],
            reserve_date=formatted_date,
        ).exists()
        if not booking_exist:
            res = JsonResponse({"ok": 1})
            json_data = json.dumps(data)
            res.set_cookie("reservation", json_data)
            return res
        return JsonResponse({"error": 0, "msg": "This date & time is reserved"})
