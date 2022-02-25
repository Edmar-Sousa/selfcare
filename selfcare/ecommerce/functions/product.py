from ecommerce.form  import FormProduct
from ecommerce.models import ProductModel

def addProductInDatabase(request):
    form = FormProduct(request.POST, request.FILES)

    if form.is_valid():
        productimage = form.cleaned_data['productimage']
        description  = form.cleaned_data['description']

        title = form.cleaned_data['title']
        price = form.cleaned_data['price']

        userLoggedIn = request.user

        productSaveInModel = ProductModel(
            user=userLoggedIn, 
            productImage=productimage, 
            description=description, 
            title=title, 
            price=price
        )
        productSaveInModel.save()

        return { 'is_valid' : True, 'msg' : 'Registrado com sucesso' }

    else:
        return { 'is_valid' : False, 'form_data' : form, 'msg' : 'ha alguns campos invalidos' }