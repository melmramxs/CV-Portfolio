#!/usr/bin/env python
# coding: utf-8

# In[1]:




#------------------------------------------------------------------------------------------------------------------
#   First order logic examples
#
#   This script contains some examples of first order logic exercises solved in python using the 
#   AIMA code. For more examples, visit https://github.com/aimacode
#
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#   Imports
#------------------------------------------------------------------------------------------------------------------

from utils import *
from logic import *


#------------------------------------------------------------------------------------------------------------------
#   Diccionario de términos
#------------------------------------------------------------------------------------------------------------------

diccionarioEnf = {
    "Celiaca": "Enfermedad Celiaca",
    "Diverticulosis": "Diverticulosis",
    "Colitis": "Colitis ulcerosa",
    "Crohn": "Enfermedad de Crohn",
    "Gastritis": "Gastritis",
    "ERGE": "ERGE",
    "Dispepsia": "Dispepsia",
    "CancerTempr": "Cáncer de estómago temprano",
    "CancerAvanz": "Cáncer de estómago avanzado",
    "Apendicitis": "Apendicitis",
}

diccionarioSintomas ={
    "Anemia": "Anemia",
    "Gases": "Gases",
    "ArdEstomago": "Ardor de estómago",
    "HecesAn": "Heces de color anormal",
    "Ascitis": "Ascitis",
    "Hinchazon": "Hinchazón abdominal",
    "Calambres": "Calambres en estómago",
    "Hipo": "Hipo",
    "Colicos": "Cólicos",
    "Ictericia": "Ictericia",
    "Depresion": "Depresión",
    "Indigestion": "Indigestión o malestar estomacal",
    "Diarrea": "Diarrea",
    "Infertilidad": "Infertilidad",
    "DifTragar": "Dificultad para tragar",
    "IntLact": "Intolerancia a la lactosa",
    "DolAbd": "Dolor abdominal",
    "BanoUrg": "Mayor urgencia para ir al baño",
    "DolAbdInt": "Dolor abdominal intenso que comienza en el área del ombligo y luego se mueve hacia el lado derecho inferior del abdomen.",
    "Nauseas": "Náuseas",
    "DolEst": "Dolor de estómago",
    "NauseasC": "Náuseas después de comer",
    "DolGar": "Dolor de garganta",
    "Apetito": "Pérdida de apetito",
    "DolArt": "Dolor en articulaciones",
    "Peso": "Pérdida de peso",
    "DolEpig": "Dolor epigástrico",
    "Plenitud": "Plenitud molesta durante y/o después de comer",
    "DolPecho": "Dolor urente en el pecho",
    "Protuberancias": "Protuberancias rojas",
    "DolCab": "Dolores de cabeza",
    "Pus": "Pus en la orina",
    "EnrOjo": "Enrojecimiento de ojo",
    "Regurgitacion": "Regurgitación",
    "Escalofrios": "Escalofríos",
    "Roncar": "Ronquera o cambios en la voz",
    "Estrenimiento": "Estreñimiento",
    "Sangrado": "Sangrado",
    "Fatiga": "Fatiga",
    "AlimEsternon": "Sentir que el alimento se atora por detrás del esternón",
    "Fiebre": "Fiebre",
    "Tos": "Tos o sibilancias",
    "BanoConst": "Ganas constantes de ir al baño",
    "Vomito": "Vómito"
    }

