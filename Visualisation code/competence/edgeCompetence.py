from CompetenceGraphe import net, get_module_id, get_skill_id

# IDU skill
id_IDU_1_1 = get_skill_id("IDU-1.1")
id_IDU_1_2 = get_skill_id("IDU-1.2")
id_IDU_1_3 = get_skill_id("IDU-1.3")
id_IDU_2_1 = get_skill_id("IDU-2.1")
id_IDU_2_2 = get_skill_id("IDU-2.2")
id_IDU_2_3 = get_skill_id("IDU-2.3")
id_IDU_3_1 = get_skill_id("IDU-3.1")
id_IDU_3_2 = get_skill_id("IDU-3.2")
id_IDU_4_1 = get_skill_id("IDU-4.1")
id_IDU_4_2 = get_skill_id("IDU-4.2")
# TC skill
id_TC_1_1 = get_skill_id("TC-1.1")
id_TC_1_2 = get_skill_id("TC-1.2")
id_TC_1_3 = get_skill_id("TC-1.3")
id_TC_1_4 = get_skill_id("TC-1.4")
id_TC_1_5 = get_skill_id("TC-1.5")
id_TC_2_1 = get_skill_id("TC-2.1")
id_TC_2_2 = get_skill_id("TC-2.2")
id_TC_2_3 = get_skill_id("TC-2.3")
id_TC_3_1 = get_skill_id("TC-3.1")
id_TC_3_2 = get_skill_id("TC-3.2")
id_TC_3_3 = get_skill_id("TC-3.3")
id_TC_3_4 = get_skill_id("TC-3.4")
id_TC_4_1 = get_skill_id("TC-4.1")
id_TC_4_2 = get_skill_id("TC-4.2")
id_TC_4_3 = get_skill_id("TC-4.3")
id_TC_4_4 = get_skill_id("TC-4.4")

id_LANG501a = get_module_id("LANG501a")
net.add_edge(id_LANG501a, id_TC_2_1, weight=1)
net.add_edge(id_LANG501a, id_TC_2_3, weight=1)
net.add_edge(id_LANG501a, id_TC_3_3, weight=1)

id_SHES501a = get_module_id("SHES501a")
net.add_edge(id_SHES501a, id_TC_1_1, weight=1)
net.add_edge(id_SHES501a, id_TC_1_2, weight=1)
net.add_edge(id_SHES501a, id_TC_1_5, weight=1)
net.add_edge(id_SHES501a, id_TC_2_1, weight=1)
net.add_edge(id_SHES501a, id_TC_2_3, weight=1)

id_SHES505 = get_module_id("SHES505")
net.add_edge(id_SHES505, id_TC_1_1, weight=1)
net.add_edge(id_SHES505, id_TC_1_2, weight=1)
net.add_edge(id_SHES505, id_TC_1_4, weight=1)
net.add_edge(id_SHES505, id_TC_2_1, weight=1)
net.add_edge(id_SHES505, id_TC_4_1, weight=1)
net.add_edge(id_SHES505, id_TC_4_3, weight=1)
net.add_edge(id_SHES505, id_TC_2_3, weight=1)
net.add_edge(id_SHES505, id_TC_3_1, weight=1)
net.add_edge(id_SHES505, id_TC_3_3, weight=1)


id_DDRS501 = get_module_id("DDRS501")
net.add_edge(id_DDRS501, id_IDU_3_2, weight=1)
net.add_edge(id_DDRS501, id_TC_1_1, weight=1)
net.add_edge(id_DDRS501, id_TC_3_1, weight=1)
net.add_edge(id_DDRS501, id_TC_3_2, weight=1)
net.add_edge(id_DDRS501, id_TC_3_3, weight=1)
net.add_edge(id_DDRS501, id_TC_3_4, weight=1)

net.add_edge(get_module_id("EASI501a"), id_IDU_3_2, weight=1)


id_INFO501a = get_module_id("INFO501a")
net.add_edge(id_INFO501a, id_IDU_1_1, weight=1)
net.add_edge(id_INFO501a, id_IDU_1_2, weight=1)
net.add_edge(id_INFO501a, id_TC_1_3, weight=1)


