% Author:
% Date: 12/24/2018

:- use_module(library(random)).
student(ali).
student(usama).
student(saad).
student(umer).
student(balaj).
student(abdullah).
student(bilal).
student(waleed).
student(basit).
student(farukh).
courses(hci).
courses(networking).
courses(datamining).
courses(mobileapp).
courses(calculus).
courses(programing).
courses(database).
courses(oop).
courses(datastructure).
courses(linearalgebra).
faculty(saroor).
faculty(saeed).
faculty(rashid).
faculty(maryam).
faculty(rida).
faculty(sehar).
faculty(naila).
faculty(mehwish).
faculty(aliya).

start:-write("hello i m advia how my i help you."),conv.
conv:-
repeat,
   read(X),
   nl,
   give_reply(X,Y),
   write(Y),
   nl,
   conv,
   !.


reply(bye, [
        'bye!',
        'hope to see you again.',
        'have a nice day!',
        'bye, have a nice day!'
        
        ]).
reply(hello, [
         'Hello!',
        'Hello, nice to meet you.',
        'Hi there!',
        'Welcome!',
        'Good afternoon!',
        'Hi.'

        ]).
reply(hi, [
         'Hello!',
        'Hello, nice to meet you.',
        'Hi there!',
        'Welcome!',
        'Good afternoon!',
        'Hi.'

        ]).
reply(who_are_you, [
        'My name is Advia, nice to meet you.',
        'I m Advia!',
        'My name isnt important right now.',
        'advia, at your service, how may I help?'
        ]).
        

% give_reply(X, Y):-
% reply(hello, L),
% reply(bye, L),
% random_member(Y,L).
% 

give_reply(X, Y):-
reply(X, L),
random_member(Y,L).

