from inspect import signature

def factorial(n):
    """return n
    """
    return n if n<2 else n*factorial(n-1)


fruits = ['apple','cherry','fig','berry']

wiki="""
A wiki is run using wiki software, otherwise known as a wiki engine. 
A wiki engine is a type of content management system, but it differs 
from most other such systems, including blog software, in that the content
is created without any defined owner or leader, and wikis have little
inherent structure, allowing structure to emerge according to the 
needs of the users.[2] There are dozens of different wiki engines 
in use, both standalone and part of other software, such as bug 
tracking systems. Some wiki engines are open source, whereas others 
are proprietary. Some permit control over different functions 
(levels of access); for example, editing rights may permit changing,
adding, or removing material. Others may permit access without
enforcing access control. Other rules may be imposed to organize 
content."""


def clip(text, prompt, max_len=80):
    """
    在max_len前面或者后面的第一个prompt处截断文
    """

    end = None
    if len(text) > max_len:
        space_before = text.rfind(prompt, 0, max_len)

        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(prompt, max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # 没有找到prompt
        end = len(text)
    return text[:end].strip()


sig = signature(clip)
for name,param in sig.parameters.items():
    print(param.kind,':',name,'=',param.default)
