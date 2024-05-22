from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
import datetime
from api.calculations import calculate_capital_call, get_membership_fee, get_upfront_fees, get_yearly_fees

from .models import Investor, Bill, CapitalCall
from .serializers import InvestorSerializer, BillSerializer, CapitalCallSerializer


class InvestorViewSet(viewsets.ModelViewSet):
    queryset = Investor.objects.all()
    serializer_class = InvestorSerializer

class CapitalCallViewSet(viewsets.ModelViewSet):
    queryset = CapitalCall.objects.all()
    serializer_class = CapitalCallSerializer

    @action(detail=False, methods=['post'])
    def generate_capital_call(self, request):
        bill_ids = request.data.get('bills')
        investor_id = request.data.get('investor')
        status = request.data.get('status')
        due_date=request.data.get('due_date')
        
        generated_capital_call = calculate_capital_call(bill_ids, investor_id, status, due_date)
        return Response({'status': 'Capital call generated', 'capital_call': CapitalCallSerializer(generated_capital_call).data}, status=status.HTTP_201_CREATED)
    

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
        investor_id = request.data.get('investor')
        fee_percentage = request.data.get('fee_percentage')
        amount_invested = request.data.get('amount')
        investment_date = datetime.datetime.strptime(request.data.get('investment_date'), '%Y-%m-%d').date()
        investment_type = request.data.get('bill_type')
        name = request.data.get('name')
        investor = Investor.objects.get(id=investor_id)

        membership_fee = get_membership_fee(amount_invested)
        bills = []

        if investment_type == "upfront_fees":
            upfront_fees = get_upfront_fees(fee_percentage, amount_invested)
            bills.append(Bill.objects.create(investor=investor, bill_type=investment_type, fee_percentage=fee_percentage, amount=upfront_fees + membership_fee,due_date=datetime.date(investment_date.year, 12, 31), name=name))
        elif investment_type == "yearly_fees":
            print(amount_invested)
            yearly_fees = get_yearly_fees(investment_date, fee_percentage, amount_invested, 5)
            for index, yearly_fee in enumerate(yearly_fees):
                bills.append(Bill.objects.create(investor=investor, bill_type=investment_type, fee_percentage=fee_percentage, amount=yearly_fee + membership_fee,due_date=datetime.date(investment_date.year + index, 12, 31), name=name))
        
        return Response({'status': 'bills generated', 'bills': BillSerializer(bills, many=True).data}, status=status.HTTP_201_CREATED)
