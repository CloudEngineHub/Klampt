# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

"""Python interface to C++ nonlinear, multidimensional root finding routines"""

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _rootfind
else:
    import _rootfind

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

from typing import Sequence,Tuple,Iterator
from klampt.model.typing import IntArray,Config,Vector,Vector3,Matrix3,Point,Rotation,RigidTransform


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)



def setFTolerance(tolf: float) ->None:
    r"""
    Sets the termination threshold for the change in f.  

    Args:
        tolf (float)
    """
    return _rootfind.setFTolerance(tolf)

def setXTolerance(tolx: float) ->None:
    r"""
    Sets the termination threshold for the change in x.  

    Args:
        tolx (float)
    """
    return _rootfind.setXTolerance(tolx)

def setVectorField(pVFObj: object) ->int:
    r"""
    Sets the vector field object.  

    Args:
        pVFObj (:obj:`object`)

    Returns:  

        status (int): 0 if pVFObj = NULL, 1 otherwise.
     See vectorfield.py for an abstract base class that can be overridden to produce
    one of these objects.  

    """
    return _rootfind.setVectorField(pVFObj)

def findRoots(startVals: object, iter: int) ->object:
    r"""
    Performs unconstrained root finding for up to iter iterations  

    Args:
        startVals (:obj:`object`)
        iter (int)

    Returns:  

        status,x,n (tuple of int, list of floats, int): where status indicates
            the return code, as follows:

                - 0: convergence reached in x
                - 1: convergence reached in f
                - 2: divergence
                - 3: degeneration of gradient (local extremum or saddle point)
                - 4: maximum iterations reached
                - 5: numerical error occurred

            and x is the final point and n is the number of iterations used


    """
    return _rootfind.findRoots(startVals, iter)

def findRootsBounded(startVals: object, boundVals: object, iter: int) ->object:
    r"""
    Same as findRoots, but with given bounds (xmin,xmax)  

    Args:
        startVals (:obj:`object`)
        boundVals (:obj:`object`)
        iter (int)
    """
    return _rootfind.findRootsBounded(startVals, boundVals, iter)

def destroy() ->None:
    r"""
    destroys internal data structures  

    """
    return _rootfind.destroy()


