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
drawbridge_raised = True
if not drawbridge_raised:
    outcome = "Thunder: The bridge is down"
else:
    outcome = "Doom: Oh no its block!!!ed"
    print(outcome)