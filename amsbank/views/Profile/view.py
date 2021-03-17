from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from amsbank.service_provider import ams_service_provider


@login_required(redirect_field_name='next')
def profile_view(request):
    user_id = request.user.id
    account_holder = ams_service_provider.account_holder_management_service().get_details_by_user(user_id)
    account = ams_service_provider.account_management_service().get_account_with_account_holder(account_holder.id)

    context = {
        'account_name': account_holder.first_name,
        'account_number': account.account_number

    }
    return render(request, 'profile.html', context)
