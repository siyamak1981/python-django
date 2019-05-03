from django import forms
from mysite.models import Contact
from painless.models.error_messages import Messages 
msg = Messages()

class CantactForm(forms.ModelForm):
    fullname = forms.CharField(label ="نام و نام خانوادگی", error_messages = {
                            'required':msg.required,
                            'max_length':msg.max_length(128)
            })
    email = forms.EmailField(label ="ایمیل", error_messages = {
                            'required':msg.required,
                            'max_length':msg.max_length(128)
            })
        
    title = forms.CharField(label =" عنوان", error_messages = {
                            'required':msg.required,
                            'max_length':msg.max_length(128)
            })
    message = forms.CharField(widget = forms.Textarea, label =" پیام" , error_messages = {
                            'required':msg.required,
                            'max_length':msg.max_length(128)
            })

    fullname.widget.attrs.update({"class":"form-control", "autofocus":"True"})
    email.widget.attrs.update({"class":"form-control", "placeholder": "example@gmail.com", "style": "direction=ltr;"})
    title.widget.attrs.update({"class":"form-control"})
    message.widget.attrs.update({"class":"form-control", "placeholder": "درخواست خود را مکاتبه نمایید"})

    class Meta:
        model = Contact
        fields = ('fullname', 'email', 'title')

        