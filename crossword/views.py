from django.shortcuts import render,get_object_or_404
from .models import Crossword,Crosswordcheck
from datetime import datetime
from django.views.decorators.csrf import csrf_protect
  

@csrf_protect
def crossword_check(request):
  
  crossword = Crossword.objects.all()
  crossword_across= Crossword.objects.all().filter(is_across=True)
  crossword_down= Crossword.objects.all().filter(is_across=False)

  word_list =[]
  list_word_list=[]
  for crossword in crossword:
    word_list =[]
    word_len = len(str(crossword.word))
    word_list.append(crossword.word)
    word_list.append(word_len)
    word_list.append(crossword.start_position) 
    word_list.append(crossword.start_position_x) 
    word_list.append(crossword.start_position_y )
    word_list.append(crossword.clue)  
    list_word_list.append(word_list)
  
  all_word_list = list_word_list  
  
  word_list =[]
  list_word_list=[]
  for crossword in crossword_down:
    word_list =[]
    word_len = len(str(crossword.word))
    word_list.append(crossword.word)
    word_list.append(word_len)
    word_list.append(crossword.start_position) 
    word_list.append(crossword.start_position_x) 
    word_list.append(crossword.start_position_y )
    word_list.append(crossword.clue)  
    list_word_list.append(word_list)
  
  word_down_list = list_word_list
  

  word_list =[]
  list_word_list=[]
  for crossword in crossword_across:
    word_list =[]
    word_len = len(str(crossword.word))
    word_list.append(crossword.word)
    word_list.append(word_len)
    word_list.append(crossword.start_position) 
    word_list.append(crossword.start_position_x) 
    word_list.append(crossword.start_position_y )
    word_list.append(crossword.clue)  
    list_word_list.append(word_list)
  
  word_across_list = list_word_list
 

  x=[]
  y=[]
  for item in word_across_list:
    x.append(int(item[3])+int(item[1]))
    max_x_coordinate = max(x)  
  for item in word_down_list:
    y.append(int(item[4])+int(item[1]))
    max_y_coordinate = max(y)     

  
  def is_occupied(x,y):
    flag_across= True
    flag_down= True
    for item in word_across_list:
      if item[4] == y:
        if x>=item[3] and x<=(item[3]+item[1]-1):
          flag_across = True
          break
        else:
          flag_across=False
      else:
        flag_across=False
    
    for item in word_down_list:
      if item[3] == x:
        if y>=item[4] and y<=(item[4]+item[1]-1):    
          flag_down=True
          break
        else:
          flag_down=False
      else:
        flag_down=False

    return flag_across or flag_down
  
  

  
  empty_cells=[]
  all_cells=[]

  for i in range(max_x_coordinate):
    for j in range(max_y_coordinate):
      all_cells.append([i,j])
  for i in range(max_x_coordinate):
    for j in range(max_y_coordinate):
      if is_occupied(i,j) == False:
        empty_cells.append([i,j])

  
      
  
  
  if request.method == 'POST' and request.is_ajax():
    crosswordcheck = Crosswordcheck(name="do",email="do@po.com",result="asdf")
    crosswordcheck.save()
    result = request.POST.get('city')
    crosswordcheck.result = result
    crosswordcheck.save()
    
  
  if request.method == 'POST' and request.is_ajax() == False:
    crosswordcheck = Crosswordcheck.objects.all().last()
    name = request.POST['name']
    email = request.POST['email']
  
    crosswordcheck.name = name
    crosswordcheck.email = email
    
    
    subscribe_yes = request.POST.get('wish_to_subscribe', False )
    if subscribe_yes == 'on':
      subscribe_yes = True
    if subscribe_yes == 'off':
      subscribe_yes = False
    crosswordcheck.subscribe_yes = subscribe_yes

    crosswordcheck.save()
    
  return render(request, 'pages/contestsubmit.html')



@csrf_protect
def crossword(request):
  crossword = Crossword.objects.all()
  crossword_across= Crossword.objects.all().filter(is_across=True)
  crossword_down= Crossword.objects.all().filter(is_across=False)

  
  word_list =[]
  list_word_list=[]
  for crossword in crossword:
    word_list =[]
    word_len = len(str(crossword.word))
    word_list.append(crossword.word)
    word_list.append(word_len)
    word_list.append(crossword.start_position) 
    word_list.append(crossword.start_position_x) 
    word_list.append(crossword.start_position_y )
    word_list.append(crossword.clue)  
    list_word_list.append(word_list)
  
  all_word_list = list_word_list

  word_list =[]
  list_word_list=[]
  for crossword in crossword_down:
    word_list =[]
    word_len = len(str(crossword.word))
    word_list.append(crossword.word)
    word_list.append(word_len)
    word_list.append(crossword.start_position) 
    word_list.append(crossword.start_position_x) 
    word_list.append(crossword.start_position_y )
    word_list.append(crossword.clue)  
    list_word_list.append(word_list)
  
  word_down_list = list_word_list
  

  word_list =[]
  list_word_list=[]
  for crossword in crossword_across:
    word_list =[]
    word_len = len(str(crossword.word))
    word_list.append(crossword.word)
    word_list.append(word_len)
    word_list.append(crossword.start_position) 
    word_list.append(crossword.start_position_x) 
    word_list.append(crossword.start_position_y )
    word_list.append(crossword.clue)  
    list_word_list.append(word_list)
  
  word_across_list = list_word_list

  

  

  
  
  
 
  
    
  # # end_position_x = crossword_across.order_by('-start_position_x').first().start_position_x + len(crossword_across.order_by('-start_position_x').first().word)
  # # end_position_y = crossword_down.order_by('-start_position_y').first().start_position_y + len(crossword_down.order_by('-start_position_y').first().word)
  # # print(end_position_y)
  
  x=[]
  y=[]
  for item in word_across_list:
    x.append(int(item[3])+int(item[1]))
    max_x_coordinate = max(x)  
  for item in word_down_list:
    y.append(int(item[4])+int(item[1]))
    max_y_coordinate = max(y)     

  
  def is_occupied(x,y):
    flag_across= True
    flag_down= True
    for item in word_across_list:
      if item[4] == y:
        if x>=item[3] and x<=(item[3]+item[1]-1):
          flag_across = True
          break
        else:
          flag_across=False
      else:
        flag_across=False
    
    for item in word_down_list:
      if item[3] == x:
        if y>=item[4] and y<=(item[4]+item[1]-1):    
          flag_down=True
          break
        else:
          flag_down=False
      else:
        flag_down=False

    return flag_across or flag_down
  
  

  
  empty_cells=[]
  all_cells=[]

  for i in range(max_x_coordinate):
    for j in range(max_y_coordinate):
      all_cells.append([i,j])
  for i in range(max_x_coordinate):
    for j in range(max_y_coordinate):
      if is_occupied(i,j) == False:
        empty_cells.append([i,j])
      
  
  


  
  
  context = {
    'crossword':crossword,
    'crossword_across':crossword_across,
    'crossword_down':crossword_down,
    'max_x_coordinate':max_x_coordinate,
    'max_y_coordinate':max_y_coordinate,
    'empty_cells':empty_cells,
    'all_cells':all_cells,
    'word_across_list':word_across_list,
    'word_down_list':word_down_list,
    'all_word_list':all_word_list,
    # 'start_position_across':start_position_across,
  }
  return render(request, 'pages/cross.html', context)
