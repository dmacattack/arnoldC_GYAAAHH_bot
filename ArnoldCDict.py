### keyword replacement ###
dict = {
   "False" : "I LIED",
   "True" : "NO PROBLEMO",
   "If" : "BECAUSE I'M GOING TO SAY PLEASE",
   "if" : "BECAUSE I'M GOING TO SAY PLEASE",
   "Else" : "BULLSHIT",
   "else" : "BULLSHIT",
   "EndIf" : "YOU HAVE NO RESPECT FOR LOGIC",
   "While" : "STICK AROUND",
   "EndWhile" : "CHILL",
   " + " : "GET UP",
   " - " : "GET DOWN",
   " * " : "YOU'RE FIRED",
   " / " : "HE HAD TO SPLIT",
   " % " : "I LET HIM GO",
   "==" : "YOU ARE NOT YOU YOU ARE ME",
   " > " : "LET OFF SOME STEAM BENNET",
   " Or " : "CONSIDER THAT A DIVORCE",
   " || " : "CONSIDER THAT A DIVORCE",
   " And " : "KNOCK KNOCK",
   " && " : "KNOCK KNOCK",
   "DeclareMethod" : "LISTEN TO ME VERY CAREFULLY",
   "NonVoidMethod" : "GIVE THESE PEOPLE AIR",
   "MethodArguments" : "I NEED YOUR CLOTHES YOUR BOOTS AND YOUR MOTORCYCLE",
   "Return" : "I'LL BE BACK",
   "EndMethodDeclaration" : "HASTA LA VISTA, BABY",
   "CallMethod" : "DO IT NOW",
   "AssignVariableFromMethodCall" : "GET YOUR ASS TO MARS",
   "DeclareInt" : "HEY CHRISTMAS TREE",
   "SetInitialValue" : "YOU SET US UP",
   "BeginMain" : "IT'S SHOWTIME",
   "EndMain" : "YOU HAVE BEEN TERMINATED",
   "Print " : "TALK TO THE HAND",
   "printf" : "TALK TO THE HAND",
   "ReadInteger" : "I WANT TO ASK YOU A BUNCH OF QUESTIONS AND I WANT TO HAVE THEM ANSWERED IMMEDIATELY",
   "AssignVariable" : "GET TO THE CHOPPER",
   "SetValue" : "HERE IS MY INVITATION",
   "EndAssignVariable" : "ENOUGH TALK",
   "ParseError" : "WHAT THE FUCK DID I DO WRONG"
   }
# keyword replacement
def translate(codeStr):
   for key in dict:
      codeStr = codeStr.replace(key, dict[key])
   return codeStr