from django.forms import ModelForm


class OrganizationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['inn',
                  'name',
                  'rating',
                  'status',
                  'registration_date',
                  'employees_number',
                  'org_type']
