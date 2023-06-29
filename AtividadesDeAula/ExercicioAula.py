def teste_args_kwargs(arg1, arg2, arg3):
    print("Arg1 = ", arg1)
    print("Arg2 = ", arg2)
    print("Arg2 = ", arg3)

lista = [1, 2, 3]
teste_args_kwargs(*lista)
#teste_args_kwargs(1,2,3)