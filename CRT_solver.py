## Generic Chinere Remainder Theorem solver


def solveCRT(congruents, moduli):
  """
  x = congruents[0] % moduli[0]
  x = congruents[1] % moduli[1]
               ...
  x = congruents[n] % moduli[n]

  Output: a such that x = a % (moduli[0] * moduli[1] * ... * moduli[n])
  
  moduli are deemed already coprimes
  """
  M = 1  # total modulo
  facts = []  # inverse factors
  a = 0  # particular solution not reduced mod M
  
  for i in range(len(moduli)):
    curmod = moduli[i]
    mInv = 1
    
    for m in moduli:
      if m == curmod:
        M *= curmod
      else:
        mInv *= m

    k = 1
    while (k * mInv) % curmod != 1:
      k+=1

    facts.append(k * mInv)
    
  for i in range(len(congruents)):
    a += facts[i] * congruents[i]

  return a % M
