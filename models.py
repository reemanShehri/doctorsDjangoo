from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext_lazy
from django.db.models.signals import post_save
from django.utils.text import slugify
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _


# Create your models here.


TYPE_OF_PERSON=(
    ('M', "MALE"),
    ('F',"FEMALE")
)

class Profiles(models.Model): 

    DOCTOR_IN = (
         ("أطفال", "أطفال"),
           ("أسنان", "أسنان"), 
           ("أنف وأذن وحنجرة", "أنف وأذن وحنجرة"),
             ("أطفال حديثي الولادة", "أطفال حديثي الولادة"),
               ("قلب وأوعية دموية", "قلب وأوعية دموية"),
                 ("عظام", "عظام"), 
                 ("جلدية", "جلدية"), 
                 ("أمراض نساء وتوليد", "أمراض نساء وتوليد"), 
                 ("أمراض باطنية", "أمراض باطنية"),
                   ("عيون", "عيون"),
                     ("مخ وأعصاب", "مخ وأعصاب"),
                       ("جراحة عامة", "جراحة عامة"),
                         ("أمراض نفسية", "أمراض نفسية"),
                           ("أمراض الأطفال", "أمراض الأطفال"), 
                          ("الطب النفسي للأطفال والمراهقين", "لطب النفسي للأطفال والمراهقين")
    )
    
    user = models.OneToOneField(User, verbose_name="user", on_delete=models.CASCADE,null=True, blank=True)
    
    name = models.CharField("الاسم", max_length=80,null=True, blank=True) 
    surname = models.CharField(" الاصلي الاسم", max_length=80,null=True, blank=True) 

    subtitle = models.CharField("عنوان", max_length=50,null=True, blank=True) 
    address = models.CharField("العنوان", max_length=50,null=True, blank=True) 
    address_detail = models.CharField("تفاصيل العنوان", max_length=50,null=True, blank=True) 
    number_phone = models.CharField("رقم الهاتف", max_length=50,null=True, blank=True)
    working_hours = models.CharField("عدد ساعات العمل", max_length=50,null=True, blank=True)
    Waiting_time = models.IntegerField("مدة الانتظار", blank=True, null=True)
    facebook= models.URLField(null=True, blank=True)
    twitter= models.URLField(null=True, blank=True)
    google= models.URLField( null=True, blank=True)
    join=models.DateTimeField("وقت الانضمام :",  auto_now_add=True, blank=True, null=True)
    type_of_person= models.CharField("النوع: ", max_length=50,choices=TYPE_OF_PERSON,null=True, blank=True)
    first_name= models.CharField("الاسم الأول : ", max_length=50,null=True, blank=True)
    last_name= models.CharField("الاسم الاأخير : ", max_length=50,null=True, blank=True)


    doctor = models.CharField("الطبيب",  choices= DOCTOR_IN ,max_length=50, blank=True, null=True) 
    who_i = models.TextField("من انا", max_length=250, blank=True, null=True)
    price = models.IntegerField("السعر", blank=True, null=True) 
    image = models.ImageField(" الصورة ", upload_to='profile', blank=True, null=True) 
    Specialist_doctor = models.CharField("تخصص الطبيب", max_length=100, blank=True, null=True)
    slug=models.SlugField("slug", blank=True, null=True)
# slug shows in yrl as www.facebook.com/reeman12 ,, reeman12 is a slug
    

#if not written slug to make a default
    def save(self, *args, **kwargs):
       if not self.slug:
          self.slug =slugify(self.user.username)
       super(Profiles, self).save(*args, **kwargs) # Call the real save() method

    class Meta:
        verbose_name=("Profiles")
        verbose_name_plural=("Profiles")


    def __str__(self):
        return f'{self.user.username}'    


def create_profile(sender , **kwargs):
    if kwargs['created']:
         Profiles.objects.create(user=kwargs['instance'])








class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label=_("الاسم الأول"), max_length=50)
    last_name = forms.CharField(label=_("الاسم الأخير"), max_length=50)
    email = forms.EmailField(label=_("البريد الإلكتروني"), max_length=254)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')





post_save.connect(create_profile, sender=User)
class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(label=_("الاسم الأول"), max_length=50)
    last_name = forms.CharField(label=_("الاسم الأخير"), max_length=50)
    email = forms.EmailField(label=_("البريد الإلكتروني"), max_length=254)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')




