import csv
import xlwt


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from .forms import *
from .models import *
from .decorators import *
from .filters import *


#==================================================================
#LOGIN AND REGISTER VIEWS
#==================================================================
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='data clerks')
            user.groups.add(group)

            messages.success(request, 'Account created for ' + username + ', Please LogIn!')
            return redirect('login')


    context = {
        'form' : form
    }
    return render(request, 'register.html', context)
#=================================================================
@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Wrong Username OR Password!')
            

    context = {}
    return render(request, 'login.html', context)
#=================================================================
def logoutUser(request):
    logout(request)
    return redirect('login')

#==================================================================
# home view
#==================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','data clerks'])
def home(request):
    title = 'Welcome: This is the Home Page'
#==================================================================
# querysets to count the delagates in each category
    queryset = NonPaying.objects.all()
    queryset1 = Paying.objects.all()
    queryset2 = Sponsorship.objects.all()
    queryset3 = Exibitor.objects.all()

    total_nonpayee = queryset.count()
    total_payee = queryset1.count()
    total_sponsors = queryset2.count()
    total_exibitors = queryset3.count()

    context = {
        "title": title,
        "total_nonpayee": total_nonpayee,
        "total_payee": total_payee,
        "total_sponsors": total_sponsors,
        "total_exibitors": total_exibitors,
        'queryset': queryset,
        'queryset1': queryset1,
        'queryset2': queryset2,
        'queryset3': queryset3,
    }
    return render(request, "home.html", context)


#==================================================================
# views for each category form
#==================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','data clerks'])
def nonpaying_form(request):
    title = 'Add Non-Paying Delagate'
    form = NonPayingForm(request.POST or None) 
    if form.is_valid():
        form.save()
        return redirect('/nonpaying')
    context = {
        "title": title,
        "form": form,
    }
    return render(request, "NonPaying.html",context)
#==================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','data clerks'])
def paying_form(request):
    title = 'Add Paying Delagate'
    form = PayingForm(request.POST or None) 
    if form.is_valid():
        form.save()
        return redirect('/paying')
    context = {
        "title": title,
        "form": form,
    }
    return render(request, "Paying.html",context)
#==================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','data clerks'])
def sponsorship_form(request):
    title = 'Add Sponsor'
    form = SponsorshipForm(request.POST or None) 
    if form.is_valid():
        form.save()
        return redirect('/sponsorship')
    context = {
        "title": title,
        "form": form,
    }
    return render(request, "Sponsorship.html",context)
#==================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','data clerks'])
def exibitor_form(request):
    title = 'Add Exibitor '
    form = ExibitorForm(request.POST or None) 
    if form.is_valid():
        form.save()
        return redirect('/exibitor')
    context = {
        "title": title,
        "form": form,
    }
    return render(request, "Exibitor.html",context)

#===================================================================
#views for contents of each category
#===================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','data clerks'])
def nonpaying_view(request):
    title = 'List of Nonpaying Delagates'
    queryset = NonPaying.objects.all()
    myFilter = NonPayingFilter(request.GET, queryset=queryset)
    queryset = myFilter.qs
    context = {
        "title": title,
        'queryset': queryset,
        'myFilter': myFilter,
    }
    return render(request, "Nonpayingview.html",context)
#===================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','data clerks'])
def paying_view(request):
    title = 'List of Paying Delagates'
    queryset = Paying.objects.all()
    myFilter = PayingFilter(request.GET, queryset=queryset)
    queryset = myFilter.qs
    context = {
        "title": title,
        'queryset': queryset,
        'myFilter': myFilter,
    }
    return render(request, "Payingview.html",context)
#====================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','data clerks'])
def sponsorship_view(request):
    title = 'List of Sponser Delagates'
    queryset = Sponsorship.objects.all()
    myFilter = SponsorshipFilter(request.GET, queryset=queryset)
    queryset = myFilter.qs
    context = {
        "title": title,
        'queryset': queryset,
        'myFilter': myFilter,
    }
    return render(request, "Sponsorshipview.html",context)
#====================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','data clerks'])
def exibitor_view(request):
    title = 'List of Exibitor Delagates'
    queryset = Exibitor.objects.all()
    myFilter = ExibitorFilter(request.GET, queryset=queryset)
    queryset = myFilter.qs
    context = {
        "title": title,
        'queryset': queryset,
        'myFilter': myFilter,
    }
    return render(request, "Exibitorview.html",context)

#=====================================================================
#individual delagate interface views
#=====================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def nonpaying_delagate(request, pk):
    delagate_nonpaying = NonPaying.objects.get(id=pk)
    context = {
        "delagate_nonpaying":delagate_nonpaying,
    }
    return render(request, "Nonpayingdelagate.html", context)
    