diccionarioTrat = {
    "Gluten": "Tener una dieta sin gluten",
    "Suplementos": "Suplementos de vitaminas y minerales",
    "Quimioterapia": "Quimioterapia",
    "Antibioticos": "Antibióticos",
    "Liquidos": "Consumir solamente líquidos por un tiempo para dejar descansar el colon",
    "Transfusion": "Transfusión de sangre",
    "Probioticos": "Probióticos",
    "Antiespasmodicos": "Antiespasmódicos para reducir el dolor",
    "CirugiaColon": "Cirugía para extirpar el colon",
    "Hidratacion": "Hidratación",
    "Aminosalicilatos": "Aminosalicilatos",
    "Corticoesteroides": "Corticosteroides",
    "Immunomoduladores": "Immunomoduladores",
    "TerapiasBiologicas": "Terapias biológicas",
    "MedicinaMolecular": "Medicina molecular",
    "Inhibidores": "Inhibidores de la bomba de protones",
    "Radioterapia": "Radioterapia",
    "BajarPeso": "Bajar de peso",
    "ElevarCabeza": "Elevar la cabecera de la cama",
    "CenarTempr": "Cenar 2 a 3 horas antes de ir a dormir",
    "MedicamentoAgua": "Tomar todos sus medicamentos con bastante agua",
    "Antiacidos": "Usar antiácidos de venta libre",
    "ComidasPeq": "Comer varias comidas pequeñas, bajas en grasas, durante todo el día a un ritmo lento",
    "Apendicectomia": "Apendicectomía",
    "Fumar": "No fumar",
    "Cafe": "No consumir café",
    "Refresco": "No consumir bebidas carbonatadas",
    "Alcohol": "No consumir alcohol",
    "Descanso": "Tener suficiente descanso",
    "Estres": "Someterse a situaciones de estrés",
    "Reseccion": "Resección endoscópica",
    "GastrParcial": "Gastrectomía parcial",
    "GastrTotal": "Gastrectomía total",
    "ConsultarDoctor": "Consultar con un doctor"
    }

#------------------------------------------------------------------------------------------------------------------
#   Enfermedades-Síntomas-Tratamiento KB
#------------------------------------------------------------------------------------------------------------------
clauses = []
continuar= True
## Definicion de enfermedades a partir de sintomas

# Enfermedad celiaca
clauses.append(expr("(Sintoma(x, Estrenimiento) & Sintoma(x, Gases) & Sintoma(x, IntLact) & Sintoma(x, Nauseas) & Sintoma(x, Vomito) & Sintoma(x, DolAbd) & Sintoma(x, Fatiga) & Sintoma(x, DolArt) & Sintoma(x, Depresion) & Sintoma(x, DolCab) & Sintoma(x, Infertilidad) ) ==> Enfermo(x, Celiaca)"))

# Diverticulosis
clauses.append(expr("(Sintoma(x, DolAbd) & Sintoma(x, Colicos) & Sintoma(x, Estrenimiento) & Sintoma(x, Diarrea) & Sintoma(x, Fiebre) & Sintoma(x, Escalofrios) & Sintoma(x, Nauseas) & Sintoma(x, Vomito)) ==> Enfermo(x, Diverticulosis)"))

# Colitis ulcerosa
clauses.append(expr("(Sintoma(x, Diarrea) & Sintoma(x, Sangrado) & Sintoma(x, DolAbd) & Sintoma(x, Colicos) & Sintoma(x, Pus) & Sintoma(x, BanoConst) & Sintoma(x, BanoUrg) & Sintoma(x, Fatiga) & Sintoma(x, Fiebre) & Sintoma(x, Peso) & Sintoma(x, Nauseas) & Sintoma(x, Vomito)) ==> Enfermo(x, Colitis)"))

# Enfermedad de Crohn
clauses.append(expr("(Sintoma(x, Diarrea) & Sintoma(x, DolAbd) & Sintoma(x, Peso) & Sintoma(x, Anemia) & Sintoma(x, EnrOjo) & Sintoma(x, Fatiga) & Sintoma(x, Fiebre) & Sintoma(x, DolArt) & Sintoma(x, Nauseas) & Sintoma(x, Protuberancias)) ==> Enfermo(x, Crohn)"))

# Gastritis
clauses.append(expr("(Sintoma(x, DolAbd) & Sintoma(x, Nauseas) & Sintoma(x, Vomito) & Sintoma(x, Apetito) & Sintoma(x, Peso) & Sintoma(x, Sangrado) & Sintoma(x, Calambres) & Sintoma(x, HecesAn) & Sintoma(x, Fatiga))  ==> Enfermo(x, Gastritis)"))

# ERGE
clauses.append(expr("(Sintoma(x, NauseasC) & Sintoma(x, AlimEsternon) & Sintoma(x, Nauseas) & Sintoma(x, Regurgitacion) & Sintoma(x, Tos) & Sintoma(x, DifTragar) & Sintoma(x, Hipo) & Sintoma(x, Roncar) & Sintoma(x, DolGar) & Sintoma(x, DolPecho)) ==> Enfermo(x, ERGE)"))

# Dispepsia
clauses.append(expr("(Sintoma(x, ArdEstomago) & Sintoma(x, DolEpig) & Sintoma(x,  Plenitud) ) ==> Enfermo(x, Dispepsia)"))

