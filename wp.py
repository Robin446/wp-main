with open('numbers.txt','r') as o, open('output.html','w') as s, open('text.txt','r') as t:
    lines = o.readlines()
    msg = t.readline()
    for lines in lines:
        s.write(f'<a target="blank" href={"https://api.whatsapp.com/send/?phone=91"+lines+"&text="+msg+""} >'+lines+' </a>')
