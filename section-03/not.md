https://github.com/philippython/Python-FullStack-Mastery

python -m pip install django==5.1.1
python -m django --version




--- 
To migrate the app models to database first register the app in INSTALLED_APPS in setting.py and then run command 
python manage.py makemigrations 
It create file 0001_initial.py in `__pychache__`





To show models in admin pannel ,we have to register the app ,and then in admin .py file in app 
from poll.models import *




1) To captute the id from url http://127.0.0.1:8000/2,
here slug is 2 and it must be intger ore;se it gives error
path('<int:question_id>',detail,name="grab_questions")
In above the 2 id will be save in question_id ,and then it is used in to retrieve id as a questions_id in detail.py in views.py
2) http://127.0.0.1:8000/100/vote   ,slug is 100 ,urls match is path('<int:question_id>/vote',vote,name="results")


This is url ,poll:grab_questions is app_name='poll' in urls.py and grab_questions is also name of urls mapping also called pattern name or view name and where to go,question.id is slug
<li><a href="{% url 'poll:grab_questions' question.id %}">{{ question.text }}</a></li>
its importat to write because of to avoid confusion between lot of apps in project


Cross Site Request Forgeries. =csrf token




https://docs.google.com/document/d/1X3TLGgg83dgwAFp5uo2C5Vs5pOJ32gmnBtfTmnGKSaU/edit?usp=sharing
https://docs.google.com/document/d/1TRw7TtRb4fJf6Vxw2BOHgVNELrA85F_l3A2O7wZAlbA/edit?tab=t.0#heading=h.5u4u6jw4r7k8
https://docs.google.com/document/d/1hFS3SciEmkj1tsFJlqcjij0OPTf1ibod3fMxWM_d-wk/edit?tab=t.0#heading=h.mz6w80pfgmxw

