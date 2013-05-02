AC_INIT(., 0.1)
m4_include([m4/ax_python_module.m4])

AC_CHECK_PROG(have_python, python, yes, [no])
if test x$have_python != xyes
then
	AC_MSG_ERROR([Python not installed])
fi

AX_PYTHON_MODULE(numpy, [fatal])
AX_PYTHON_MODULE(pandas, [fatal])
AX_PYTHON_MODULE(tornado)
AX_PYTHON_MODULE(zmq)

if test x$HAVE_PYMOD_zmq != xyes
then
	AC_MSG_NOTICE([Python zmq module is not installed, you will not be able to run ipython notebook])
fi
if test x$HAVE_PYMOD_tornado != xyes
then
	AC_MSG_NOTICE([Python tornado module is not installed, you will not be able to run ipython notebook])
fi

AC_CHECK_PROG(have_git, git, yes)
if test x$have_git != xyes
then
	AC_MSG_ERROR([Git is not installed])
fi

AC_CHECK_PROG(have_ipython, ipython, yes)
if test x$have_ipython != xyes
then
	AC_MSG_ERROR([IPython is not installed])
fi

AC_MSG_RESULT([All setup check passed, you are good to go!])
