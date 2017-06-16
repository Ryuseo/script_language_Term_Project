#include "python.h"

static PyObject * 

pack(PyObject *self, PyObject *args)
{
	int num = NULL;
	int result = 1;

	if (!PyArg_ParseTuple(args, "i", &num)) // �Ű����� ���� �м��ϰ� ���������� �Ҵ� ��ŵ�ϴ�.
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

	if (!PyArg_ParseTuple(args, "i", &num)) // �Ű����� ���� �м��ϰ� ���������� �Ҵ� ��ŵ�ϴ�.
		return NULL;


	return Py_BuildValue("i", num * num);
}

static PyMethodDef SpamMethods[] = 
{
	{ "pack", pack, METH_VARARGS,"count a string length." },
	{ "square", square, METH_VARARGS,"count a string length." },
	{NULL, NULL, 0, NULL} // �迭�� ���� ��Ÿ���ϴ�.
}; 

static struct PyModuleDef spammodule = 
{
    PyModuleDef_HEAD_INIT,
    "spam",            // ��� �̸�
    "It is test module.", // ��� ������ ���� �κ�, ����� __doc__�� ����˴ϴ�.
    -1,SpamMethods
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModule_Create(&spammodule);
}
