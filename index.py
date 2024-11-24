file ="./asm.asm"

#diccionario donde se guarda la linea donde se encuentra la etiqueta
LABELS = {}

#lista con los registros
REG_CODES = ["arg","brg","crg","drg","erg","frg","grg","hrg","irg","jrg" ]

#aqui se guardan la ultima linea donde se uso el registro
DIR_REG = {"arg":-1,"brg":-1,"crg":-1,"drg":-1,"erg":-1,"frg":-1,"grg":-1,
           "hrg":-1,"irg":-1,"jrg":-1}

#operaciones de salto de linea con la conversion a binario
JM_CODES = {
    "jmp": "10001",
    "je": "10010",
    "jne": "10011",
    "ja": "10100",
    "jae": "10101",
    "jb": "10110",
    "jbe": "10111",
}

#aqui se tienen la lista con las operaciones en orden
OPC_CODES = [
    "add",
    "sub",
    "mul",
    "div",
    "cmp",
    "and",
    "or",
    "not",
    "xor",
    "shl",
    "shr",
    "rol",
    "ror",
    "test",
    "read",
    "write",
    "move",
]