AC_INIT(., 0.1)
m4_include([m4/ax_python.m4])
m4_include([m4/ax_python_module.m4])

AC_CHECK_PROG(have_python, python, ok, [no])
if test x$have_python != xok
then
	AC_MSG_ERROR([Python not installed])
fi

AX_PYTHON_MODULE(numpy, [fatal])
AX_PYTHON_MODULE(pandas, [fatal])

AC_CHECK_PROG(have_git, git, ok)
if test x$have_git != xok
then
	AC_MSG_ERROR([Git is not installed])
fi

AC_CHECK_PROG(have_ipython, ipython, ok)
if test x$have_ipython != xok
then
	AC_MSG_ERROR([IPython is not installed])
fi

AC_MSG_RESULT([All setup check passed, you are good to go!])
