name="  JoHN  ."
y=name.strip().lower().replace('.','')
print(y)
name="EmmANuel"
y=name.casefold()
print(y)
text="The Dog Breed is German Shepherd"
print(text[8:])
text="Defeats for the Clinton forces,this was her moment of triumph"
print(text[16:30])
name='The lazy dog;ran so fast;it hit the wall.'
print(len(name))
first_name=' Joh.n'
last_name=' Do,e'
full_name=first_name+last_name
full_name=full_name.replace('.','')
full_name=full_name.replace(',','')
print(full_name.strip())
r='["E","W","C"]'
clean_r=r.replace("[","").replace("]","").replace('"',"").replace(",","")
print(clean_r)