id_INFO502a = get_module_id("INFO502a")
net.add_edge(id_INFO502a, id_IDU_1_1, weight=1)
net.add_edge(id_INFO502a, id_IDU_2_2, weight=1)
net.add_edge(id_INFO502a, id_IDU_2_3, weight=1)


id_MATH500a = get_module_id("MATH500a")
net.add_edge(id_MATH500a, id_IDU_2_3, weight=1)
net.add_edge(id_MATH500a, id_TC_1_3, weight=1)


id_MATH501a = get_module_id("MATH501a")
net.add_edge(id_MATH501a, id_IDU_2_3, weight=1)
net.add_edge(id_MATH501a, id_TC_1_3, weight=1)


id_EASI541b = get_module_id("EASI541b")
net.add_edge(id_EASI541b, id_IDU_1_1, weight=1)
net.add_edge(id_EASI541b, id_IDU_4_1, weight=1)


id_ISOC531 = get_module_id("ISOC531")
net.add_edge(id_ISOC531, id_IDU_3_1, weight=1)
net.add_edge(id_ISOC531, id_TC_1_4, weight=1)
net.add_edge(id_ISOC531, id_TC_1_5, weight=1)
net.add_edge(id_ISOC531, id_TC_2_2, weight=1)
net.add_edge(id_ISOC531, id_TC_2_2, weight=1)


id_MATH531 = get_module_id("MATH531")
net.add_edge(id_MATH531, id_IDU_1_1, weight=1)
net.add_edge(id_MATH531, id_IDU_1_2, weight=1)


id_PROJ531 = get_module_id("PROJ531")
net.add_edge(id_PROJ531, id_IDU_1_1, weight=1)
net.add_edge(id_PROJ531, id_TC_1_4, weight=1)
net.add_edge(id_PROJ531, id_TC_3_2, weight=1)
net.add_edge(id_PROJ531, id_TC_1_1, weight=1)
net.add_edge(id_PROJ531, id_TC_2_1, weight=1)
net.add_edge(id_PROJ531, id_TC_2_2, weight=1)
net.add_edge(id_PROJ531, id_IDU_2_3, weight=1)
net.add_edge(id_PROJ531, id_IDU_4_1, weight=1)


#Semestre 9
id_LANG901a = get_module_id("LANG901a")
net.add_edge(id_LANG901a,id_TC_2_1, weight=1)
net.add_edge(id_LANG901a,id_TC_2_3, weight=1)
net.add_edge(id_LANG901a,id_TC_3_3, weight=1)

id_LANG902a = get_module_id("LANG902a")
net.add_edge(id_LANG902a,id_TC_2_1, weight=1)
net.add_edge(id_LANG902a,id_TC_2_3, weight=1)
net.add_edge(id_LANG902a,id_TC_3_3, weight=1)

id_PROJ901a = get_module_id("LANG901a")
net.add_edge(id_PROJ901a,id_TC_1_3, weight=1)
net.add_edge(id_PROJ901a,id_TC_2_1, weight=1)
net.add_edge(id_PROJ901a,id_TC_2_3, weight=1)
net.add_edge(id_PROJ901a,id_TC_4_1, weight=1)
net.add_edge(id_PROJ901a,id_TC_4_2, weight=1)
net.add_edge(id_PROJ901a,id_TC_4_3, weight=1)
net.add_edge(id_PROJ901a,id_TC_1_1, weight=1)
net.add_edge(id_PROJ901a,id_TC_1_2, weight=1)
net.add_edge(id_PROJ901a,id_TC_1_5, weight=1)
net.add_edge(id_PROJ901a,id_TC_4_4, weight=1)

id_SHES901a = get_module_id("LANG901a")
net.add_edge(id_SHES901a,id_TC_2_2, weight=1)
net.add_edge(id_SHES901a,id_TC_2_3, weight=1)
net.add_edge(id_SHES901a,id_TC_3_4, weight=1)
net.add_edge(id_SHES901a,id_TC_1_1, weight=1)
net.add_edge(id_SHES901a,id_TC_1_5, weight=1)