# Cáncer de estómago estadío temprano
clauses.append(expr("(Sintoma(x, ArdEstomago) & Sintoma(x, Apetito) & Sintoma(x, Nauseas) & Sintoma(x, Hinchazon) & Sintoma(x, Indigestion)) ==> Enfermo(x, CancerTempr)"))

# Cáncer de estómago estadío avanzado
clauses.append(expr("(Sintoma(x, DifTragar) & Sintoma(x, Ascitis) & Sintoma(x,  Ictericia) & Sintoma(x, Peso) & Sintoma(x, Vomito) & Sintoma(x, Sangrado)) ==> Enfermo(x, CancerAvanz)"))

# Apendicitis
clauses.append(expr("(Sintoma(x, DolAbd) & Sintoma(x, DolAbdInt) & Sintoma(x,  Fiebre) & Sintoma(x, Hinchazon) & Sintoma(x, Vomito) & Sintoma(x, Nauseas) & Sintoma(x, Apetito) & Sintoma(x, Plenitud) ) ==> Enfermo(x, Apendicitis)"))


## Definicion de tratamiento a partir de enfermedad

# Enfermedad celiaca

clauses.append(expr("Enfermo(x, Celiaca) ==> Tratamiento(x, Gluten)"))
clauses.append(expr("Enfermo(x, Celiaca) ==> Tratamiento(x, Suplementos)"))

# Diverticulosis

clauses.append(expr("Enfermo(x, Diverticulosis) ==> Tratamiento(x, Gluten)"))
clauses.append(expr("Enfermo(x, Diverticulosis) ==> Tratamiento(x, Liquidos)"))
clauses.append(expr("Enfermo(x, Diverticulosis) ==> Tratamiento(x, Antibioticos)"))
clauses.append(expr("Enfermo(x, Diverticulosis) ==> Tratamiento(x, Probioticos)"))

# Colitis ulcerosa

clauses.append(expr("Enfermo(x, Colitis) ==> Tratamiento(x, Aminosalicilatos)"))
clauses.append(expr("Enfermo(x, Colitis) ==> Tratamiento(x, Immunomoduladores)"))
clauses.append(expr("Enfermo(x, Colitis) ==> Tratamiento(x, Corticosteroides)"))
clauses.append(expr("Enfermo(x, Colitis) ==> Tratamiento(x, Suplementos)"))
clauses.append(expr("Enfermo(x, Colitis) ==> Tratamiento(x, Hidratacion)"))

# Enfermedad de Crohn
clauses.append(expr("Enfermo(x, Crohn) ==> Tratamiento(x, Aminosalicilatos)"))
clauses.append(expr("Enfermo(x, Crohn) ==> Tratamiento(x, Corticoesteroides)"))
clauses.append(expr("Enfermo(x, Crohn) ==> Tratamiento(x, Immunomoduladores)"))

#Gastritis
clauses.append(expr("Enfermo(x, Gastritis) ==> Tratamiento(x, Antibioticos)"))
clauses.append(expr("Enfermo(x, Gastritis) ==> Tratamiento(x, Suplementos)"))
clauses.append(expr("Enfermo(x, Gastritis) ==> Tratamiento(x, Inhibidores)"))

# ERGE
clauses.append(expr("Enfermo(x, ERGE) ==> Tratamiento(x, BajarPeso)"))
clauses.append(expr("Enfermo(x, ERGE) ==> Tratamiento(x, ElevarCabeza)"))
clauses.append(expr("Enfermo(x, ERGE) ==> Tratamiento(x, CenarTempr)"))
clauses.append(expr("Enfermo(x, ERGE) ==> Tratamiento(x, MedicamentoAgua)"))
clauses.append(expr("Enfermo(x, ERGE) ==> Tratamiento(x, Antiacidos)"))

# Dispepsia
clauses.append(expr("Enfermo(x, Dispepsia) ==> Tratamiento(x, ComidasPeq)"))
clauses.append(expr("Enfermo(x, Dispepsia) ==> Tratamiento(x, Fumar)"))
clauses.append(expr("Enfermo(x, Dispepsia) ==> Tratamiento(x, Cafe)"))
clauses.append(expr("Enfermo(x, Dispepsia) ==> Tratamiento(x, Refresco)"))
clauses.append(expr("Enfermo(x, Dispepsia) ==> Tratamiento(x, Alcohol)"))
clauses.append(expr("Enfermo(x, Dispepsia) ==> Tratamiento(x, Descanso)"))
clauses.append(expr("Enfermo(x, Dispepsia) ==> Tratamiento(x, Estres)"))
clauses.append(expr("Enfermo(x, Dispepsia) ==> Tratamiento(x, Antiacidos)"))

