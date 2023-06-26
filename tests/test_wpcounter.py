from wpcounter import WPCounter


def test_canmatch():
  result = 'PAYER' in WPCounter('P.Y.R')
  assert result

def test_sustitutes():
  result = WPCounter('REAL..ING').substitutes('TRING')
  assert result == [0]
  result = WPCounter('REAL..ING').substitutes('HELP')
  assert result == [0,3]
  result = WPCounter('REAL..ING').substitutes('LEAVE')
  assert result == [3,4]
  result = WPCounter('REAL..ING').substitutes('ZIONIST')
  assert result is None
