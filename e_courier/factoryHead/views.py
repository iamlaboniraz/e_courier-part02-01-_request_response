from django.http import request
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

import industry
from account.models import Profile
from delivery_service.models import DelevaryInfo
from industry.models import IndustryName, PriceSet, Industry
from django.db.models import Sum, Count, OuterRef, Subquery


class FactoryList(ListView):
    context_object_name = 'Factorys'
    model = IndustryName
    template_name = 'factorylist.html'


class FactoryEmployeeList(DetailView):
    context_object_name = 'FactoryDetalis'
    model = IndustryName
    template_name = 'factoryDetails.html'



class FactoryInvoicePrint(DetailView):
    context_object_name = 'Factoryinvoice'
    model = Profile
    model2 = DelevaryInfo
    template_name = 'invoice.html'



class FactoryDetails(DetailView):
    context_object_name = 'FactoryDetalis'
    model = Profile
    # print(Profile.objects.get(id=id).industrys)
    # x = DelevaryInfo.objects.filter(industry=OuterRef("industry")).order_by("-client")
    # y = DelevaryInfo.objects.all().annotate(z=Subquery(x.values('client_id')))
    # print("y = ",y)
    template_name = 'employeeBillDetails.html'

    def total_bill(self, profile):
        employee = profile.FactoryInvoice.all()
        total = 0
        for e in employee:
            if str(e.order.order_status) == '0':
                total += e.industry.price
        return total

    def get_context_data(self, **kwargs):
        context = super(FactoryDetails, self).get_context_data(**kwargs)
        print(kwargs)
        context['total_bill'] = self.total_bill(kwargs['object'])

        return context

def totalpayment(request):
    total = Profile.objects.all()
    order = []
    groups = DelevaryInfo.objects.select_related('Bill').values('industry')
    print(groups)
    result = DelevaryInfo.objects.values('industry').order_by('client').annotate(total_price=Sum('industry'))
    # print(result)
    x = DelevaryInfo.objects.raw('SELECT *,sum(price) from industry')
    from django.db import connection
    print("c = ", connection.queries)
    print("total = ", x.query)
    # for item in groups:
    #     print(item)
    # for delivery_info in total:
        # print(delivery_info.user)
        # print("factory name = ",delivery_info.factoryName.name)
        # if str(delivery_info.user) in str(delivery_info.factoryName.name):
        #     print("x", delivery_info.user)
    return render(request,'accounts/totalBill.html',)



