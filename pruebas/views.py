from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ArgentinaStateForm
from django.views.generic import TemplateView
from .models import Blog
def flex(request):
    return render(request, 'pruebas/flexbox0.html')

def wrap(request):
    return render(request, 'pruebas/flexbox-wrap0.html')

class Temp2View(TemplateView):
    template_name='pruebas/temp2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = Blog.objects.all()
        context["titulo"] = 'Lista de blogs'
        return context
    


class ArgentinaStateFormView(FormView):
    template_name = 'pruebas/argentina_state_form.html'
    form_class = ArgentinaStateForm
    success_url = '/success/'

    def form_valid(self, form):
        form
        return super().form_valid(form)
    
# Certainly! Let's dive into the `form_valid` method in the context of the `ArgentinaStateFormView` class:

# 1. **`form_valid` Method**:
#     - The `form_valid` method is a callback method provided by `FormView`.
#     - It is called when the submitted form data is valid (i.e., all form fields pass validation).
#     - You can override this method to customize what happens after a valid form submission.
#     - By default, it redirects to the URL specified in the `success_url` attribute.

# 2. **Customization**:
#     - Inside the `form_valid` method, you can perform various actions:
#         - Save form data to the database (if applicable).
#         - Send emails or notifications.
#         - Perform additional business logic related to the form submission.
#         - Return an HTTP response (e.g., redirect to a success page).

# 3. **Example**:
#     - In your provided code snippet:
#         ```python
#         def form_valid(self, form):
#             # Handle form submission (save data, send emails, etc.)
#             # You can customize this method as needed.
#             return super().form_valid(form)
#         ```
#         - The default behavior is to call the superclass's `form_valid` method (which performs the redirect specified in `success_url`).
#         - You can add your custom logic here, such as saving form data to the database or sending notifications.

# 4. **Use Cases**:
#     - Common use cases for customizing `form_valid` include:
#         - Saving form data to a model (e.g., creating a new record).
#         - Sending confirmation emails.
#         - Logging successful form submissions.

# In summary, `form_valid` is a hook that allows you to handle valid form submissions in a customized way. You can override it to tailor the behavior according to your application's requirements.