id_INFO931 = get_module_id("INFO931")
net.add_edge(id_INFO931,id_IDU_2_2, weight=1)
net.add_edge(id_INFO931,id_IDU_4_1, weight=1)
net.add_edge(id_INFO931,id_TC_1_2, weight=1)
net.add_edge(id_INFO931,id_TC_1_4, weight=1)
net.add_edge(id_INFO931,id_IDU_3_1, weight=1)
net.add_edge(id_INFO931,id_IDU_3_2, weight=1)

id_INFO932 = get_module_id("INFO932")
net.add_edge(id_INFO932,id_IDU_1_1, weight=1)
net.add_edge(id_INFO932,id_IDU_1_2, weight=1)
net.add_edge(id_INFO932,id_IDU_1_3, weight=1)
net.add_edge(id_INFO932,id_IDU_4_1, weight=1)

id_PROJ931 = get_module_id("PROJ931")
net.add_edge(id_PROJ931 ,id_IDU_1_1, weight=1)
net.add_edge(id_PROJ931 ,id_IDU_2_3, weight=1)
net.add_edge(id_PROJ931 ,id_IDU_3_1, weight=1)

id_DATA931 = get_module_id("DATA931")
net.add_edge(id_DATA931 ,id_IDU_1_3, weight=1)
net.add_edge(id_DATA931 ,id_IDU_2_1, weight=1)
net.add_edge(id_DATA931 ,id_IDU_2_3, weight=1)
net.add_edge(id_DATA931 ,id_IDU_3_1, weight=1)
net.add_edge(id_DATA931 ,id_IDU_4_1, weight=1)
net.add_edge(id_DATA931,id_TC_2_3, weight=1)

id_ISOC931 = get_module_id("ISOC931")
net.add_edge(id_ISOC931,id_TC_1_2, weight=1)
net.add_edge(id_ISOC931,id_TC_2_1, weight=1)
net.add_edge(id_ISOC931,id_TC_3_3, weight=1)
net.add_edge(id_ISOC931,id_TC_4_1, weight=1)

id_PROJ932 = get_module_id("PROJ932")
net.add_edge(id_PROJ932,id_IDU_1_1, weight=1)
net.add_edge(id_PROJ932,id_IDU_1_2, weight=1)
net.add_edge(id_PROJ932,id_IDU_1_3, weight=1)
net.add_edge(id_PROJ932,id_IDU_2_1, weight=1)
net.add_edge(id_PROJ932,id_IDU_4_1, weight=1)

#Semestre 10
id_PROJ001  = get_module_id("PROJ001")
net.add_edge(id_PROJ001,id_TC_3_1, weight=1)
net.add_edge(id_PROJ001,id_TC_3_2, weight=1)
net.add_edge(id_PROJ001,id_TC_3_3, weight=1)
net.add_edge(id_PROJ001,id_TC_3_4, weight=1)
net.add_edge(id_PROJ001,id_TC_1_1, weight=1)
net.add_edge(id_PROJ001,id_TC_1_2, weight=1)
net.add_edge(id_PROJ001,id_TC_1_3, weight=1)
net.add_edge(id_PROJ001,id_TC_1_4, weight=1)
net.add_edge(id_PROJ001,id_TC_1_5, weight=1)
net.add_edge(id_PROJ001,id_TC_2_1, weight=1)
net.add_edge(id_PROJ001,id_TC_2_2, weight=1)
net.add_edge(id_PROJ001,id_TC_2_3, weight=1)
net.add_edge(id_PROJ001,id_TC_4_3, weight=1)
net.add_edge(id_PROJ001,id_TC_4_4, weight=1)

# semestre 6

# id_LANG601 = get_module_id("LANG601a")
# print(id_LANG601)

# net.add_edge(id_LANG601, id_TC_2_1, weight=1)
# net.add_edge(id_LANG601, id_TC_2_3, weight=1)
# net.add_edge(id_LANG601, id_TC_3_3, weight=1)

id_PROJ601a  = get_module_id("PROJ601a")
net.add_edge(id_PROJ601a, id_TC_2_1, weight=1)
net.add_edge(id_PROJ601a, id_TC_2_2, weight=1)
net.add_edge(id_PROJ601a, id_TC_2_3, weight=1)
net.add_edge(id_PROJ601a, id_TC_3_3, weight=1)

