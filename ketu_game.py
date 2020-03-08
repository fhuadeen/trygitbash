def commute():
  ojuelegba = input("""At Ojuelegba, on your way to Lands in Alausa,
  which bus is best to take, Ketu or Ikeja?""")

  ketu = "Ketu"
  ikeja = "Ikeja"

  if ojuelegba == ikeja:
    input("""Drop where:
    Maryland or Computer Village?""")

    mary = "Maryland"
    comp = "Computer Village"

    if ikeja == mary:
      print("You lost, learn more about the route")
    elif ikeja == "Computer Village":
      input("""Take which bus next?
      Ogba or Berger""")

      ogba = "Ogba"
      berger =

      if comp == "Ogba":
        print("You lost, learn more about the route")
      elif comp == "Berger":
        print("""Good job!
        Though you're a novice of the best route.
        You spent N350 and one hour""")
      else:
        print("Please input Ogba or Berger")
    else:
      print("Please input Maryland or Computer Village")

  elif ojuelegba == ketu:
    input("""Drop where?
    Ojota or Tipper""")

    ojota = "Ojota"
    tipper = "Tipper"

    if ketu == ojota:
      input("""Where next?
      Opebi or Secretariat""")

      opebi = "Opebi"
      sec = "Secretariat"

      if ojota == opebi:
        print("You lost. Learn more about the route")
      elif ojota == sec:
        print("""Better job!
        However, you're an intermediate of the best route.
        You spent N300 and 50 minutes""")
      else:
        print("Please input Opebi or Secretariat")
    elif ketu == tipper:
      input("""Where next?
      Magodo or Otedola""")

      mag = "Magodo"
      ote = "Otedola"

      if tipper == mag:
        print("You lost. Learn more about the route")
      elif tipper == ote:
        print("""Great job!
        You're an expert of the best route.
        You spent N300 and 40 minutes""")
      else:
        print("Please input Magodo or Otedola")
    else:
      print("Please input Ojota or Tipper")

  else:
    print("Please input Ikeja or Ketu")

#from Jubril

def commute():
    Location = input('Where are you possible route: Ketu or Ikeja ')
    if Location == 'ketu':
        Next = input('Next stop: Ojota or Tipper ')
        if  Next == 'ojota':
            Next1 = input('Next stop: Opebi or Secretariat ')
            if Next1 == 'opebi':
                print('Wrong destination, Try know your route')
            elif Next1 == 'secretariat':
                print('Hurray, Welcome to the Office')
        elif Next == 'tipper':
            Next2 = ('Next stop: Magodo or Otedola')
            if Next2 == 'magodo':
                print('Wrong destination, Ogbeni know your way')
            elif Next2 == 'otedola':
                print('Very close to the office, not bad')
    elif Location == 'ikeja':
        Next3= input('Next stop: Maryland or Computer Village')
        if Next3 == 'maryland':
            print('Ogbeni, you have lost, better find urself')
        elif Next3 == 'computer village':
            Next4 = input('Next stop: Ogba or Berger')
            if Next4 == 'ogba':
                print('My Guy, Take back that ur previous route')
            elif Next4 == 'berger':
                print('Close to work, but trekking dey for u',"Good job! Though you're a novice of the best route You spent N350 and one hour")
    else:
        print('check wetin you press!!!')
    return 'Are we there yet!!!!'