# Cancer temprano
clauses.append(expr("Enfermo(x, CancerTempr) ==> Tratamiento(x, Reseccion)"))
clauses.append(expr("Enfermo(x, CancerTempr) ==> Tratamiento(x, GastrParcial)"))
clauses.append(expr("Enfermo(x, CancerTempr) ==> Tratamiento(x, GastrTotal)"))
clauses.append(expr("Enfermo(x, CancerTempr) ==> Tratamiento(x, Quimioterapia)"))
clauses.append(expr("Enfermo(x, CancerTempr) ==> Tratamiento(x, Radioterapia)"))

# Cancer tardío
clauses.append(expr("Enfermo(x, CancerAvanz) ==> Tratamiento(x, ConsultarDoctor)"))

# Apendicitis
clauses.append(expr("Enfermo(x, Apendicitis) ==> Tratamiento(x, Apendicectomia)"))


## Base de conocimiento
kb = FolKB(clauses)


#------------------------------------------------------------------------------------------------------------------
#   Forward chaining
#------------------------------------------------------------------------------------------------------------------

# Diagnostico
def diagnostico():
    print("\nSintomas del paciente {}: ".format(name))
    sintomas1= fol_fc_ask(kb, expr("Sintoma({}, x)".format(name)))
    sintomas1=list(sintomas1)
    
    if len(sintomas1)>0:
        for sintoms in sintomas1:
            print(diccionarioSintomas[str(sintoms[x])])
    else:
        print("No hay diagnostico")
        
    print("\nTu diagnóstico es: ")
    diagnostico= fol_fc_ask(kb, expr("Enfermo({}, x)".format(name)))
    diagnostico=list(diagnostico)
    
    if len(diagnostico)>0:
        for diagnostic in diagnostico:
            print(diccionarioEnf[str(diagnostic[x])])
    else:
        print("No hay diagnostico")
        
    print("\nTu tratamiento es: ")
    tratamiento= fol_fc_ask(kb, expr("Tratamiento({}, x)".format(name)))
    tratamiento=list(tratamiento)
    
    if len(tratamiento)>0:
        for treatmet in tratamiento:
            print(diccionarioTrat[str(treatmet[x])])
    else:
        print("No hay tratamientos\n")
    
        
    return [sintomas1, diagnostico, tratamiento]

#------------------------------------------------------------------------------------------------------------------
#   Preguntas
#------------------------------------------------------------------------------------------------------------------
name=input("¿Cuál es tu nombre?: ")

if (input("¿Tiene usted fiebre?").lower()=="s"):
    kb.tell(expr("Sintoma({}, Fiebre)".format(name)))

if(input("¿Ha perdido usted peso recientemente?").lower() == "s"):
    kb.tell(expr("Sintoma({}, Peso)".format(name)))
    
if(input("¿Presenta usted sangrado?").lower() == "s"):
    kb.tell(expr("Sintoma({}, Sangrado)".format(name)))
    
if (input("¿Siente usted ardor de estómago?").lower()=="s"):
    kb.tell(expr("Sintoma({}, ArdEstomago)".format(name)))
    
if(input("¿Ha experimentado usted pérdida de apetito?").lower() == "s"):
    kb.tell(expr("Sintoma({}, Apetito)".format(name)))
    
