# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


"""
Python interface to KrisLibrary nonlinear, multidimensional root finding routines
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_rootfind', [dirname(__file__)])
        except ImportError:
            import _rootfind
            return _rootfind
        if fp is not None:
            try:
                _mod = imp.load_module('_rootfind', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _rootfind = swig_import_helper()
    del swig_import_helper
else:
    import _rootfind
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def setFTolerance(*args):
  """
    setFTolerance(double tolf)

    void setFTolerance(double tolf)

    Sets the termination threshold for the change in f. 
    """
  return _rootfind.setFTolerance(*args)

def setXTolerance(*args):
  """
    setXTolerance(double tolx)

    void setXTolerance(double tolx)

    Sets the termination threshold for the change in x. 
    """
  return _rootfind.setXTolerance(*args)

def setVectorField(*args):
  """
    setVectorField(PyObject * pVFObj) -> int

    int setVectorField(PyObject
    *pVFObj)

    Sets the vector field object, returns 0 if pVFObj = NULL, 1 otherwise.

    """
  return _rootfind.setVectorField(*args)

def findRoots(*args):
  """
    findRoots(PyObject * startVals, int iter) -> PyObject *

    PyObject* findRoots(PyObject
    *startVals, int iter)

    Performs unconstrained root finding for up to iter iterations Return
    values is a tuple indicating (0,x,n) : convergence reached in x
    (1,x,n) : convergence reached in f (2,x,n) : divergence (3,x,n) :
    degeneration of gradient (local extremum or saddle point) (4,x,n) :
    maximum iterations reached (5,x,n) : numerical error occurred where x
    is the final point and n is the number of iterations used 
    """
  return _rootfind.findRoots(*args)

def findRootsBounded(*args):
  """
    findRootsBounded(PyObject * startVals, PyObject * boundVals, int iter) -> PyObject *

    PyObject*
    findRootsBounded(PyObject *startVals, PyObject *boundVals, int iter)

    Same as findRoots, but with given bounds (xmin,xmax) 
    """
  return _rootfind.findRootsBounded(*args)

def destroy():
  """
    destroy()

    void destroy()

    destroys internal data structures 
    """
  return _rootfind.destroy()
# This file is compatible with both classic and new-style classes.


