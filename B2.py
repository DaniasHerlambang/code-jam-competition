
def checkParagraf(paragraf, checker='o'):
  last_index    = paragraf[-1]
  get_paragraf  = paragraf.split('\n\n')
  penentu_index = ''
  for index in range(len(get_paragraf)):
    if get_paragraf[index][32].lower() == checker:
      penentu_index = "= Berada di paragraf `{}`".format(index)
    else:
      penentu_index = penentu_index
      
  def info(bol, last, index):
    return "{}, index terakhir berkarakter `{}` \nDan index32=`{}` {}\n----".format(bol, last, checker, index)
  
  if last_index == checker:
    return info("Benar", last_index, penentu_index)
  return info("Salah", last_index, penentu_index)


paragraf = """Lorem ipsum dolor sit amet, consoctetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

print checkParagraf(paragraf)



paragraf = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborumo"""

print checkParagraf(paragraf)
