#include "python.h"

static PyObject * 

pack(PyObject *self, PyObject *args)
{
	int num = NULL;
	int result = 1;

	if (!PyArg_ParseTuple(args, "i", &num)) // 매개변수 값을 분석하고 지역변수에 할당 시킵니다.
		return NULL;


	for (int i = num; i > 0; --i)
	{
		result = result * i;
	}

	return Py_BuildValue("i", result);
}

square(PyObject *self, PyObject *args)
{
	int num = NULL;

	if (!PyArg_ParseTuple(args, "i", &num)) // 매개변수 값을 분석하고 지역변수에 할당 시킵니다.
		return NULL;


	return Py_BuildValue("i", num * num);
}

static PyMethodDef SpamMethods[] = 
{
	{ "pack", pack, METH_VARARGS,"count a string length." },
	{ "square", square, METH_VARARGS,"count a string length." },
	{NULL, NULL, 0, NULL} // 배열의 끝을 나타냅니다.
}; 

static struct PyModuleDef spammodule = 
{
    PyModuleDef_HEAD_INIT,
    "spam",            // 모듈 이름
    "It is test module.", // 모듈 설명을 적는 부분, 모듈의 __doc__에 저장됩니다.
    -1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}