id_SHES601a  = get_module_id("SHES601a")
net.add_edge(id_SHES601a, id_TC_3_2, weight=1)

id_SHES602a  = get_module_id("SHES602a")
net.add_edge(id_SHES602a, id_TC_3_2, weight=1)

id_INFO631a  = get_module_id("INFO631a")
net.add_edge(id_INFO631a, id_IDU_1_1, weight=1)
net.add_edge(id_INFO631a, id_IDU_1_2, weight=1)

id_MATH641c = get_module_id("MATH641c")
net.add_edge(id_MATH641c, id_IDU_2_1, weight=1)
net.add_edge(id_MATH641c, id_IDU_2_3, weight=1)

id_PROJ631a  = get_module_id("PROJ631a")
net.add_edge(id_PROJ631a, id_IDU_2_1, weight=1)
net.add_edge(id_PROJ631a, id_IDU_2_1, weight=1)
net.add_edge(id_PROJ631a, id_IDU_4_1, weight=1)
net.add_edge(id_PROJ631a, id_TC_4_1, weight=1)
net.add_edge(id_PROJ631a, id_TC_4_2, weight=1)

id_INFO632  = get_module_id("INFO632")
net.add_edge(id_INFO632, id_IDU_1_1, weight=1)
net.add_edge(id_INFO632, id_IDU_4_1, weight=1)

id_INFO641c  = get_module_id("PROJ001")
net.add_edge(id_INFO641c, id_IDU_1_1, weight=1)
net.add_edge(id_INFO641c, id_IDU_4_1, weight=1)

id_INFO642c  = get_module_id("INFO642c")
net.add_edge(id_INFO642c, id_IDU_1_1, weight=1)
net.add_edge(id_INFO642c, id_IDU_4_1, weight=1)
net.add_edge(id_INFO642c, id_IDU_2_3, weight=1)
net.add_edge(id_INFO642c, id_IDU_2_2, weight=1)

id_ISOC631  = get_module_id("ISOC631")
net.add_edge(id_ISOC631, id_IDU_2_3, weight=1)
net.add_edge(id_ISOC631, id_IDU_2_1, weight=1)
net.add_edge(id_ISOC631, id_IDU_4_1, weight=1)
net.add_edge(id_ISOC631, id_TC_1_4, weight=1)

id_PROJ632 = get_module_id("PROJ632")
net.add_edge(id_PROJ632, id_IDU_1_1, weight=1)
net.add_edge(id_PROJ632, id_IDU_2_1, weight=1)

id_INFO632a  = get_module_id("INFO632a")
net.add_edge(id_INFO632a, id_IDU_1_1, weight=1)
net.add_edge(id_INFO632a, id_IDU_4_1, weight=1)

id_ISOC631a  = get_module_id("ISOC631a")
net.add_edge(id_ISOC631a, id_IDU_2_1, weight=1)
net.add_edge(id_ISOC631a, id_IDU_2_3, weight=1)
net.add_edge(id_ISOC631a, id_TC_1_1, weight=1)

id_PROJ632a = get_module_id("PROJ632a")
net.add_edge(id_PROJ632a, id_IDU_1_1, weight=1)
net.add_edge(id_PROJ632a, id_IDU_2_1, weight=1)

# semestre 8

id_LANG801a  = get_module_id("LANG801a")
net.add_edge(id_LANG801a, id_TC_2_1, weight=1)
net.add_edge(id_LANG801a, id_TC_2_3, weight=1)
net.add_edge(id_LANG801a, id_TC_3_3, weight=1)

id_LANG802a  = get_module_id("LANG802a")
net.add_edge(id_LANG802a, id_TC_2_1, weight=1)
net.add_edge(id_LANG802a, id_TC_2_3, weight=1)
net.add_edge(id_LANG802a, id_TC_3_3, weight=1)

id_SHES802a = get_module_id("SHES802a")
net.add_edge(id_SHES802a, id_TC_1_1, weight=1)
net.add_edge(id_SHES802a, id_TC_2_3, weight=1)
net.add_edge(id_SHES802a, id_TC_3_1, weight=1)
net.add_edge(id_SHES802a, id_TC_3_2, weight=1)

