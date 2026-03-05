good = r'''
 '\__
  (o )     ___
  <>(_)(_)(___)
    < < > >
    ' ' ` `
pb'''
print(good)
bad = r'''
 \       /
  \     /  
   \.-./ 
  (o\^/o)  _   _   _     __
   ./ \.\ ( )-( )-( ) .-'  '-.
    {-} \(//  ||   \\/ (   )) '-.
         //-__||__.-\\.       .-'
        (/    ()     \)'-._.-'
        ||    ||      \\
MJP     ('    ('       ')
'''
torch_lit = True
if torch_lit:
    outcome = "Flicker:Yay!Light!"
else:
    outcome = "Doom: Who turn off the lights!"
    print(outcome)