#Nauseas VERDADERO
if(input("¿Tiene usted náuseas?").lower() == "s"):
    kb.tell(expr("Sintoma({}, Nauseas)".format(name)))
    if(input("¿Ha experimentado usted vómitos?").lower() == "s"):
        kb.tell(expr("Sintoma({}, Vomito)".format(name)))
        #DolAbd VERDADERO
        if (input("¿Siente usted dolor abdominal?").lower()=="s"):
            kb.tell(expr("Sintoma({}, DolAbd)".format(name)))
            #Diarrea VERDADERO
            if (input("¿Tiene usted diarrea?").lower()=="s"):
                kb.tell(expr("Sintoma({}, Diarrea)".format(name)))
                #Fatiga VERDADERO
                if (input("¿Experimenta usted fatiga?").lower()=="s"):
                    kb.tell(expr("Sintoma({}, Fatiga)".format(name)))
                    #CELIACA
                    if (input("¿Ha experimentado problemas de depresión en los últimos 2 meses?").lower()=="s"):
                        kb.tell(expr("Sintoma({}, Depresion)".format(name)))
                        if (input("¿Tiene usted dolores de cabeza?").lower()=="s"):
                            kb.tell(expr("Sintoma({}, DolCab)".format(name)))
                            if (input("¿Tiene usted gases?").lower()=="s"):
                                kb.tell(expr("Sintoma({}, Gases)".format(name)))
                                if(input("¿Tiene usted intolerancia a la lactosa?").lower() == "s"):
                                    kb.tell(expr("Sintoma({}, IntLact)".format(name)))
                                    if (input("¿Es propenso a sufrir de estreñimiento?").lower()=="s"):
                                        kb.tell(expr("Sintoma({}, Estrenimiento)".format(name)))
                                        if (input("¿Experimenta usted dolor en las articulaciones?").lower()=="s"):
                                            kb.tell(expr("Sintoma({}, DolArt)".format(name)))
                                            if (input("¿Tiene usted infertilidad?").lower()=="s"):
                                                kb.tell(expr("Sintoma({}, Infertilidad)".format(name)))
                                                diagnostico()
                                                continuar=False
                    #COLITIS
                    if continuar==True:
                        if (input("¿Siente usted ganas constantes de ir al baño?").lower()=="s"):
                            kb.tell(expr("Sintoma({}, BanoConst)".format(name)))
                            if(input("¿Siente usted una mayor urgencia para ir al baño?").lower()== "s"):
                                kb.tell(expr("Sintoma({}, BanoUrg)".format(name)))
                                if(input("¿Tiene usted pus en la orina?").lower()== "s"):
                                    kb.tell(expr("Sintoma({}, Pus)".format(name)))
                                    if (input("¿Sufre usted de cólicos?").lower()=="s"):
                                        kb.tell(expr("Sintoma({}, Colicos)".format(name)))
                                        diagnostico()
                                        continuar=False
                #Fatiga FALSO
                #DIVERTICULITIS
                if continuar==True:
                    if (input("¿Es propenso a sufrir de estreñimiento?").lower()=="s"):
                        kb.tell(expr("Sintoma({}, Estrenimiento)".format(name)))
                        if (input("¿Experimenta usted escalofríos?").lower()=="s"):
                            kb.tell(expr("Sintoma({}, Escalofrios)".format(name)))
                            if (input("¿Sufre usted de cólicos?").lower()=="s"):
                                kb.tell(expr("Sintoma({}, Colicos)".format(name)))
                                diagnostico()
                                continuar=False
            #Diarrea FALSO
            #GASTRITIS
            if continuar==True:
                if (input("¿Experimenta usted calambres en el estómago?").lower()=="s"):
                    kb.tell(expr("Sintoma({}, Calambres)".format(name)))
                    if (input("¿Tiene usted heces de color anormal?").lower()=="s"):
                        kb.tell(expr("Sintoma({}, HecesAn)".format(name)))
                        if (input("¿Experimenta usted fatiga?").lower()=="s"):
                            kb.tell(expr("Sintoma({}, Fatiga)".format(name)))
                            diagnostico()
                            continuar=False
            #APENDICITIS
            if continuar==True:
                if (input("¿Experimenta usted dolor abdominal intenso que comienza en el área del ombligo y luego se mueve hacia el lado derecho inferior del abdomen?").lower()=="s"):
                    kb.tell(expr("Sintoma({}, DolAbdInt)".format(name)))
                    if(input("¿Siente usted plenitud molesta durante y/o después de comer?").lower() == "s"):
                        kb.tell(expr("Sintoma({}, Plenitud)".format(name)))
                        if (input("¿Presenta usted hinchazón abdominal?").lower()=="s"):
                            kb.tell(expr("Sintoma({}, Hinchazon)".format(name)))    
                            diagnostico()
                            continuar=False
   #Vomito FALSO
    #CROHN
    if continuar==True:
        if (input("¿Siente usted dolor abdominal?").lower()=="s"):
            kb.tell(expr("Sintoma({}, DolAbd)".format(name)))
            if (input("¿Tiene usted diarrea?").lower()=="s"):
                kb.tell(expr("Sintoma({}, Diarrea)".format(name)))
                if (input("¿Experimenta usted fatiga?").lower()=="s"):
                    kb.tell(expr("Sintoma({}, Fatiga)".format(name)))
                    if (input("¿Experimenta usted anemia?").lower()=="s"):
                        kb.tell(expr("Sintoma({}, Anemia)".format(name)))
                        if(input("¿Tiene usted protuberancias rojas?").lower() == "s"):
                            kb.tell(expr("Sintoma({}, Protuberancias)".format(name)))
                            if (input("¿Tiene usted enrojecimiento en el ojo?").lower()=="s"):
                                kb.tell(expr("Sintoma({}, EnrOjo)".format(name)))
                                if (input("¿Experimenta usted dolor en las articulaciones?").lower()=="s"):
                                    kb.tell(expr("Sintoma({}, DolArt)".format(name)))   
                                    diagnostico()
                                    continuar=False
    #ERGE
    if continuar==True:
        if (input("¿Tiene usted dificultad para tragar?").lower()=="s"):
            kb.tell(expr("Sintoma({}, DifTragar)".format(name))) 
            if(input("¿Experimenta usted náuseas después de comer?").lower() == "s"):
                kb.tell(expr("Sintoma({}, NauseasC)".format(name)))
                if(input("¿Sufre usted de regurgitación?").lower() == "s"):
                    kb.tell(expr("Sintoma({}, Regurgitacion)".format(name)))
                    if(input("¿Siente usted que el alimento se le atasca por detrás del esternón?").lower() == "s"):
                        kb.tell(expr("Sintoma({}, AlimEsternon)".format(name)))
                        if (input("¿Siente usted dolor de garganta?").lower()=="s"):
                            kb.tell(expr("Sintoma({}, DolGar)".format(name)))
                            if(input("¿Tiene usted tos o sibilancias?").lower() == "s"):
                                kb.tell(expr("Sintoma({}, Tos)".format(name)))
                                if (input("¿Sufre usted de dolor urente en el pecho?").lower()=="s"):
                                    kb.tell(expr("Sintoma({}, DolPecho)".format(name)))
                                    if (input("¿Tiene usted hipo?").lower()=="s"):
                                        kb.tell(expr("Sintoma({}, Hipo)".format(name)))
                                        if(input("¿Experimenta usted ronquera o cambios en la voz?").lower() == "s"):
                                            kb.tell(expr("Sintoma({}, Roncar)".format(name)))
                                            diagnostico()
                                            continuar=False
    #CANCER TEMPRANO
    if continuar==True:
        if (input("¿Experimenta usted indigestión o malestar estomacal?").lower()=="s"):
            kb.tell(expr("Sintoma({}, Indigestion)".format(name)))
            if (input("¿Presenta usted hinchazón abdominal?").lower()=="s"):
                kb.tell(expr("Sintoma({}, Hinchazon)".format(name)))
                diagnostico()
                continuar=False