#=====================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def paying_delagate(request, pk):
    delagate_paying = Paying.objects.get(id=pk)
    context = {
        "delagate_paying":delagate_paying,
    }
    return render(request, "Paying_delagate.html", context)

#=====================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def sponsorship_delagate(request, pk):
    delagate_sponsorship = Sponsorship.objects.get(id=pk)
    context = {
        "delagate_sponsorship":delagate_sponsorship,
    }
    return render(request, "Sponsorship_delagate.html", context)

#=====================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def exibitor_delagate(request, pk):
    delagate_exibitor = Exibitor.objects.get(id=pk)
    context = {
        "delagate_exibitor":delagate_exibitor,
    }
    return render(request, "Exibitor_delagate.html", context)

#=======================================================================
#updating delagates. 
#=======================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateNonpaying(request, pk):

	delagate = NonPaying.objects.get(id=pk)
	form = NonPayingForm(instance=delagate)

	if request.method == 'POST':
		form = NonPayingForm(request.POST, instance=delagate)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'NonPaying.html', context)
#=====================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updatePaying(request, pk):

	delagate = Paying.objects.get(id=pk)
	form = PayingForm(instance=delagate)

	if request.method == 'POST':
		form = PayingForm(request.POST, instance=delagate)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'Paying.html', context)
#=====================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateSponsorship(request, pk):

	delagate = Sponsorship.objects.get(id=pk)
	form = SponsorshipForm(instance=delagate)

	if request.method == 'POST':
		form = SponsorshipForm(request.POST, instance=delagate)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'Sponsorship.html', context)
#========================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateExibitor(request, pk):

	delagate = Exibitor.objects.get(id=pk)
	form = ExibitorForm(instance=delagate)

	if request.method == 'POST':
		form = ExibitorForm(request.POST, instance=delagate)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'Exibitor.html', context)
#========================================================================
#deleting delagates
#========================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteNonpaying(request, pk):
	delagate = NonPaying.objects.get(id=pk)
	if request.method == "POST":
		delagate.delete()
		return redirect('Display1')

	context = {'item':delagate}
	return render(request, 'delete.html', context)

#========================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deletePaying(request, pk):
	delagate = Paying.objects.get(id=pk)
	if request.method == "POST":
		delagate.delete()
		return redirect('Display2')

	context = {'item':delagate}
	return render(request, 'delete_paying.html', context)

#========================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteSponsorship(request, pk):
	delagate = Sponsorship.objects.get(id=pk)
	if request.method == "POST":
		delagate.delete()
		return redirect('Display3')

	context = {'item':delagate}
	return render(request, 'delete_sponsor.html', context)
#========================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteExibitor(request, pk):
	delagate = Exibitor.objects.get(id=pk)
	if request.method == "POST":
		delagate.delete()
		return redirect('Display4')

	context = {'item':delagate}
	return render(request, 'delete_exibitor.html', context)

#========================================================================
#exporting to csv
#========================================================================
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def export(request):
    items = NonPaying.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Dsiposition'] = 'attachment; filename="Nonpaying.csv"'

    write = csv.writer(response, delimiter='|')
    write.writerow(['Name','Surname','Organisation','Email'])

    for obj in items:
        write.writerow([obj.Name,obj.Surname,obj.Organisation,obj.Email])

    return response

#========================================================================
#exporting to excel
#========================================================================
def export_NP(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="nonpaying.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Name', 'Surname', 'Organisation', 'Email']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = NonPaying.objects.all().values_list('Name', 'Surname', 'Organisation', 'Email')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

#========================================================================
def export_P(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="paying.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Name', 'Surname', 'Organisation', 'Email', 'InvoiceNum', 'ReceiptNum', 'Amount', 'Options', 'Payment_Date' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Paying.objects.all().values_list('Name', 'Surname', 'Organisation', 'Email', 'InvoiceNum', 'ReceiptNum', 'Amount', 'Options', 'Payment_Date' )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

#========================================================================
def export_S(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Sponsors.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Name', 'Surname', 'Organisation', 'Email', 'InvoiceNum', 'ReceiptNum', 'Amount', 'Packages', 'Payment_Date' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Sponsorship.objects.all().values_list('Name', 'Surname', 'Organisation', 'Email', 'InvoiceNum', 'ReceiptNum', 'Amount', 'Packages', 'Payment_Date' )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

#========================================================================
def export_E(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Exibitors.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Name', 'Surname', 'Organisation', 'Email', 'InvoiceNum', 'ReceiptNum', 'Amount', 'Payment_Date' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Exibitor.objects.all().values_list('Name', 'Surname', 'Organisation', 'Email', 'InvoiceNum', 'ReceiptNum', 'Amount', 'Payment_Date' )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response

#========================================================================

