from typing import Literal, Mapping

type Version_type = Literal["0.1.0"]
type Sound_type = Literal[
        "b","ch","d","ds","f","g",
        "h","k","l","m","n",
        "p","r","s","sh","t","th","ts",
        "v","w",
        "A_ei","an","ar_short","ar",
        "E_ee","e","er",
        "I_ai","i",
        "O_ou","o","or_",
        "U_iu","oo_short","oo",
        ]
SPELLING_TABLE_0_1_0:Mapping[Sound_type,str] = {
        "b":"b", "ch":"ch", "d":"d", "ds":"ds", "f":"f", "g":"g",
        "h":"h", "k":"k", "l":"l", "m":"m", "n":"n",
        "p":"p", "r":"r", "s":"s", "sh":"sh", "t":"t", "th":"th", "ts":"ts",
        "v":"v", "w":"w",
        "A_ei":"ei", "an":"a", "ar_short":"aa", "ar":"ar",
        "E_ee":"ii", "e":"e", "er":"er",
        "I_ai":"ai", "i":"i",
        "O_ou":"ou", "o":"o", "or_":"oer",
        "U_iu":"iu", "oo_short":"u", "oo":"uu",
}
def get_spelling_table(version:Version_type)->Mapping[Sound_type,str]:
    match version:
        case "0.1.0":
            return SPELLING_TABLE_0_1_0
        case _:
            assert False, "bad param:version"
            pass
    pass#end of function.
if "some meta programming" and True:
    def ____some_meta_programming():
        for key in get_spelling_table("0.1.0").keys():
            print(f'''        def {key}(self):
            self.add_sound("{key}")
            return self''')
        return
    ____some_meta_programming()
    pass



class NewSpelling:
    data:list[Sound_type]
    version:Version_type
    def __init__(self):
        self.data = []
        self.version = "0.1.0"
        pass
    def __add_sound(self, new_sound:Sound_type):
        self.data.append(new_sound)
        pass
    def __str__(self, end = " ")->str:
        spelling_table = get_spelling_table(self.version)
        
        result = ""
        for sound in self.data:
            result += spelling_table[sound]
            pass
        
        result += end
        return result

    if "to fold":
        def b(self):
            self.add_sound("b")
            return self
        def ch(self):
            self.add_sound("ch")
            return self
        def d(self):
            self.add_sound("d")
            return self
        def ds(self):
            self.add_sound("ds")
            return self
        def f(self):
            self.add_sound("f")
            return self
        def g(self):
            self.add_sound("g")
            return self
        def h(self):
            self.add_sound("h")
            return self
        def k(self):
            self.add_sound("k")
            return self
        def l(self):
            self.add_sound("l")
            return self
        def m(self):
            self.add_sound("m")
            return self
        def n(self):
            self.add_sound("n")
            return self
        def p(self):
            self.add_sound("p")
            return self
        def r(self):
            self.add_sound("r")
            return self
        def s(self):
            self.add_sound("s")
            return self
        def sh(self):
            self.add_sound("sh")
            return self
        def t(self):
            self.add_sound("t")
            return self
        def th(self):
            self.add_sound("th")
            return self
        def ts(self):
            self.add_sound("ts")
            return self
        def v(self):
            self.add_sound("v")
            return self
        def w(self):
            self.add_sound("w")
            return self
        def A_ei(self):
            self.add_sound("A_ei")
            return self
        def an(self):
            self.add_sound("an")
            return self
        def ar_short(self):
            self.add_sound("ar_short")
            return self
        def ar(self):
            self.add_sound("ar")
            return self
        def E_ee(self):
            self.add_sound("E_ee")
            return self
        def e(self):
            self.add_sound("e")
            return self
        def er(self):
            self.add_sound("er")
            return self
        def I_ai(self):
            self.add_sound("I_ai")
            return self
        def i(self):
            self.add_sound("i")
            return self
        def O_ou(self):
            self.add_sound("O_ou")
            return self
        def o(self):
            self.add_sound("o")
            return self
        def or_(self):
            self.add_sound("or_")
            return self
        def U_iu(self):
            self.add_sound("U_iu")
            return self
        def oo_short(self):
            self.add_sound("oo_short")
            return self
        def oo(self):
            self.add_sound("oo")
            return self
        pass#/ "to fold"
    
    pass#end of class.

if "hello world" and True:
    def ____test____NewSpelling():
        the_hello = NewSpelling().h().ar_short().l().O_ou()
        the_world = NewSpelling().w().or_().O_ou().d()
        result_str = f"{the_hello}{the_world.__str__(end="")}"
        assert result_str == "haalou woeroud"
        #print(result_str)
        
        return 
    ____test____NewSpelling()