id_SHES803a  = get_module_id("SHES803a")
net.add_edge(id_SHES803a, id_TC_3_2, weight=1)

id_PROJ801  = get_module_id("PROJ801")
net.add_edge(id_PROJ801, id_TC_1_1, weight=1)
net.add_edge(id_PROJ801, id_TC_1_2, weight=1)
net.add_edge(id_PROJ801, id_TC_1_3, weight=1)
net.add_edge(id_PROJ801, id_TC_1_4, weight=1)
net.add_edge(id_PROJ801, id_TC_1_5, weight=1)
net.add_edge(id_PROJ801, id_TC_2_1, weight=1)
net.add_edge(id_PROJ801, id_TC_2_2, weight=1)
net.add_edge(id_PROJ801, id_TC_2_3, weight=1)
net.add_edge(id_PROJ801, id_TC_3_1, weight=1)
net.add_edge(id_PROJ801, id_TC_3_2, weight=1)
net.add_edge(id_PROJ801, id_TC_3_3, weight=1)
net.add_edge(id_PROJ801, id_TC_3_4, weight=1)
net.add_edge(id_PROJ801, id_TC_4_1, weight=1)
net.add_edge(id_PROJ801, id_TC_4_2, weight=1)
net.add_edge(id_PROJ801, id_TC_4_3, weight=1)
net.add_edge(id_PROJ801, id_TC_4_4, weight=1)

id_DATA831a  = get_module_id("DATA831a")
net.add_edge(id_DATA831a, id_IDU_1_1, weight=1)
net.add_edge(id_DATA831a, id_IDU_1_3, weight=1)

id_DATA832a  = get_module_id("DATA832a")
net.add_edge(id_DATA832a, id_IDU_1_3, weight=1)
net.add_edge(id_DATA832a, id_IDU_2_1, weight=1)
net.add_edge(id_DATA832a, id_IDU_2_2, weight=1)
net.add_edge(id_DATA832a, id_IDU_2_3, weight=1)
net.add_edge(id_DATA832a, id_TC_1_2, weight=1)
net.add_edge(id_DATA832a, id_TC_3_2, weight=1)

id_INFO831a = get_module_id("INFO831a")
net.add_edge(id_INFO831a, id_IDU_1_3, weight=1)
net.add_edge(id_INFO831a, id_IDU_2_1, weight=1)
net.add_edge(id_INFO831a, id_IDU_2_2, weight=1)
net.add_edge(id_INFO831a, id_IDU_3_1, weight=1)
net.add_edge(id_INFO831a, id_TC_3_2, weight=1)

id_PROJ831a = get_module_id("PROJ831a")
net.add_edge(id_PROJ831a, id_IDU_1_1, weight=1)
net.add_edge(id_PROJ831a, id_IDU_2_1, weight=1)

id_INFO832a = get_module_id("INFO832a")
net.add_edge(id_INFO832a, id_IDU_1_1, weight=1)
net.add_edge(id_INFO832a, id_IDU_3_1, weight=1)

id_INFO833a  = get_module_id("INFO833a")
net.add_edge(id_INFO833a, id_IDU_1_1, weight=1)
net.add_edge(id_INFO833a, id_IDU_1_2, weight=1)
net.add_edge(id_INFO833a, id_IDU_1_3, weight=1)
net.add_edge(id_INFO833a, id_IDU_4_1, weight=1)
net.add_edge(id_INFO833a, id_IDU_4_2, weight=1)

id_INFO834a  = get_module_id("INFO834a")
net.add_edge(id_INFO834a, id_TC_3_2, weight=1)
net.add_edge(id_INFO834a, id_TC_1_2, weight=1)
net.add_edge(id_INFO834a, id_IDU_4_1, weight=1)
net.add_edge(id_INFO834a, id_IDU_2_3, weight=1)
net.add_edge(id_INFO834a, id_IDU_1_3, weight=1)
net.add_edge(id_INFO834a, id_IDU_1_2, weight=1)

id_ISOC831a  = get_module_id("ISOC831a")
net.add_edge(id_ISOC831a, id_TC_3_1, weight=1)
net.add_edge(id_ISOC831a, id_TC_3_2, weight=1)
