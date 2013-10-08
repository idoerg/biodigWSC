def APIS(fn, path, description):
        fn.__description = description
        fn.__path = path
        return fn

def Operations(fn, method, nickname, typeOfOperation, parameters[],summary, notes, responseMessage[]):
               fn.__method = method
               fn.__nickname = nickname
               fn.__typeOfOperation = operation
               fn.__parameters[] = parameters[]
               fn.summary = summary
               fn.notes = notes
               fn.response = response
               return fn

def Param (fn, paramType, name, description, typeOfParam, formatOfParam, required, minimum, maximum):
                fn.__paramType = ParamType
                fn.__name = name
                fn.__description = description
                fn.__typeOfParam = typeOfParam
                fn.__formatOfParam= formatOfParam
                fn.__required = required
                fn.__minimum = minimum
                fn.__maximum = maximum
                return fn




