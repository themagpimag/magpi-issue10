# A class to calculate the value of a function string
class FunctionCalculator:
  def evaluate(self, cmd):
    y = 0.
    print "exec \"%s\"" % cmd
    exec cmd
    print "y = %e" % y
    return y

# A class to calculate many the result of many equations at once. 
class SynchronousCalculator:
  def __init__(self):
    self.calculator =  FunctionCalculator()

  def evaluate(self, cmds):
    results=[]
    for cmd in cmds:
      results.append(self.calculator.evaluate(cmd))
    return results
