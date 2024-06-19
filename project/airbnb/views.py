from django.shortcuts import render, redirect
from django.http import JsonResponse
from airbnb.models import User, Property
from airbnb.forms import PropertyForm, SignUpUserForm
from airbnb.utils import hash_password, check_password
from airbnb.serializers import PropertySerializer

COOKIE_NAME = 'airbnb'

def get_user_by_id(id: str):
    return User.objects.get(pk = id)

def get_user_by_username(username: str):
    return User.objects.get(username = username)

def get_user_from_cookie(req):
    id = req.COOKIES.get(COOKIE_NAME)

    if id:
        return get_user_by_id(id)
    else:
        None

def get_properties():
    return Property.objects.all()

def signup(req):
    if (req.method == 'POST'):
        form = SignUpUserForm(req.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.password = hash_password(user.password)
            user.save()

            redirect('signin')

    return render(req, 'signup.html')

def signin(req):
    user = get_user_from_cookie(req)

    if user is not None:
        return redirect('main')

    if (req.method == 'POST'):
        username = req.POST['username']
        password = req.POST['password']

        user = get_user_by_username(username)
        is_password = check_password(password, user.password)

        print(is_password)

        if is_password:
            res = redirect('main')
            res.set_cookie(COOKIE_NAME, user.pk)
            return res

    return render(req, 'signin.html')

def logout(req):
    res = redirect('signin')
    res.set_cookie(COOKIE_NAME)
    return res

def main(req):
    user = get_user_from_cookie(req)
    properties = get_properties()

    return render(req, 'main.html', {
        'properties': properties,
        'user': user
    })

def create_property(req):
    user = get_user_from_cookie(req)

    if user is None:
        return redirect('signin')

    print(user)

    if req.method == 'POST':
        form = PropertyForm(req.POST)

        if form.is_valid():
            property_instance = form.save(commit=False)
            property_instance.owner = user
            property_instance.save()
            return redirect('main')
    else:
        form = PropertyForm()

    return render(req, 'create-property.html', {'form': form})

def api_properties(req):
    properties = get_properties()
    json_properties = PropertySerializer(properties, many=True)

    return JsonResponse(json_properties.data, safe=False)
