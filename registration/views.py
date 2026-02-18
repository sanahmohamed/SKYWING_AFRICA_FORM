from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from .forms import RegistrationForm
from .models import Registration


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@require_http_methods(["GET", "POST"])
def registration_view(request):
    """Main registration form view"""
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.ip_address = get_client_ip(request)
            registration.save()

            # Check if AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'message': 'Registration submitted successfully!',
                    'redirect': '/success/'
                })

            messages.success(
                request,
                f'Thank you {registration.full_name}! Your registration has been submitted successfully.'
            )
            return redirect('success')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                errors = {}
                for field, error_list in form.errors.items():
                    errors[field] = [str(e) for e in error_list]
                return JsonResponse({'success': False, 'errors': errors}, status=400)

            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()

    return render(request, 'registration/form.html', {'form': form})


def success_view(request):
    """Success page after registration"""
    return render(request, 'registration/success.html')


def admin_registrations(request):
    """Simple admin view to see all registrations"""
    registrations = Registration.objects.all().order_by('-submitted_at')
    paginator = Paginator(registrations, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'total_count': registrations.count(),
    }
    return render(request, 'registration/admin_list.html', context)
