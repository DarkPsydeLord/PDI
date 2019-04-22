# Main class while testing, will change after GUI implementation

import Transformations.color as tc
import Tools.readfile as f
import Tools.showimg as s
import Tools.keepimgalive as w
import Transformations.Filters as tf

filename = f.openfile()
s.show(filename, name="Original")
# gray = tc.graytransform(filename)
# s.show(gray, name="Gris")
# binary = tc.binarytransform(filename)
# s.show(binary, name="Binary")
# invbinary = tc.invbinarytransform(filename)
# s.show(invbinary, name="Inverted Binary")
#adpbinary = tc.adpbinarytransform(filename)
#s.show(adpbinary, name="Adaptative Binary")
gauss = tf.gaussian(filename, 9, 9, 3, 3)
s.show(gauss, name="Gaussian Filter")
w.wait()