#Nauseas FALSO                                 
#CANCER AVANZADO
if continuar==True:
    if (input("¿Tiene usted dificultad para tragar?").lower()=="s"):
        kb.tell(expr("Sintoma({}, DifTragar)".format(name))) 
        if (input("¿Tiene usted dolor de estómago?").lower()=="s"):
            kb.tell(expr("Sintoma({}, DolEst)".format(name)))
            if(input("¿Ha experimentado usted vómitos?").lower() == "s"):
                kb.tell(expr("Sintoma({}, Vomito)".format(name)))
                if (input("¿Presenta usted ictericia?").lower()=="s"):
                    kb.tell(expr("Sintoma({}, Ictericia)".format(name)))  
                    if (input("¿Tiene usted ascitis?").lower()=="s"):
                        kb.tell(expr("Sintoma({}, Ascitis)".format(name)))
                        diagnostico()
                        continuar=False
                        
#DISPEPSIA
if continuar==True:
    if (input("¿Tiene usted dolor epigástrico?").lower()=="s"):
        kb.tell(expr("Sintoma({}, DolEpig)".format(name)))
        if(input("¿Siente usted plenitud molesta durante y/o después de comer?").lower() == "s"):
            kb.tell(expr("Sintoma({}, Plenitud)".format(name)))
            diagnostico()
            continuar=False
if continuar==True:            
    diagnostico()
#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------



# In[ ]:




