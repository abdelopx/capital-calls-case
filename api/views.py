from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
import datetime
from api.calculations import get_membership_fee, get_upfront_fees, get_yearly_fees

from .models import Investor, Bill, CapitalCall
from .serializers import InvestorSerializer, BillSerializer, CapitalCallSerializer


class InvestorViewSet(viewsets.ModelViewSet):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer

class CapitalCallViewSet(viewsets.ModelViewSet):
    queryset = CapitalCall.objects.all()
    serializer_class = CapitalCallSerializer

    

class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        investor_name = self.request.query_params.get('investor_name')
        if investor_name:
            queryset = queryset.filter(investor__name__icontains=investor_name)
        return queryset

    @action(detail=False, methods=['post'])
    def generate_bills(self, request):
        investor_id = request.data.get('investor_id')
        fee_percentage = request.data.get('fee_percentage')
        amount_invested = request.data.get('amount_invested')
        investment_date = datetime.datetime.strptime(request.data.get('investment_date'), '%Y-%m-%d').date()
        investment_type = request.data.get('investment_type')
        investor = Investor.objects.get(id=investor_id)

        membership_fee = get_membership_fee(amount_invested)
        upfront_fees = get_upfront_fees(fee_percentage, amount_invested)
        yearly_fees = get_yearly_fees(investment_date, fee_percentage, amount_invested, 5)
        bills = []

        if investment_type == "upfront":
            bills.append(Bill.objects.create(investor=investor, bill_type=investment_type, amount=upfront_fees,due_date=datetime.date.today()))
        elif investment_type == "yearly":
            for yearly_fee in yearly_fees:
                bills.append(Bill.objects.create(investor=investor, bill_type=investment_type, amount=yearly_fee,due_date=datetime.date.today()))
        
        # if membership_fee > 0:
        #     bills.append(Bill.objects.create(investor=investor, bill_type='membership', amount=membership_fee, due_date=datetime.date.today()))
        
        return Response({'status': 'bills generated', 'bills': BillSerializer(bills, many=True).data}, status=status.HTTP_201_CREATED)
