import tabula
from textReader import text, semestre_UE, UE_module_court

text = text
# we take the second table
df = tabula.read_pdf('Referentiel_Competences_IDU_2021_2025.pdf', pages='all')[2]
p_ue_competence = df["UE"]
# test
# print(ue_competence)


def change_to_str(text):
    """ 
    change an input to str
    """
    return str(text)


def matching_ue_name(roughly_eu_name, semestre, fichier=text):
    """ 
    take a the roughly ue name and the semestre id then return the correct ue name
    """
    rigth_ue_name = ""
    relation_semestre_ue = semestre_UE(fichier)
    for item in relation_semestre_ue.items():
        if semestre[1] in item[0]:
            for ue in item[1]:
                if roughly_eu_name[2] in ue:
                    rigth_ue_name = ue
    return rigth_ue_name


# test
# print( matching_ue_name("UE1", "s7"))


def competence_ue(p_ue_competence, fichier):
    """
    return the relation between module and skills
    """
    relation_ue_module = UE_module_court(fichier)
    relation_compentence_module = {"TC": [], "IDU": []}
    for relation in p_ue_competence:
        if change_to_str(relation) == "nan":
            pass
        else:
            split_relation = change_to_str(relation).split("-")
            competence = split_relation[2]
            ue = split_relation[0]
            sem = split_relation[1]
            ue_name = matching_ue_name(ue, sem)
            for item in relation_ue_module.items():
                if item[0] == ue_name:
                    if competence == "TC":
                        cal1 = relation_compentence_module.get("TC") + item[1]
                        relation_compentence_module.update({"TC": cal1})
                    else:
                        cal = relation_compentence_module.get("IDU") + item[1]
                        relation_compentence_module.update({"IDU": cal})
    return relation_compentence_module


# test
# print( competence_ue(ue_competence, text) )


def competence_spe_info():
    """
    return more information about idu skill
    """
    table1 = tabula.read_pdf('Referentiel_Competences_IDU_2021_2025.pdf', pages='all')[0]
    table2 = tabula.read_pdf('Referentiel_Competences_IDU_2021_2025.pdf', pages='all')[1]
    liste = [table1, table2]
    competence_info = {"IDU": [], "TC": []}
    for table in liste:
        table_info = table.values
        for value in table_info:
            if change_to_str(value[2]).split("-")[0] == "IDU":
                competence_info.get("IDU").append(value[2])
            if change_to_str(value[2]).split("-")[0] == "TC":
                competence_info.get("TC").append(value[2])
    # adjustment for data loss errors
    competence_info.get("IDU").append('IDU-4.2')
    competence_info.get("TC").append('TC-1.1')
    competence_info.get("TC").append('TC-1.2')
    competence_info.get("TC").append('TC-1.3')
    competence_info.get("TC").append('TC-4.2')
    competence_info.get("TC").append('TC-4.3')
    competence_info.get("TC").append('TC-4.4')
    return competence_info


# test
# print(len(competence_spe_info()))
