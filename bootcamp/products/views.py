from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from .forms import ProductModelForm
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
def bad_view(request):
    # print(dict(request.GET))
    my_request_data = dict(request.GET)
    new_product = my_request_data.get("new_product")
    print(my_request_data, new_product)
    if new_product[0].lower() == "true":
        print("new product")
        Product.objects.create(title=my_request_data.get('title')
        [0], content=my_request_data.get('content')[0])
    return HttpResponse('Dont do this')

# def product_create_view(request, *args, **kwargs):
#     # print(request.POST)
#     # print(request.GET)
#     if request.method == "POST":
#         post_data = request.POST or None
#         if post_data != None:
#             my_form = ProductForm(request.POST)
#             # print(my_form.is_valid())
#             if my_form.is_valid():
#                 print(my_form.cleaned_data.get('title'))
#                 title_from_input = my_form.cleaned_data.get('title')
#                 Product.objects.create(title=title_from_input)
#             print("post data :", post_data)
#     return render(request, "products/forms.html")
@staff_member_required

def product_create_view(request, *args, **kwargs):
    form = ProductModelForm(request.POST or None, 
                            request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        image = request.FILES['image']
        # do some stuff
        obj.image = image
        obj.user = request.user
        # obj.user.is_staff = True
        # obj.user = obj.user.is_staff=True  if obj.user.is_superuser==False else obj.user
        # import pdb;pdb.set_trace()
        obj.save()

        # print(request.POST)
        # print(form.cleaned_data)
        # data = form.cleaned_data
        # Product.objects.create(**data)
    # its also valid but 3 lines of code
    # if request.method == 'POST':
    #     form = ProductForm(request.POST)
    # options
        form = ProductModelForm()
    # return HttpResponseRedirect("/success")
    # return redirect("/success")
    return render(request, "products/forms.html", {"forms": form})

def search_view(request, *args,**kwargs):
    print(args, kwargs)
    query = request.GET.get('q')
    print(query)
    qs = Product.objects.filter(title__icontains=query[0])
    print(qs)
    # return HttpResponse("<h1>Hello Pranav</h1>")
    context = {'neeps':1986, 'query': query}
    return render(request, 'products/home.html', context)

def product_api_detail_view(request, pk):
    print(object)
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"message": "Not Found Mr pranav"})
    print(dir(request))
    return render(request, 'products/detail.html', {'object':obj})
    
def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all()
    context = {'object_list': qs}
    print(context)
    return render(request, 'products/list.html', context)

