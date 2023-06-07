import collections, sys, os
from logic import *

############################################################
# Problem 1: propositional logic
# Convert each of the following natural language sentences into a propositional
# logic formula.  See rainWet() in examples.py for a relevant example.
# sentence: If I have a deadline tomorrow and I'm watching TV, then I'm not being very productive.
def formula1a():
    # Predicates to use:
    tomorrow = Atom('Tomorrow')               # whether it's
    TV = Atom('TV')                 # whether watching TV
    productive = Atom('Productive')               # whether it's productive
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    #raise Exception("Not implemented yet")
    return Implies(And(tomorrow, TV), Not(productive))
    # END_YOUR_CODE

# sentence: Either I'll go to the gym or go for a run (but not both).
def formula1b():
    # Predicates to use:
    gym = Atom('Gym')     # whether it's gym
    run = Atom('Run') # whether it's night
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    #raise Exception("Not implemented yet")
    return And(Or(gym, run), Not(And(gym, run)))
    # END_YOUR_CODE

# sentence: The store is open if and only if the sign says "open" and the lights are on.
def formula1c():
    # Predicates to use:
    store = Atom('Store')              # whether it is store
    O = Atom('Open')                # whether it it open
    lights = Atom('Lights')  # whether the lights are on
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    #raise Exception("Not implemented yet")
    return And(Implies(And(O, lights), store), Implies(store, And(O, lights)))
    # END_YOUR_CODE

############################################################
# Problem 2: first-order logic
# sentence: some people are students, some people are teacher. 
# There exists at least 1 student and 1 teacher, any person must either be a student or a teacher. 
# only student can learn, and only teacher can teach. Every student must have at least one teacher
def formula2a():
    # Predicates to use:
    def Student(x): return Atom('Student', x)
    def Teacher(x): return Atom('Teacher', x)
    def Teaches(x, y): return Atom('Teaches', x, y)

    # Statements as first-order logic:

    # Every object is either a student or a teacher
    f1 = Forall('$x', Or(Student('$x'), Teacher('$x')))

    # but not at the same time
    f2 = And(Forall('$x', Implies(Student('$x'), Not(Teacher('$x')))), Forall('$x', Implies(Teacher('$x'), Not(Student('$x')))))

    # There exists at least one student and at least one teacher
    f3 = And(Exists('$x', Student('$x')), Exists('$x', Teacher('$x')))

    # Only students can learn, and only teachers can teach
    f4 = And(
        Forall('$x', Forall('$y', Implies(Teaches('$y', '$x'), Student('$x')))),
        Forall('$x', Forall('$y', Implies(Teaches('$y', '$x'), Teacher('$y'))))
    )

    # Every student must have at least one teacher
    f5 = Forall('$x', Implies(Student('$x'), Exists('$y', And(Teacher('$y'), Teaches('$y', '$x')))))

    return AndList([f1, f2, f3, f4, f5])

# sentence: Teacher can also learn from teacher, but student cannot teach
def formula2b():
    # Predicates to use:
    def Student(x): return Atom('Student', x)
    def Teacher(x): return Atom('Teacher', x)
    def Teaches(x, y): return Atom('Teaches', x, y)

    # Statements as first-order logic:

    # Every object is either a student or a teacher
    f1 = Forall('$x', Or(Student('$x'), Teacher('$x')))

    # but not at the same time
    f2 = And(Forall('$x', Implies(Student('$x'), Not(Teacher('$x')))), Forall('$x', Implies(Teacher('$x'), Not(Student('$x')))))

    # There exists at least one student and at least one teacher
    f3 = And(Exists('$x', Student('$x')), Exists('$x', Teacher('$x')))

    # Only teacher can teach, both student and teacher can learn;
    f4 = And(
        Forall('$x', Forall('$y', Implies(Teaches('$y', '$x'), Or(Student('$x'), Teacher('$x'))))),
        Forall('$x', Forall('$y', Implies(Teaches('$y', '$x'), Teacher('$y'))))
    )

    # Every student must have at least one teacher
    f5 = Forall('$x', Implies(Student('$x'), Exists('$y', And(Teacher('$y'), Teaches('$y', '$x')))))

    return AndList([f1, f2, f3, f4, f5])


############################################################
# Problem 3: Liar puzzle
# Facts:
# • Adam says: "My shirt is not blue."
# • Levi says: "Adam’s shirt is red."
# • John says: "Levi’s shirt is not blue."
# • Luke says: "John’s shirt is blue.
# • You know that exactly one person is telling the truth 
# • and exactly one person is wearing a red shirt.
# # Query: Who is telling the truth?
# This function returns a list of 6 formulas corresponding to each of the above facts.
# Hint: You might want to use the Equals predicate, defined in logic.py.  
# This predicate is used to assert that two objects are the same.
# In particular, Equals(x,x) = True and Equals(x,y) = False iff x is not equal to y.

def liar():
    def WearsRed(x): return Atom('WearsRed', x)
    def TellTruth(x): return Atom('TellTruth', x)
    luke = Constant('luke')
    john = Constant('john')
    levi = Constant('levi')
    adam = Constant('adam')
    formulas = []
    # We provide the formula for fact 0 here.
    formulas.append(Equiv(TellTruth(adam), WearsRed(adam)))
    # You should add 5 formulas, one for each of facts 1-5.
    # BEGIN_YOUR_CODE 
    formulas.append(Equiv(TellTruth(levi), WearsRed(adam)))
    formulas.append(Equiv(TellTruth(john), WearsRed(levi)))
    formulas.append(Equiv(TellTruth(luke), Not(WearsRed(john))))

    formulas.append(AndList([
        OrList([TellTruth(adam), TellTruth(levi), TellTruth(john), TellTruth(luke)]),
        Not(And(TellTruth(adam), TellTruth(levi))),
        Not(And(TellTruth(adam), TellTruth(john))),
        Not(And(TellTruth(adam), TellTruth(luke))),
        Not(And(TellTruth(levi), TellTruth(john))),
        Not(And(TellTruth(levi), TellTruth(luke))),
        Not(And(TellTruth(john), TellTruth(luke)))
    ]))
    
    formulas.append(AndList([
        OrList([WearsRed(adam), WearsRed(levi), WearsRed(john), WearsRed(luke)]),
        Not(And(WearsRed(adam), WearsRed(levi))),
        Not(And(WearsRed(adam), WearsRed(john))),
        Not(And(WearsRed(adam), WearsRed(luke))),
        Not(And(WearsRed(levi), WearsRed(john))),
        Not(And(WearsRed(levi), WearsRed(luke))),
        Not(And(WearsRed(john), WearsRed(luke)))
    ]))
    # END_YOUR_CODE
    query = TellTruth('$x')
    return (formulas, query)

