from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import VendorForm
from accounts.models import User, Profile
from accounts.forms import UserForm



def registerVendor(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        ven_form = VendorForm(request.POST, request.FILES)
        if form.is_valid() and ven_form.is_valid:
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
            )
            user.role = User.VENDOR
            user.save()
            vendor = ven_form.save(commit=False)
            vendor.user = user
            profile = Profile.objects.get(user=user)
            vendor.profile = profile
            vendor.save()
            messages.success(request, 'Your account has been registered successfully! Please wait for approval.')
            return redirect('registerVendor')
        else:
            print(form.errors)
    else:
        form = UserForm()
        ven_form = VendorForm()
    context = {
        'form' : form,
        'ven_form' : ven_form,
    }
    return render(request, 'vendor/registerVendor.html', context)
