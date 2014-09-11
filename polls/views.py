from django.shortcuts import render , render_to_response
from django.http import HttpResponse
from models import Question,Choice,Product,Manufacturer,ProductFilter
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# output = ', '.join([p.question_text for p in latest_question_list])
	return render(request , 'polls/index.html',{'latest_question_list':latest_question_list})

def detail(request, question_id):
	obj=get_object_or_404(Question,pk = question_id)
	return render(request, 'polls/details.html' ,{'question':obj})

def results(request, question_id):
	question = get_object_or_404(Question,pk = question_id)
	return render(request,'polls/results.html',{'question':question })

def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
	# Redisplay the question voting form.
		return render(request, 'polls/details.html', {'question': p,'error_message': "You didn't select a choice.",})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
    	return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def product_list(request):
	f = ProductFilter(request.GET, queryset=Product.objects.all())
	return render_to_response('polls/product.html', {'filter': f})