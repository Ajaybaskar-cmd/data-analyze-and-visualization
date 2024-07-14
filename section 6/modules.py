import pkg_resources as pk
pack=pk.working_set

list=sorted("%s==%s"%(i.key,i.version) for i in pack)
print(list)