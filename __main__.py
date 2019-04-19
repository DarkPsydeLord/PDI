# Main class while testing, will change after GUI implementation

import Transformations.color as tc
import Tools.readfile as f
import Tools.showimg as s
import Tools.keepimgalive as w

filename = f.openfile()
s.show(filename, name="Original")
gris = tc.graytransform(filename)
s.show(gris, name="Gris")
w.wait()

